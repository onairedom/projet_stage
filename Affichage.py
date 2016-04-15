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

l=53 # on créé une variable qui rpz le nb de semaine plus 1pour le nombre de matière

Semaine=[]
for i in range(l):
	Semaine.append([]);


Semaine[0].append(0)
for i in recap:	# On créé le nb de colonnes qui correspondent au nombre de matière plus 1
	Semaine[0].append(i)

nb_mat=len(recap)
k=0;
for j in Semaine:		#On créé le nombre des semaines dans la colonne 0 du tableau
	if k>0:
		Semaine[k].append(k)
		for m in range(nb_mat):		#On ajoute les colonnes vide à chaque ligne
			Semaine[k].append([])
	k+=1

print(Semaine[0])
for j in lst:		#On va chercher le nombre d'heure par matière par semaine pour compléter ce nouveau tableau
	s=j[7]
	m=j[0]
	Hour=','.join(j[6])  #Sépare  heure pour créer Heure avec datetime
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
	time=t1.total_seconds()
	time2=time/3600
	if m=='STCE':
		m='SOUTENANCE'
	elif m=='EW':
		m='Eval Wims'
	if m in Semaine[0]:
		index=Semaine[0].index(m)
	Semaine[s][index]=time2


###############################################création 2ème histogramme pour nb heure matière sur toute l'année

for i in range(nb_mat): #car on commence a 0 et pour faire correspondre les numéros de matières avec les heures
	 globals()['y%s' % i] = [] # créé des tableau avec des noms comportznt un chiffre de 0 à nb de matière

	

nb_heure=[];matiere=[];x=[];
m=0;n=0;k=0;
for i in Semaine: #Parcours tableau semaine
	for j in i:	#parcours chaque ligne avec nombre d'heure ont le meme indice que dans le tableau recap des matière
		if m==8:
			m=0;
		if type(j)==float :
			globals()['y%s' % m].append(j) # utilise tableau ayant des noms de 0 à nb_matière et ajoute le nombre d'heure a l'intérieur
		m+=1;	
			
print("c'est moi",recap)
print(y0)
print(y1)
print(y2)
print(y3)
print(y4)
print(y6)
print(y7)

for j in Semaine:
	x.append(k)
	
	k=k+1
	
print(x)



plt.hist([for i in range(nb_mat):globals()['y%s' % i],], range = (1, len(x)), bins = len(x), color = ['yellow','green','blue','orange'],
            edgecolor = 'red',histtype = 'barstacked',align='left')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Exemple d\' histogramme simple')
plt.show()

"""
plt.bar(x, nb_heure, align='center', edgecolor = 'red', hatch = '/')  # ces deux lignes permettent de mettre des string dans un histogrammes plutot que des entiers
# plt.xticks(x, matiere) # x est une liste composé du nombre d'éléments qe l'on veut mettre en horizontal
plt.grid(True) # celà sert à mettre une grille dans le diagramme
plt.xlabel('Semaines') 
plt.ylabel(u"Nombre d'heures")
plt.title("Nombre d'heures par matière sur l'année")
plt.text(600,500,'STCE=SOUTENANCE EW=Eval Wims')# a travailler
plt.show()"""

# x1 = [1, 4, 2, 3, 4, 4, 4, 4, 4, 5, 5]
# x2 = [1, 4, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]
# bins = [x + 0.5 for x in range(0, 6)]
# plt.hist(x1, bins = bins, color = 'yellow',edgecolor = 'red', hatch = '/', label = 'x1')
# # plt.hist(x2, bins = bins, color = 'green', alpha = 0.5,edgecolor = 'blue', hatch = '/', label = 'x2')
# # plt.ylabel('valeurs')
# plt.xlabel('nombres')
# plt.title('superpose')
# plt.legend()
# plt.show()

"""
x = [1, 1, 1, 3, 3, 4, 2, 2, 4, 5,4]
x1=[1,1,2,2,3,4,5]
x2=[1,1,2,2,2,3,4,4,5,5,5]
x3=[1,2,2,2,2,3,4,4,5,5,5]
plt.hist([x,x1,x2,x3], range = (1, 5), bins = 5, color = ['yellow','green','blue','orange'],
            edgecolor = 'red',histtype = 'barstacked',align='left')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Exemple d\' histogramme simple')
plt.show()"""