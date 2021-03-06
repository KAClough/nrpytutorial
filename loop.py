# This module contains infrastructure for generating
#   C-code loops of arbitrary dimension

# Author: Zachariah B. Etienne
#         zachetie **at** gmail **dot* com

import sys                         # Standard Python modules for multiplatform OS-level functions

# loop1D() is just a special case of loop(), and in fact is called by loop().
#   For documentation on the inputs, see loop()'s documentation below.
def loop1D(idxvar="i0",lower="0",upper="Nx0",incr="1",OpenMPpragma="#pragma omp parallel for",tabprefix=""):
    if not (isinstance(idxvar, str) and isinstance(lower, str) and
            isinstance(upper, str) and isinstance(incr, str) and isinstance(OpenMPpragma, str)):
        print("Error: all inputs to loop1D() must be STRINGS, and to loop() must be LISTS OF STRINGS")
        sys.exit(1)
    OMPheader = ""
    if OpenMPpragma != "":
        OMPheader = OpenMPpragma + "\n"
    incrstr = "++"
    if incr != "1":
        incrstr = "+="+incr
    loopbody = tabprefix+"for(int "+idxvar+"="+lower+"; "+idxvar+"<"+upper+"; "+idxvar+incrstr+")"
    return OMPheader+loopbody+" {\n", tabprefix+"} // END LOOP: "+loopbody.replace(tabprefix,"")+"\n"

# loop() creates a C code loop, taking as input:
#    idxvar (string or list of strings): the index variable name or list of names.
#        In the case that idxvar is a list of N strings, we adopt the formulation:
#            idxvar[0]=outermost loop variable
#            idxvar[N-1]=innermost loop variable
#    lower (string or list of strings): lower loop index of idxvar or idxvar[i].
#         See definition of "idxvar" if lower is a list of strings. 
#         idxvar[] must have the same length as idxvar.
#    upper (string or list of strings): Defined similarly to "lower", except
#         this refers to the *upper* loop index of idxvar or idxvar[i].
#    incr (string or list of strings):  Defined similarly to "lower", except
#         this refers to the loop increment of idxvar or idxvar[i]
#         (incr[i] = 1 -> idxvar++)
#    OpenMPpragma (string or list of strings): Defined similarly to "lower", except
#         this refers to the OpenMP pragma corresponding to idxvar or idxvar[i].
#    tabprefix (optional; string): Sets the tab stop for the C code.
#    loopguts (optional; string): The loop interior.
#
# Example: loop(["i0","i1"],["0","5"],["N","N-5"],["1","5"],["#pragma omp parallel for",""],
#               "double a=-2;\n gf[IDX3(GF,i0,i1)]=-2*a;\n"])
# Output:
# #pragma omp parallel for
# for(int i0=0;i0<N;i0++) {
#     for(int i1=5;i1<N-5;i1+=5) {
#         a=-2;
#         gf[IDX3(GF,i0,i1)]=-2*a;
#     } // END LOOP: for(int i1=5;i1<N-5;i1+=5)
# } // END LOOP: for(int i0=0;i0<N;i0++)
def loop(idxvar,lower,upper,incr,OpenMPpragma,tabprefix="",loopguts=""):
    # Step 1: Check and/or clean input. 
    # Step 1a: If only strings are passed, then create lists out of them:
    if (isinstance(idxvar,str) and isinstance(lower,str) and
        isinstance(upper, str) and isinstance(incr, str) and isinstance(OpenMPpragma, str)):
        idxvar = [idxvar]
        lower = [lower]
        upper = [upper]
        incr = [incr]
        OpenMPpragma = [OpenMPpragma]
    # Step 1b: At this point all inputs should be lists. If they are not, then exit.
    if not (isinstance(idxvar,list) and isinstance(lower,list) and
            isinstance(upper, list) and isinstance(incr, list) and isinstance(OpenMPpragma, list)):
        print("Error: loop(idxvar,lower,upper,incr,OpenMPpragma) requires all inputs be lists")
        sys.exit(1)
    # Step 1c: At this point all inputs should be lists. If they are not the same length, then exit.
    if len(idxvar) != len(lower) or len(lower) != len(upper) or len(upper) != len(incr) or len(incr) != len(
            OpenMPpragma):
        print("Error: loop(idxvar,lower,upper,incr,OpenMPpragma) requires all inputs be lists OF THE SAME LENGTH")
        sys.exit(1)
    # Step 2: tabprefix will be set according to the loop nesting, so the loop has proper tabination;
    #         one tab for each nesting of the loop.
    # Step 3: header will be the top of the loop
    header = ""
    # Step 4: footerarray 
    footerarray = []
    for i in range(len(idxvar)):
        headerstr,footerstr = loop1D(idxvar[i],lower[i],upper[i],incr[i],OpenMPpragma[i],tabprefix)
        header += headerstr
        footerarray.append(footerstr)
        tabprefix += "    "
    loopgutsout = ""
    if loopguts != "":
        loopgutsarray = loopguts.split("\n")
        for line in loopgutsarray:
            loopgutsout += tabprefix+line+"\n"
    footer = ""
    for i in range(len(idxvar)-1,-1,-1):
        footer += footerarray[i]
    if loopguts == "":
        return header,footer
    return header+loopgutsout+footer

