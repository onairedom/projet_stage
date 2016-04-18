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
			if j=='SOUTENANCE':
				j='STCE';
			elif j=='Eval Wims':
				j='EW'
			
			if i==j:  #Compare grand tableau et list matière

				k=0;
					 #Récupère durée d'un cours
				Hour=','.join(e[7])  #Sépare  heure pour créer Heure avec datetime
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
				elif e[0]=='DS':
					t=t+t1*0.5
				elif e[0]=='AM2':
					t=t+t1*0.5
				else:
					t=t+t1
				t5=t.total_seconds()
				t3=t1.total_seconds()
				t4=int(t3+t4)
	time4.append(t5)	#Création de tableau qui garde la durée en seconds en tenant compte coeff
	time3.append(t4)	#Création de tableau qui garde la durée en seconds sans coeff
	time2.append([str(t)])	#Création de tableau qui garde la durée en jours et heures avec datetime avec coeff
	time.append([str(t2)])	#Création de tableau qui garde la durée en jours et heures avec datetime sans coeff
	t4=0
	t5=0
	t2=datetime.timedelta(0,(0+0))
	t=datetime.timedelta(0,(0+0))


nb_heure=[];matiere=[];x=[]
k=0;
for i in time4:
	p=(i/3600)
	nb_heure.append(p)

for j in recap:
	x.append(k)
	k=k+1
	matiere.append(j)



############################################histogramme terminé##############################################""
# plt.bar(x, nb_heure, align='center', edgecolor = 'red', hatch = '/')  # ces deux lignes permettent de mettre des string dans un histogrammes plutot que des entiers
# plt.xticks(x, matiere) # x est une liste composé du nombre d'éléments qe l'on veut mettre en horizontal
# plt.grid(True) # celà sert à mettre une grille dans le diagramme
# plt.xlabel('Matières') 
# plt.ylabel(u"Nombre d'heures")
# plt.title("Nombre d'heures par matière sur l'année")
# plt.text(600,500,'STCE=SOUTENANCE EW=Eval Wims')# a travailler
# plt.show()


###########################################création tableau pour toutes les semaines####################################################

l=54 # on créé une variable qui rpz le nb de semaine plus 1 pour le nombre de matière

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
			Semaine[k].append(0)
	k+=1


for j in lst:		#On va chercher le nombre d'heure par matière par semaine pour compléter ce nouveau tableau
	m=j[0]
	if m=='SOUTENANCE':
		m='STCE';
	elif m=='Eval Wims':
		m='EW'
	s=j[8]
	
	Hour=','.join(j[7])  #Sépare  heure pour créer Heure avec datetime
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
	if j[1]==1:	#Permet d'augmenter heure faite en fonction type de séance cours,td,tp...
		t1=t1*1.5
	elif j[0]=='DS':
		t=t1*0.5
	elif j[0]=='AM2':
		t1=t1*0.5
	elif j[5]=='_TD':
		t1=t1*0.5
	time=t1.total_seconds()

	time2=time/3600
	if m in Semaine[0]:  #Recherche le nom de la matière dans la première ligne du tableau semaine pour lui assigné la position de la matière dans le tableau par la suite
		index=Semaine[0].index(m)
	Semaine[s][index]=time2+Semaine[s][index]

###############################################création 2ème histogramme pour nb heure matière sur toute l'année########################################


for i in range(nb_mat+1): #car on commence a 0 et pour faire correspondre les numéros de matières avec les heures
	 	globals()['y%s' % i] = [0] # créé des tableau avec des noms comportant un chiffre de 0 à nb de matière

for i in range(nb_mat+1): 
	for j in range (51):
		globals()['y%s' % i].append(0) # créé des tableaux correspondant 


nb_heure=[];matiere=[];x=[];
m=-1;n=0;k=0;
for i in Semaine: #Parcours tableau semaine
	for j in i:	#parcours chaque ligne avec nombre d'heure ont le meme indice que dans le tableau recap des matière
		a=i[0]
		# print("c'est moi",a)
		if m==(nb_mat):
			m=0;
		# print(j)
		if type(j)==float : #Prend le nombre d'heure par matière et insère le numéro de la semaine qui correspond à l'entier du nb d'heure pr pouvoir le rpz
			globals()['y%s' % m][a]=j # utilise tableau ayant des noms de 0 à nb_matière et ajoute le nombre d'heure a l'intérieur
			# print("matière",m, "nb heure",j)
		m+=1;	



print (Semaine)
print(y0)
print(y1)
print(y2)
print(y3)
print(y4)
print(y5)
print(y6)
print(y7)


j=1

for j in range(53):
	x.append(k)
	k=k+1
	
# print("x",x)
# print("recap",recap)
# print("me voila",y0)
# print("me voila1",y1)
# print("me voila2",y2)
# print("me voila3",y3)
# print("me voila4",y4)
# print("me voila5",y5)
# print("me voila6",y6)
# print("me voila7",y7)
# plt.hist([y0,y1,y2,y3,y4,y5,y6,y7], range = (1, len(x)), bins = len(x), color = ['yellow','green','blue','orange','grey','black','red','brown'],
#             edgecolor = 'red',histtype = 'barstacked',align='left')
# plt.xlabel('valeurs')
# plt.ylabel('nombres')
# plt.title('Exemple d\' histogramme simple')
# plt.show()


