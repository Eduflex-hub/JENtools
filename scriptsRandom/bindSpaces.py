import maya.cmds as mc
#############
#VARS:
#############
hipParent='C_hipSpaceFollow_01_NULL'
chestParent='C_chestSpaceFollow_01_NULL'
leftShoulderParent='L_shoulderSpaceFollow_01_NULL'
rigthShoulderParent='R_shoulderSpaceFollow_01_NULL'
headParent='C_headSpaceFollow_01_NULL'
worldParent='C_mainSpaceFollow_01_NULL'

#---------------------------

leftIkArmChild='L_ikArmSpaceFollow_01_NULL'
rigthIkArmChild='R_ikArmSpaceFollow_01_NULL'

leftIkLegChild='L_ikfootSpaceFollow_01_NULL'
rigthIkLegChild='R_ikfootSpaceFollow_01_NULL'

leftFkArmChild='L_fkArmSpaceFollow_01_NULL'
rigthFkArmChild='R_fkArmSpaceFollow_01_NULL'

leftFkLegChild='L_fkfootSpaceFollow_01_NULL'
rigthFkLegChild='R_fkfootSpaceFollow_01_NULL'

#-----------------------------------------

leftArmSwitch='L_lowerArm_02_endswitchCTRL'
rigthArmSwitch='R_lowerArm_02_endswitchCTRL'

leftLegSwitch='L_lowerLeg_02_endswitchCTRL'
rigthLegSwitch='R_lowerLeg_02_endswitchCTRL'


#############
#ARM:
#############

lIkArm=mc.parentConstraint( hipParent, chestParent, leftShoulderParent, headParent, leftIkArmChild, mo=1)[0]

rIkArm=mc.parentConstraint( hipParent,  chestParent, rigthShoulderParent, headParent, rigthIkArmChild, mo=1)[0]

lFkArm=mc.orientConstraint( chestParent,  hipParent, worldParent, leftFkArmChild, mo=1)[0]

rFkArm=mc.orientConstraint( chestParent,  hipParent, worldParent, rigthFkArmChild, mo=1)[0]

#############
#LEG:
#############

lIkLeg=mc.parentConstraint( hipParent, leftIkLegChild, mo=1)[0]

rIkLeg=mc.parentConstraint( hipParent, rigthIkLegChild, mo=1)[0]

lFkFoot=mc.orientConstraint( worldParent, leftFkLegChild, mo=1)[0]

rFkFoot=mc.orientConstraint( worldParent, rigthFkLegChild, mo=1)[0]

#############
#BIND:
#############
#leftArm:
print lIkArm
print hipParent
print leftArmSwitch


mc.setDrivenKeyframe(lIkArm+'.'+hipParent+'W0', cd=leftArmSwitch+".ikSpace", dv=0, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+chestParent+'W1', cd=leftArmSwitch+".ikSpace", dv=0, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+leftShoulderParent+'W2', cd=leftArmSwitch+".ikSpace", dv=0, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+headParent+'W3', cd=leftArmSwitch+".ikSpace", dv=0, v=0)

mc.setDrivenKeyframe(lIkArm+'.'+hipParent+'W0', cd=leftArmSwitch+".ikSpace", dv=1, v=1)
mc.setDrivenKeyframe(lIkArm+'.'+chestParent+'W1', cd=leftArmSwitch+".ikSpace", dv=1, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+leftShoulderParent+'W2', cd=leftArmSwitch+".ikSpace", dv=1, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+headParent+'W3', cd=leftArmSwitch+".ikSpace", dv=1, v=0)

mc.setDrivenKeyframe(lIkArm+'.'+hipParent+'W0', cd=leftArmSwitch+".ikSpace", dv=2, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+chestParent+'W1', cd=leftArmSwitch+".ikSpace", dv=2, v=1)
mc.setDrivenKeyframe(lIkArm+'.'+leftShoulderParent+'W2', cd=leftArmSwitch+".ikSpace", dv=2, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+headParent+'W3', cd=leftArmSwitch+".ikSpace", dv=2, v=0)

