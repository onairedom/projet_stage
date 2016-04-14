#!/usr/bin/python3
from prog15 import tableau
import time
import datetime
import random
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import pylab as plt

lst=tableau()

M=""
j=0
# print("Le tableau est composé de", len(lst),"lignes et dispose donc de",(len(lst)*9),"élément")

# print("Si vous êtes intéressé par info1 tapez i")
# print("OL1 tapez O")
# print("Ma1 tapez M")
# print("Au3 Tapez A")


# Demande=input("Quel cours avez vous choisis?")
# switcher ={
# 	'A' or 'a': 
# }
M='Info1'
N='Ma1'
O='Au3'
P='DS'
L='Eval Wims'
Q='AM2'
R='SOUTENANCE'



# print(lst)
# j=0;i=0;k=0;
# nb=[]
# cours=[]

# for i in range(len(lst)):
# 	nb.append([0]);
# 	cours.append([])

# for cpt in lst:
# 	test=cpt[0]
# 	cours[k]=test;
# 	k+=1;
# print("first",cours[0])
# test=cours[0]
# print(len(cours))
# print(cours)
# k=0

# indices=[i for i,x in enumerate(cours) if x==test]
# print (indices)


# i=0
# for i in range(j):
# 	print(cours[i])


k=0;Heure=0;Min=0
recap=[];time=[];time2=[];time3=[];time4=[]
semaine=[];
j=0
var=""
for i in lst:	# Parcours grand tableau
	if lst[k][0] not in recap: #récupère élément tableau
		recap.append(lst[k][0]) #ajoute élément dans petit tableau
	k+=1
m=0
for j in recap:
	if j=='SOUTENANCE':
		recap[m]='STCE'
		
	elif j=='Eval Wims':
		recap[m]='EW'
		
	m+=1;



t2=datetime.timedelta(0,(0+0))
t=datetime.timedelta(0,(0+0))
t4=0;t5=0
for i in recap: #tableau liste matière
	t2=datetime.timedelta(0,(0+0))
	for e in lst: #prend chaque ligne grand tableau
		for j in e:  #Récup info dans chaque ligne
			if i==j:  #Compare grand tableau et list matière
				k=0;
					 #Récupère durée d'un cours
				Hour=','.join(e[6])  #Sépare  heure pour créer Heure avec datetime
				H=Hour[0]
				if Hour[2].isnumeric()==True:
					H=Hour[0]+Hour[2]
				if Hour[6].isnumeric()==True and Hour[4].isnumeric()==True:
					M=Hour[4]+Hour[6]
				else:
					M=Hour[6]+Hour[8]
				H=int(H)
				M=int(M)

				t1=datetime.timedelta(0,(3600*H+60*M))
				t2=t1+t2
				if e[1]==1:	#Permet d'augmenter heure faite en fonction type de séance cours,td,tp...
					t=t+t1*1.5
				else:
					t=t+t1
				
				t5=t.total_seconds()
				t3=t1.total_seconds()
				t4=int(t3+t4)
	time4.append(t5)	#Création de tableau qui garde la durée en seconds en tenant compte coeff
	time3.append(t4)	#Création de tableau qui garde la durée en seconds sans coeff
	time2.append([str(t)])	#Création de tableau qui garde la durée en jours et heures avec datetime avec coeff
	time.append([str(t2)])	#Création de tableau qui garde la durée en jours et heures avec datetime sans coeff
# print(time)
# print(time2)
# print (time3) #seconde sans coeff
# print (time4)	#seconde coeff
"""
nb_heure=[];matiere=[];x=[]
k=0;
for i in time4:
	p=(i/3600)
	nb_heure.append(p)

for j in recap:
	x.append(k)
	k=k+1
	matiere.append(j)

plt.bar(x, nb_heure, align='center', edgecolor = 'red', hatch = '/')  # ces deux lignes permettent de mettre des string dans un histogrammes plutot que des entiers
plt.xticks(x, matiere) # x est une liste composé du nombre d'éléments qe l'on veut mettre en horizontal
plt.grid(True) # celà sert à mettre une grille dans le diagramme
plt.xlabel('Matières') 
plt.ylabel(u"Nombre d'heures")
plt.title("Nombre d'heures par matière sur l'année")
plt.text(600,500,'STCE=SOUTENANCE EW=Eval Wims')# a travailler
plt.show()

"""
###########################################création tableau pour toutes les semaines####################################################
Sem=[]
k=0
longueur=len(recap) #pr créer un tableau ayant la semaine suivi de chaque matière elle même suivi du nombre d'heure par semaine
l=longueur*2 # on mutliplie la longueur par 2 a cause du nombre d'heure qui apparait derrière le tableau
for i in lst:
	if lst[k][7] not in Sem:
		Sem.append(lst[k][7])
	k+=1
nb=len(Sem)

Semaine=[]
for i in range(l*nb):
	Semaine.append([]);



# k=0
# m=0
# if k%(l+1)==0:		# Dans l'exemple on insère le nom de la semaine modulo nb de matière *2+1
# 	for j in Sem:
# 		if j not in Semaine:   #vérifie si la semaine existe dans le tableau existe et laisse place pour les matières et heures
# 			Semaine[k]=j
# if  k%2==0 and k!=0:	#Tous les nb pair du tableau correspondront aux matières
# 	for n in recap: # parcours tableau matière
# 		Semaine[k]=n
# if  k%3==0 and k!=0: # Tous les modulos de 3 correspondront aux nombres de seconde par matières de chaque semaines
# 	for m in time4:
# 		Semaine[k]=m
	
# k+=1


#Améliorer ça et le faire dans le grand tableau lst pour que cela marche
k=0;j=0;
for i in lst:
	Semaine[k]=lst[j][7]
	S=Semaine[k]
	for S in lst:
		j+=1
		k+=1
		Semaine[k]=lst[j][0]
		k+=1
		Semaine[k]=lst[j][6]
		k+=1
	j+=1