# Automatic generation of C-code loops around an arbitrarily
#     defined loop body.
def simple_loop(loopopts, body):
    if loopopts == "":
        return body

    if "AllPoints" in loopopts:
        i2i1i0_mins = ["0", "0", "0"]
        i2i1i0_maxs = ["Nxx_plus_2NGHOSTS2", "Nxx_plus_2NGHOSTS1", "Nxx_plus_2NGHOSTS0"]
        if "oldloops" in loopopts:
            i2i1i0_maxs = ["Nxx_plus_2NGHOSTS[2]", "Nxx_plus_2NGHOSTS[1]", "Nxx_plus_2NGHOSTS[0]"]
    elif "InteriorPoints" in loopopts:
        i2i1i0_mins = ["NGHOSTS","NGHOSTS","NGHOSTS"]
        i2i1i0_maxs = ["NGHOSTS+Nxx2","NGHOSTS+Nxx1","NGHOSTS+Nxx0"]
        if "oldloops" in loopopts:
            i2i1i0_maxs = ["NGHOSTS+Nxx[2]", "NGHOSTS+Nxx[1]", "NGHOSTS+Nxx[0]"]
    else:
        print("Error: loopopts given, but no points over which to loop were specified.")
        sys.exit(1)

    Read_1Darrays = ["", "", ""]
    if "Read_xxs" in loopopts:
        if not "EnableSIMD" in loopopts:
            Read_1Darrays = ["const REAL xx0 = xx[0][i0];",
                             "            const REAL xx1 = xx[1][i1];",
                             "        const REAL xx2 = xx[2][i2];", ]
        else:
            print("Error: No SIMD support on Read_xxs yet.")
            sys.exit(1)

    if "Enable_rfm_precompute" in loopopts:
        if "Read_xxs" in loopopts:
            print("Error: Enable_rfm_precompute and Read_xxs cannot both be enabled.")
            sys.exit(1)
        if "EnableSIMD" in loopopts:
            Read_1Darrays = ["#include \"rfm_files/rfm_struct__SIMD_inner_read0.h\"",
                             "#include \"rfm_files/rfm_struct__SIMD_outer_read1.h\"",
                             "#include \"rfm_files/rfm_struct__SIMD_outer_read2.h\""]
        else:
            Read_1Darrays = ["#include \"rfm_files/rfm_struct__read0.h\"",
                             "#include \"rfm_files/rfm_struct__read1.h\"",
                             "#include \"rfm_files/rfm_struct__read2.h\""]

    OpenMPpragma = "#pragma omp parallel for"
    if "DisableOpenMP" in loopopts:
        OpenMPpragma = ""

    loopincrements = ["1","1","1"]
    if "EnableSIMD" in loopopts:
        loopincrements = ["1", "1", "SIMD_width"]

    return loop(["i2","i1","i0"],i2i1i0_mins,i2i1i0_maxs,loopincrements,
                [OpenMPpragma,Read_1Darrays[2],Read_1Darrays[1]],tabprefix="    ",loopguts = Read_1Darrays[0]+"\n"+body)


#loopheader,loopfooter = loop(idxvar=["i0","i1"],lower=["0","0"],upper=["Nx0","Nx1"],incr=["1","1"],
#                             OpenMPpragma=["", "#pragma omp parallel for"])
#loopheader,loopfooter = loop(idxvar=["i0","i1"],lower=["0","0"],upper=["Nx0","Nx1"],incr=["1","1"],
#                             OpenMPpragma=["", "#pragma omp parallel for"])
#print(loopheader+loopfooter)