mc.setDrivenKeyframe(lIkArm+'.'+hipParent+'W0', cd=leftArmSwitch+".ikSpace", dv=3, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+chestParent+'W1', cd=leftArmSwitch+".ikSpace", dv=3, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+leftShoulderParent+'W2', cd=leftArmSwitch+".ikSpace", dv=3, v=1)
mc.setDrivenKeyframe(lIkArm+'.'+headParent+'W3', cd=leftArmSwitch+".ikSpace", dv=3, v=0)

mc.setDrivenKeyframe(lIkArm+'.'+hipParent+'W0', cd=leftArmSwitch+".ikSpace", dv=4, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+chestParent+'W1', cd=leftArmSwitch+".ikSpace", dv=4, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+leftShoulderParent+'W2', cd=leftArmSwitch+".ikSpace", dv=4, v=0)
mc.setDrivenKeyframe(lIkArm+'.'+headParent+'W3', cd=leftArmSwitch+".ikSpace", dv=4, v=1)


mc.setDrivenKeyframe(lFkArm+'.'+chestParent+'W0', cd=leftArmSwitch+".fkSpace", dv=0, v=0)
mc.setDrivenKeyframe(lFkArm+'.'+hipParent+'W1', cd=leftArmSwitch+".fkSpace", dv=0, v=0)
mc.setDrivenKeyframe(lFkArm+'.'+worldParent+'W2', cd=leftArmSwitch+".fkSpace", dv=0, v=0)

mc.setDrivenKeyframe(lFkArm+'.'+chestParent+'W0', cd=leftArmSwitch+".fkSpace", dv=1, v=1)
mc.setDrivenKeyframe(lFkArm+'.'+hipParent+'W1', cd=leftArmSwitch+".fkSpace", dv=1, v=0)
mc.setDrivenKeyframe(lFkArm+'.'+worldParent+'W2', cd=leftArmSwitch+".fkSpace", dv=1, v=0)

mc.setDrivenKeyframe(lFkArm+'.'+chestParent+'W0', cd=leftArmSwitch+".fkSpace", dv=2, v=0)
mc.setDrivenKeyframe(lFkArm+'.'+hipParent+'W1', cd=leftArmSwitch+".fkSpace", dv=2, v=1)
mc.setDrivenKeyframe(lFkArm+'.'+worldParent+'W2', cd=leftArmSwitch+".fkSpace", dv=2, v=0)

mc.setDrivenKeyframe(lFkArm+'.'+chestParent+'W0', cd=leftArmSwitch+".fkSpace", dv=3, v=0)
mc.setDrivenKeyframe(lFkArm+'.'+hipParent+'W1', cd=leftArmSwitch+".fkSpace", dv=3, v=0)
mc.setDrivenKeyframe(lFkArm+'.'+worldParent+'W2', cd=leftArmSwitch+".fkSpace", dv=3, v=1)



#rigthArm:

mc.setDrivenKeyframe(rIkArm+'.'+hipParent+'W0', cd=rigthArmSwitch+".ikSpace", dv=0, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+chestParent+'W1', cd=rigthArmSwitch+".ikSpace", dv=0, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+rigthShoulderParent+'W2', cd=rigthArmSwitch+".ikSpace", dv=0, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+headParent+'W3', cd=rigthArmSwitch+".ikSpace", dv=0, v=0)

mc.setDrivenKeyframe(rIkArm+'.'+hipParent+'W0', cd=rigthArmSwitch+".ikSpace", dv=1, v=1)
mc.setDrivenKeyframe(rIkArm+'.'+chestParent+'W1', cd=rigthArmSwitch+".ikSpace", dv=1, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+rigthShoulderParent+'W2', cd=rigthArmSwitch+".ikSpace", dv=1, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+headParent+'W3', cd=rigthArmSwitch+".ikSpace", dv=1, v=0)

