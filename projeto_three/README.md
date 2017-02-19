# Projeto agatha_three

# Função do Potencial
  - U_Xb1 = constante

## Code: agatha_three.py

# Library
```python
#-*- coding: utf-8 -*-
# library
from turtle import *
import pylab as plt
from random import random,choice,randint,uniform
from math import pi
from time import localtime
#
```

# Window
```python
# Window
window = Screen()
window.title("The walk person")
window.screensize(250,100)
window.setup(300,150,0,0)
frequence = 2e+5
window.delay(1.0/frequence)
#
```

# Person
```python
# Person
person = Turtle()
person.penup()
person.shape("circle")
person.shapesize(0.3,0.3)
person.color("black","red")
#
```

# Block Center
```python
# Block Center
block_center = Turtle()
block_center.penup()
block_center.shape("square")
block_center.shapesize(1.0,0.01)
block_center.color("red")
block_center.goto(0,0)
#
```

# Block right
```python
# Block right
block_right = Turtle()
block_right.penup()
block_right.shape("square")
block_right.shapesize(1.0,0.01)
block_right.color("green")
block_right.goto(140,0)
#
```
# Block left
```python
# Block left
block_left = Turtle()
block_left.penup()
block_left.shape("square")
block_left.shapesize(1.0,0.01)
block_left.color("green")
block_left.goto(-140,0)
#
```

# Move bar right
```python
# move bar right
bar_right = Turtle()
bar_right.penup()
bar_right.shape("square")
bar_right.shapesize(1.0,0.01)
bar_right.color("blue")
#
```

# Move bar left
```python
# move bar left
bar_left = Turtle()
bar_left.penup()
bar_left.shape("square")
bar_left.shapesize(1.0,0.01)
bar_left.color("blue")
#
```

# Function Potencial
```python
# Function Potencial
def U(Person_pos,bar_right,bar_left):
	X = int(Person_pos/10.0)
	Xb1 = int(bar_left/10.0)
	Xb2 = int(bar_right/10.0)
	Tp = 0.0
	U_Tp = [0.0,1.0,0.0]
	K = 1.5
	B = (U_Tp[1]-U_Tp[0])/(Tp-(Tp-K))
	U_Xb1 = 1.0
	A = (U_Tp[0]-U_Xb1)/(Tp-K-Xb1)
	if X >= Xb1 and X <= Tp-K:
		return (X-Xb1)*A+U_Xb1
	elif X >= Tp-K and X <= Tp:
		return (X-(Tp-K))*(B)+U_Tp[0]
	elif X >= Tp and X <= Tp+K:
		return (X-Tp)*(-B)+U_Tp[1]
	elif X >= Tp+K and X <= Xb2:
		return (X-(Tp+K))*A+U_Tp[2]
#
```

