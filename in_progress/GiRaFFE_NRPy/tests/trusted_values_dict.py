from mpmath import mpf, mp, mpc
from UnitTesting.standard_constants import precision

mp.dps = precision
trusted_values_dict = {}

# Generated on: 2019-10-08
# Reason for changing values: Issue with lowering operator on u^{\mu} to compute u_j. Stilde_rhsD affected as well.
trusted_values_dict['GiRaFFE_HO__GiRaFFE_Higher_Order__globals'] = {'A_rhsD[0]': mpc(real='-0.733235010089164696012176136719', imag='0.165576521170778173663862276044'), 'A_rhsD[1]': mpc(real='-0.27204726861856154407348640234', imag='-0.158378065480573926304685983268'), 'A_rhsD[2]': mpc(real='-0.447485382816490862012415163917', imag='-0.113920141861762774793120911454'), 'AevolParen': mpc(real='-1.33624532586521493904285762255', imag='-0.344717596676114568232662804803'), 'alpsqrtgam': mpc(real='0.0', imag='0.287206864362771430165821584524'), 'gammadet': mpf('-0.249945345858354359323568625781'), 'gammaUU[0][0]': mpf('1.5685144003653602430227467825'), 'gammaUU[0][1]': mpf('-0.918925735762276382088541324239'), 'gammaUU[0][2]': mpf('0.0556557158507127226919364696343'), 'gammaUU[1][0]': mpf('-0.918925735762276382088541324239'), 'gammaUU[1][1]': mpf('-1.80649576353102912734623132484'), 'gammaUU[1][2]': mpf('1.81188776789429056085099706766'), 'gammaUU[2][0]': mpf('0.0556557158507127226919364696343'), 'gammaUU[2][1]': mpf('1.81188776789429056085099706766'), 'gammaUU[2][2]': mpf('-0.361125192285811549808229761942'), 'PevolParenU[0]': mpc(real='-0.223244664097171335859215446362', imag='-0.0705095579135382177771163014768'), 'PevolParenU[1]': mpc(real='-0.087517094413118015627794932243', imag='-0.0838494759844927717296059199725'), 'PevolParenU[2]': mpc(real='-0.235728967783171816652298957706', imag='0.405016702547488505192774255192'), 'psi6Phi_rhs': mpf('-1.22513083961622711186385532584'), 'Stilde_rhsD[0]': mpc(real='0.0791147549814407019530548836883', imag='0.194417761497892832567302434654'), 'Stilde_rhsD[1]': mpc(real='-0.215262963977954052685603869577', imag='-0.00388867096871151453688075783077'), 'Stilde_rhsD[2]': mpc(real='0.176710658059943709341510498234', imag='0.117773774657098581619685262467'), 'u0alpha': mpf('0.367135744642744378541883654491'), 'uD[0]': mpf('0.156151565266665266967701965089'), 'uD[1]': mpf('0.101833114422742486298693165777'), 'uD[2]': mpf('0.265850154315525160646297945124'), 'uU[0]': mpf('-0.309433032761499727934847830213'), 'uU[1]': mpf('-0.0321997718658402285660564677369'), 'uU[2]': mpf('-0.40497761650374306520442195942')}


# Generated on: 2019-10-08
# Reason for changing values: Issue with lowering operator on u^{\mu} to compute u_j. Stilde_rhsD and SevolParenUD affected.
trusted_values_dict['GiRaFFE_HO_v2__GiRaFFE_Higher_Order_v2__globals'] = {'A_rhsD[0]': mpc(real='-0.733235010089164696012176136719', imag='0.165576521170778173663862276044'), 'A_rhsD[1]': mpc(real='-0.27204726861856154407348640234', imag='-0.158378065480573926304685983268'), 'A_rhsD[2]': mpc(real='-0.447485382816490862012415163917', imag='-0.113920141861762774793120911454'), 'AevolParen': mpc(real='-1.33624532586521493904285762255', imag='-0.344717596676114568232662804803'), 'gammadet': mpf('-0.249945345858354359323568625781'), 'gammaUU[0][0]': mpf('1.5685144003653602430227467825'), 'gammaUU[0][1]': mpf('-0.918925735762276382088541324239'), 'gammaUU[0][2]': mpf('0.0556557158507127226919364696343'), 'gammaUU[1][0]': mpf('-0.918925735762276382088541324239'), 'gammaUU[1][1]': mpf('-1.80649576353102912734623132484'), 'gammaUU[1][2]': mpf('1.81188776789429056085099706766'), 'gammaUU[2][0]': mpf('0.0556557158507127226919364696343'), 'gammaUU[2][1]': mpf('1.81188776789429056085099706766'), 'gammaUU[2][2]': mpf('-0.361125192285811549808229761942'), 'PevolParenU[0]': mpc(real='-0.223244664097171335859215446362', imag='-0.0705095579135382177771163014768'), 'PevolParenU[1]': mpc(real='-0.087517094413118015627794932243', imag='-0.0838494759844927717296059199725'), 'PevolParenU[2]': mpc(real='-0.235728967783171816652298957706', imag='0.405016702547488505192774255192'), 'psi6Phi_rhs': mpf('-1.22513083961622711186385532584'), 'SevolParenUD[0][0]': mpc(real='0.0', imag='-0.00760121582906386067390869243354'), 'SevolParenUD[0][1]': mpc(real='0.0', imag='-0.0146266612839660806871799891837'), 'SevolParenUD[0][2]': mpc(real='0.0', imag='-0.0605117492091906752915697609296'), 'SevolParenUD[1][0]': mpc(real='0.0', imag='-0.0376753508322823713050375715738'), 'SevolParenUD[1][1]': mpc(real='0.0', imag='0.0165469600498312913172682669938'), 'SevolParenUD[1][2]': mpc(real='0.0', imag='-0.0598102194516057436568523542064'), 'SevolParenUD[2][0]': mpc(real='0.0', imag='-0.00274446628741218355551634289213'), 'SevolParenUD[2][1]': mpc(real='0.0', imag='-0.00210480864586638912946958690497'), 'SevolParenUD[2][2]': mpc(real='0.0', imag='0.0255254872925272935368923299393'), 'Stilde_rhsD[0]': mpc(real='-2.05669044585248350642814330058', imag='0.0505860239115470053383738502362'), 'Stilde_rhsD[1]': mpc(real='-1.39929177474189447849539646995', imag='-0.0595283716889681291384306405234'), 'Stilde_rhsD[2]': mpc(real='-0.562245303441695765123142791708', imag='-0.00594943635350156634772345043416')}