mc.setDrivenKeyframe(rIkArm+'.'+hipParent+'W0', cd=rigthArmSwitch+".ikSpace", dv=2, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+chestParent+'W1', cd=rigthArmSwitch+".ikSpace", dv=2, v=1)
mc.setDrivenKeyframe(rIkArm+'.'+rigthShoulderParent+'W2', cd=rigthArmSwitch+".ikSpace", dv=2, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+headParent+'W3', cd=rigthArmSwitch+".ikSpace", dv=2, v=0)

mc.setDrivenKeyframe(rIkArm+'.'+hipParent+'W0', cd=rigthArmSwitch+".ikSpace", dv=3, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+chestParent+'W1', cd=rigthArmSwitch+".ikSpace", dv=3, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+rigthShoulderParent+'W2', cd=rigthArmSwitch+".ikSpace", dv=3, v=1)
mc.setDrivenKeyframe(rIkArm+'.'+headParent+'W3', cd=rigthArmSwitch+".ikSpace", dv=3, v=0)

mc.setDrivenKeyframe(rIkArm+'.'+hipParent+'W0', cd=rigthArmSwitch+".ikSpace", dv=4, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+chestParent+'W1', cd=rigthArmSwitch+".ikSpace", dv=4, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+rigthShoulderParent+'W2', cd=rigthArmSwitch+".ikSpace", dv=4, v=0)
mc.setDrivenKeyframe(rIkArm+'.'+headParent+'W3', cd=rigthArmSwitch+".ikSpace", dv=4, v=1)


mc.setDrivenKeyframe(rFkArm+'.'+chestParent+'W0', cd=rigthArmSwitch+".fkSpace", dv=0, v=0)
mc.setDrivenKeyframe(rFkArm+'.'+hipParent+'W1', cd=rigthArmSwitch+".fkSpace", dv=0, v=0)
mc.setDrivenKeyframe(rFkArm+'.'+worldParent+'W2', cd=rigthArmSwitch+".fkSpace", dv=0, v=0)

mc.setDrivenKeyframe(rFkArm+'.'+chestParent+'W0', cd=rigthArmSwitch+".fkSpace", dv=1, v=1)
mc.setDrivenKeyframe(rFkArm+'.'+hipParent+'W1', cd=rigthArmSwitch+".fkSpace", dv=1, v=0)
mc.setDrivenKeyframe(rFkArm+'.'+worldParent+'W2', cd=rigthArmSwitch+".fkSpace", dv=1, v=0)

mc.setDrivenKeyframe(rFkArm+'.'+chestParent+'W0', cd=rigthArmSwitch+".fkSpace", dv=2, v=0)
mc.setDrivenKeyframe(rFkArm+'.'+hipParent+'W1', cd=rigthArmSwitch+".fkSpace", dv=2, v=1)
mc.setDrivenKeyframe(rFkArm+'.'+worldParent+'W2', cd=rigthArmSwitch+".fkSpace", dv=2, v=0)

mc.setDrivenKeyframe(rFkArm+'.'+chestParent+'W0', cd=rigthArmSwitch+".fkSpace", dv=3, v=0)
mc.setDrivenKeyframe(rFkArm+'.'+hipParent+'W1', cd=rigthArmSwitch+".fkSpace", dv=3, v=0)
mc.setDrivenKeyframe(rFkArm+'.'+worldParent+'W2', cd=rigthArmSwitch+".fkSpace", dv=3, v=1)


#leftLeg:

mc.setDrivenKeyframe(lIkLeg+'.'+hipParent+'W0', cd=leftLegSwitch+".ikSpace", dv=0, v=0)

mc.setDrivenKeyframe(lIkLeg+'.'+hipParent+'W0', cd=leftLegSwitch+".ikSpace", dv=1, v=1)


mc.setDrivenKeyframe(lFkFoot+'.'+worldParent+'W0', cd=leftLegSwitch+".fkSpace", dv=0, v=0)