col=[]
Y=[];L=[]
k=0;
j=0;
for i in recap:
	a=globals()['y%s' % j]
	Y.append(a)
	L.append(i)
	j+=1;
	if k==0:
		col.append('yellow')		
	elif k==1:
		col.append('green')
	elif k==2:
		col.append('blue')
	elif k==3:
		col.append('orange')
	elif k==4:
		col.append('brown')
	elif k==5:
		col.append('black')
	elif k==6:
		col.append('purple')
	elif k==7:
		col.append('red')
	elif k==8:
		col.append('magenta')
	elif k==9:
		col.append('grey')
	elif k==10:
		col.append('pink')
	elif k==11:
		col.append('#AF1425')
	elif k==12:
		col.append('#AF1687')
	elif k==13:
		col.append('#AF1267')
	elif k==14:
		col.append('#AF1381')
	elif k==15:
		col.append('#AF1594')
	elif k==16:
		col.append('#AF2154')
	elif k==17:
		col.append('#AF3168')
	elif k==18:
		col.append('#AF8463')
	elif k==19:
		col.append('#AF7543')
	elif k==20:
		col.append('#AF8136')
	elif k==21:
		col.append('#AF9463')
	elif k==22:
		col.append('#AF2425')
	elif k==23:
		col.append('#AF3425')
	elif k==24:
		col.append('#AF4687')
	elif k==25:
		col.append('#AF5267')
	elif k==26:
		col.append('#AF6381')
	elif k==27:
		col.append('#AF5594')
	elif k==28:
		col.append('#AF4154')
	elif k==29:
		col.append('#AF2168')
	elif k==30:
		col.append('#AF8463')
	elif k==31:
		col.append('#AF4543')
	elif k==32:
		col.append('#AF2136')
	elif k==33:
		col.append('#AF5463')
	elif k==34:
		col.append('#AF1687')
	elif k==35:
		col.append('#AF1267')
	elif k==36:
		col.append('#AF1381')
	elif k==37:
		col.append('#AF1594')
	k+=1;
	barWidth = 0.8
	print(i)
	r = range(len(y0))
	plt.bar(r, a, width = barWidth, color = col, edgecolor = ['blue' for i in y1], linestyle = 'solid', hatch ='/',linewidth = 3)
	plt.xticks([r + barWidth / 2 for r in range(len(y0))], x)


red_patch = patches.Patch(color='red', label='The red data')
plt.legend(handles=[red_patch])
# plt.legend(Y,L )
plt.xlabel('Numéro des Semaines')
plt.ylabel("Nombre d'Heures")
plt.title("Nombre d'heures par matière sur l'année")
plt.show()




# barWidth = 0.8
# y1 = [1, 2, 4, 3]
# y2 = [3.2, 4, 4.8, 3]
# r = range(len(y1))

# plt.bar(r, y1, width = barWidth, color = ['yellow' for i in y1],
#            edgecolor = ['blue' for i in y1], linestyle = 'solid', hatch ='/',
#            linewidth = 3)
# # plt.bar(r, y2, width = barWidth, bottom = y1, color = ['pink' for i in y1],
# #            edgecolor = ['green' for i in y1], linestyle = 'dotted', hatch = 'o',
# #            linewidth = 3)
# plt.xticks([r + barWidth / 2 for r in range(len(y1))], ['A', 'B', 'C', 'D'])
# plt.show()



# bins = [x + 0.5 for x in range(1, 52)]
# plt.hist(Y, range = (1, len(x)), bins = bins, color = col, edgecolor = 'red',histtype = 'barstacked',align='mid')
# #plt.xticks(x, matiere) # x est une liste composé du nombre d'éléments qe l'on veut mettre en horizontal
# plt.axis([1,52,1,23])

# plt.title("Représentation du nombre d'heure faite dans l'année par matière")
# plt.show()

"""
plt.bar(x, nb_heure, align='center', edgecolor = 'red', hatch = '/')  # ces deux lignes permettent de mettre des string dans un histogrammes plutot que des entiers
plt.xticks(x, matiere) # x est une liste composé du nombre d'éléments qe l'on veut mettre en horizontal
plt.grid(True) # celà sert à mettre une grille dans le diagramme
plt.xlabel('Semaines') 
plt.ylabel(u"Nombre d'heures")

plt.text(600,500,'STCE=SOUTENANCE EW=Eval Wims')# a travailler
plt.show()"""



# x = [1, 1, 1, 3, 3, 4, 2, 2, 4, 5,4]
# x1=[1,1,2,2,3,4,5]
# x2=[1,1,2,2,2,3,4,4,5,5,5]
# x3=[1,2,2,2,2,3,4,4,5,5,5]
# plt.hist([x,x1,x2,x3], range = (1, 5), bins = 5, color = ['yellow','green','blue','orange'],
#             edgecolor = 'red',histtype = 'barstacked',align='left')
# plt.xlabel('valeurs')
# plt.ylabel('nombres')
# plt.title('Exemple d\' histogramme simple')
# plt.show()


