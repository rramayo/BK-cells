#-*- coding: utf-8 -*-

# library
from random import random,choice,randint,uniform
from math import pi
from time import localtime
#
# Function Potencial
def U(Person_pos,bar_right,bar_left):
	X = int(Person_pos/10.0)
	Xb1 = int(bar_left/10.0)
	Xb2 = int(bar_right/10.0)
	Tp = 0.0
	U_Tp = [0.0,1.0,0.0]
	K = 1.5
	A = 0.2
	B = (U_Tp[1]-U_Tp[0])/(Tp-(Tp-K))
	U_Xb1 = U_Tp[0]-A*(Tp-K-Xb1)
	if X >= Xb1 and X <= Tp-K:
		return (X-Xb1)*A+U_Xb1
	elif X >= Tp-K and X <= Tp:
		return (X-(Tp-K))*(B)+U_Tp[0]
	elif X >= Tp and X <= Tp+K:
		return (X-Tp)*(-B)+U_Tp[1]
	elif X >= Tp+K and X <= Xb2:
		return (X-(Tp+K))*A+U_Tp[2]
#
# Method
bar_init_locate = choice(range(20,140,10))
person_init = choice([-1,1])*choice(range(10,bar_init_locate,10))
#Arquivos
localtime = [
	localtime()[0], localtime()[1],
	localtime()[2], localtime()[3],
	localtime()[4]
]
arq1 = open(
	"{}_{}_{}_{}_{}_arq_Ta_Xm_{}_Xb_{}_X_{}.dat".format(
		localtime[4], localtime[3], localtime[2], localtime[1], localtime[0],
		14, int(bar_init_locate/10.0), int(person_init/10.0)
	),
	"a"
)
arq2 = open(
	"{}_{}_{}_{}_{}_arq_Tf_Xm_{}_Xb_{}_X_{}.dat".format(
		localtime[4], localtime[3], localtime[2], localtime[1], localtime[0],
		14, int(bar_init_locate/10.0), int(person_init/10.0)
	),
	"a"
)
arq3 = open(
	"{}_{}_{}_{}_{}_arq_Tf_Ta_Xm_{}_Xb_{}_X_{}.dat".format(
		localtime[4], localtime[3], localtime[2], localtime[1], localtime[0],
		14, int(bar_init_locate/10.0), int(person_init/10.0)
	),
	"a"
)
arq4 = open(
	"{}_{}_{}_{}_{}_arq_X_Xm_{}_Xb_{}_X_{}.dat".format(
		localtime[4], localtime[3], localtime[2], localtime[1], localtime[0],
		14, int(bar_init_locate/10.0), int(person_init/10.0)
	),
	"a"
)
arq5 = open(
	"{}_{}_{}_{}_{}_p_Delta_U.dat".format(
		localtime[4],localtime[3],localtime[2],localtime[1], localtime[0]
	),
	"a"
)
#
N = 1000
Tf = 0
Ta = 0
cont = 0
for run in xrange(N):
	steps = 600
	person_init = person_init
	person = person_init
	bar_Fix = bar_init_locate
	while run != 0:
		bar_init_locate = choice([int(bar_init_locate)-10, int(bar_init_locate)+10])
		if abs(bar_init_locate) not in [0,10,abs(person_init),140]:
			break
		else:
			bar_init_locate = bar_Fix
			break
	bar_left = -bar_init_locate
	bar_right = bar_init_locate
	vec_x = [person_init/140.0]
	if run == 0:
		Delta_U = U(person+10.0,bar_right,bar_left)-(U(person-10.0,bar_right,bar_left))
		p = 1.0/2.0 - (1.0/4.0)*Delta_U
		arq5.write("%s\t%s\n" %(p,Delta_U))
	for step in xrange(steps):
		if random() <= p:
			walk_x = int(person)+10
			bar_x = int(bar_right)
			if walk_x > bar_x:
				person = int(person)
				walk_x = int(person)
			elif walk_x < bar_x:
				person = walk_x
			if int(person) > 0:
				if Ta != 0:
					arq2.write('%s\n' %(Ta))
					arq3.write('Tf\t%s\n' %(Ta))
					Ta = 0
				Tf += 1
			elif int(person) < 0:
				if Tf != 0:
					arq1.write('%s\n' %(Tf))
					arq3.write('Ta\t%s\n' %(Tf))
					Tf = 0
				Ta += 1
		else:
			walk_x = int(person)-10
			bar_x = int(bar_left)
			if walk_x < bar_x:
				person = int(person)
				walk_x = int(person)
			elif walk_x > bar_x:
				person = walk_x
			if int(person) > 0:
				if Ta != 0:
					arq2.write('%s\n' %(Ta))
					arq3.write('Tf\t%s\n' %(Ta))
					Ta = 0
				Tf += 1
			elif int(person) < 0:
				if Tf != 0:
					arq1.write('%s\n' %(Tf))
					arq3.write('Ta\t%s\n' %(Tf))
					Tf = 0
				Ta += 1
		Delta_U = U(person+10.0,bar_right,bar_left)-(U(person-10.0,bar_right,bar_left))
		p = 1.0/2.0 - (1.0/4.0)*Delta_U
		vec_x.append(int(walk_x/10.0)/14.0)
		cont+=1
		arq4.write('%s\t%s\n' %(cont,vec_x[step]))
		arq5.write("%s\t%s\n" %(p,Delta_U))
else:
	if Ta != 0:
		arq2.write('%s\n' %(Ta))
		arq3.write('Tf\t%s\n' %(Ta))
		Ta = 0
	if Tf != 0:
		arq1.write('%s\n' %(Tf))
		arq3.write('Ta\t%s\n' %(Tf))
		Tf = 0
	arq1.close()
	arq2.close()
	arq3.close()
	arq4.close()
	arq5.close()
#