mc.setDrivenKeyframe(lFkFoot+'.'+worldParent+'W0', cd=leftLegSwitch+".fkSpace", dv=1, v=1)


#rigthLeg:

mc.setDrivenKeyframe(rIkLeg+'.'+hipParent+'W0', cd=rigthLegSwitch+".ikSpace", dv=0, v=0)

mc.setDrivenKeyframe(rIkLeg+'.'+hipParent+'W0', cd=rigthLegSwitch+".ikSpace", dv=1, v=1)


mc.setDrivenKeyframe(rFkFoot+'.'+worldParent+'W0', cd=rigthLegSwitch+".fkSpace", dv=0, v=0)

mc.setDrivenKeyframe(rFkFoot+'.'+worldParent+'W0', cd=rigthLegSwitch+".fkSpace", dv=1, v=1)


###########################
#Binding IK and FK switches:
###########################

contL_FKArm='L_upperArm_01_fkZTR'
contR_FKArm='R_upperArm_01_fkZTR'

contL_IKArm=['L_hand_01_ikZTR','L_upperArm_01_PoleVector_ikCTRL_GRP']
contR_IKArm=['R_hand_01_ikZTR','R_upperArm_01_PoleVector_ikCTRL_GRP']


contL_FKLeg='L_upperLeg_01_fkZTR'
contR_FKLeg='R_upperLeg_01_fkZTR'

contL_IKLeg=['L_foot_01_ikZTR','L_upperLeg_01_PoleVector_ikCTRL_GRP']
contR_IKLeg=['R_foot_01_ikZTR','R_upperLeg_01_PoleVector_ikCTRL_GRP']




#arm:
mc.setDrivenKeyframe(contL_FKArm+'.v', cd=leftArmSwitch+".IK_FK", dv=0, v=0)
mc.setDrivenKeyframe(contL_FKArm+'.v', cd=leftArmSwitch+".IK_FK", dv=1, v=1)

mc.setDrivenKeyframe(contR_FKArm+'.v', cd=rigthArmSwitch+".IK_FK", dv=0, v=0)
mc.setDrivenKeyframe(contR_FKArm+'.v', cd=rigthArmSwitch+".IK_FK", dv=1, v=1)


for i in contL_IKArm:

	mc.setDrivenKeyframe(i+'.v', cd=leftArmSwitch+".IK_FK", dv=0, v=1)
	mc.setDrivenKeyframe(i+'.v', cd=leftArmSwitch+".IK_FK", dv=1, v=0)

for i in contR_IKArm:

	mc.setDrivenKeyframe(i+'.v', cd=rigthArmSwitch+".IK_FK", dv=0, v=1)
	mc.setDrivenKeyframe(i+'.v', cd=rigthArmSwitch+".IK_FK", dv=1, v=0)

#leg:

mc.setDrivenKeyframe(contL_FKLeg+'.v', cd=leftLegSwitch+".IK_FK", dv=0, v=0)
mc.setDrivenKeyframe(contL_FKLeg+'.v', cd=leftLegSwitch+".IK_FK", dv=1, v=1)

mc.setDrivenKeyframe(contR_FKLeg+'.v', cd=rigthLegSwitch+".IK_FK", dv=0, v=0)
mc.setDrivenKeyframe(contR_FKLeg+'.v', cd=rigthLegSwitch+".IK_FK", dv=1, v=1)


for i in contL_IKLeg:

	mc.setDrivenKeyframe(i+'.v', cd=leftLegSwitch+".IK_FK", dv=0, v=1)
	mc.setDrivenKeyframe(i+'.v', cd=leftLegSwitch+".IK_FK", dv=1, v=0)

for i in contR_IKLeg:

	mc.setDrivenKeyframe(i+'.v', cd=rigthLegSwitch+".IK_FK", dv=0, v=1)
	mc.setDrivenKeyframe(i+'.v', cd=rigthLegSwitch+".IK_FK", dv=1, v=0)