# Aplicando o Método
```python
# Method
bar_init_locate = choice(range(20,140,10))
person_init = choice([-1,1])*choice(range(10,bar_init_locate,10))
person.goto(person_init,0)
#Arquivos
arq1 = open("%s_%s_%s_%s_%s_arq_Ta_Xm_%s_Xb_%s_X_%s.dat" \
			%(localtime()[0],localtime()[1],localtime()[2],localtime()[3],\
			localtime()[4],14,int(bar_init_locate/10.0),int(person_init/10.0)), "a")
arq2 = open("%s_%s_%s_%s_%s_arq_Tf_Xm_%s_Xb_%s_X_%s.dat" \
			%(localtime()[0],localtime()[1],localtime()[2],localtime()[3],\
			localtime()[4],14,int(bar_init_locate/10.0),int(person_init/10.0)), "a")
arq3 = open("%s_%s_%s_%s_%s_arq_Tf_Ta_Xm_%s_Xb_%s_X_%s.dat" \
			%(localtime()[0],localtime()[1],localtime()[2],localtime()[3],\
			localtime()[4],14,int(bar_init_locate/10.0),int(person_init/10.0)), "a")
arq4 = open("%s_%s_%s_%s_%s_arq_X_Xm_%s_Xb_%s_X_%s.dat" \
			%(localtime()[0],localtime()[1],localtime()[2],localtime()[3],\
			localtime()[4],14,int(bar_init_locate/10.0),int(person_init/10.0)), "a")
arq5 = open("p_Delta_U.dat","a")
#
N = 1000
Tf = 0
Ta = 0
cont = 0
for run in xrange(N):
	steps = 600
	person_init = int(person.pos()[0])
	bar_Fix = bar_init_locate
	while run != 0:
		print "Entrou {0}".format(run)
		bar_init_locate = choice([int(bar_init_locate)-10, int(bar_init_locate)+10])
		if abs(bar_init_locate) not in [0,10,abs(person_init),140]:
			print "Saiu bar_locate {0}".format(run)
			break
		else:
			bar_init_locate = bar_Fix
			print "Saiu bar_fix {0}".format(run)
			break
	bar_left.goto(-bar_init_locate,0)
	bar_right.goto(bar_init_locate,0)
	vec_x = [person_init/140.0]
	if run == 0:
		Delta_U = U(person.pos()[0]+10.0,bar_right.pos()[0],bar_left.pos()[0])-(U(person.pos()[0]-10.0,bar_right.pos()[0],bar_left.pos()[0]))
		print "U+10: {0:.2f}".format(U(person.pos()[0]+10.0,bar_right.pos()[0],bar_left.pos()[0])), "U-10: {0:.2f}".format(U(person.pos()[0]-10.0,bar_right.pos()[0],bar_left.pos()[0]))
		print "Delta_U_init: {0:.2f}".format(Delta_U)
		p = 1.0/2.0 - (1.0/4.0)*Delta_U
		print "p_init: {0:.2f}".format(p)
		arq5.write("%s\t%s\n" %(p,Delta_U))
	for step in xrange(steps):
		if random() <= p:
			walk_x = int(person.pos()[0])+10
			bar_x = int(bar_right.pos()[0])
			if walk_x > bar_x:
				person.goto(int(person.pos()[0]),0)
				walk_x = int(person.pos()[0])
			elif walk_x < bar_x:
				person.goto(walk_x,0)
			if int(person.pos()[0]) > 0:
				if Ta != 0:
					arq2.write('%s\n' %(Ta))
					arq3.write('Tf\t%s\n' %(Ta))
					Ta = 0
				Tf += 1
			elif int(person.pos()[0]) < 0:
				if Tf != 0:
					arq1.write('%s\n' %(Tf))
					arq3.write('Ta\t%s\n' %(Tf))
					Tf = 0
				Ta += 1
		else:
			walk_x = int(person.pos()[0])-10
			bar_x = int(bar_left.pos()[0])
			if walk_x < bar_x:
				person.goto(int(person.pos()[0]),0)
				walk_x = int(person.pos()[0])
			elif walk_x > bar_x:
				person.goto(walk_x,0)
			if int(person.pos()[0]) > 0:
				if Ta != 0:
					arq2.write('%s\n' %(Ta))
					arq3.write('Tf\t%s\n' %(Ta))
					Ta = 0
				Tf += 1
			elif int(person.pos()[0]) < 0:
				if Tf != 0:
					arq1.write('%s\n' %(Tf))
					arq3.write('Ta\t%s\n' %(Tf))
					Tf = 0
				Ta += 1
		Delta_U = U(person.pos()[0]+10.0,bar_right.pos()[0],bar_left.pos()[0])-(U(person.pos()[0]-10.0,bar_right.pos()[0],bar_left.pos()[0]))
		print "U+10: {0:.2f}".format(U(person.pos()[0]+10.0,bar_right.pos()[0],bar_left.pos()[0])), "U-10: {0:.2f}".format(U(person.pos()[0]-10.0,bar_right.pos()[0],bar_left.pos()[0]))
		print "Delta_U: {0:.2f}".format(Delta_U)
		print "p_old: {0:.2f}".format(p),
		p = 1.0/2.0 - (1.0/4.0)*Delta_U
		print "p_new: {0:.2f}".format(p)
		vec_x += [int(walk_x/10)/14.0]
		cont+=1
		arq4.write('%s\t%s\n' %(cont,vec_x[step]))
		arq5.write("%s\t%s\n" %(p,Delta_U))
		plt.ion()
		plt.clf()
		plt.plot(vec_x,"-b")
		plt.plot(vec_x,".r")
		plt.draw()
else:
	if Ta != 0:
		arq2.write('%s\n' %(Ta))
		arq3.write('Tf\t%s\n' %(Ta))
		Ta = 0
	if Tf != 0:
		arq1.write('%s\n' %(Tf))
		arq3.write('Ta\t%s\n' %(Tf))
		Tf = 0
	print
	print "-----------------"
	print "-Fim do Programa-"
	print "-----------------"
	print
	arq1.close()
	arq2.close()
	arq3.close()
	arq4.close()
	arq5.close()
	plt.ioff()
	plt.show()
#
```
