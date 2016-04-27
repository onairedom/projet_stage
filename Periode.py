#!/usr/bin/python3
from histo_recap import histogramme
import time
import datetime
from pylab import *
import random
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages
import math
import pylab as plt

def periode_semaine():

	# lst=tableau()
	recap,time4,time3,time2,time,lst,Semaine,nb_mat,nb_heure,matiere=histogramme();


	a=int(input("Quelles semaines voulez vous voir ? Donnez la première "))
	b=int(input("La deuxième "))

	print(a)
	print(b)

	x=[]
	if b<a:
		tps=52-a+b
		for i in range(tps+1): ###Permet de créer la variable pour afficher le nb de semaines en abscisse##############################
			if a==53:
				a=1
			x.append(a)
			a+=1

	else:
		tps=b-a;
		for i in range(tps+1): ###Permet de créer la variable pour afficher le nb de semaines en abscisse##############################
			x.append(a)
			a+=1

		
	for i in range(nb_mat+1): #car on commence a 0 et pour faire correspondre les numéros de matières avec les heures
		 	globals()['y%s' % i] = [0] # créé des tableau avec des noms comportant un chiffre de 0 à nb de matière
		 	
	for i in range(nb_mat+1): 
		for j in range (tps):
			globals()['y%s' % i].append(0) # créé des tableaux correspondant 




	for i in Semaine:
			m=0;a=0;
			for l in x:
				if i[0]==l:
					# print("c'est moi",a)
					# for e in recap:
					if m==(nb_mat+1):
							m=0;
					for j in i:
						if type(j)==float : #Prend le nombre d'heure par matière et insère le numéro de la semaine qui correspond à l'entier du nb d'heure pr pouvoir le rpz
							globals()['y%s' % m][a]=j # utilise tableau ayant des noms de 0 à nb_matière et ajoute le nombre d'heure a l'intérieur
			
						m+=1;
				a+=1
	# print(Semaine)
	print(y0,sum(y0))
	print(y1,sum(y1))
	print(y2,sum(y2))
	print(y3,sum(y3))
	print(y4,sum(y4))
	print(y5,sum(y5))
	print(y6,sum(y6))
	print(y7,sum(y7))
	print(y8,sum(y8))
	print(y9,sum(y9))		

	col=[]
	Y=[];L=[]
	k=0;X=[];k1=1
	to=1;cpt=0
	m=0
	for w in range(tps+1): #Creation tableau qui va additionner les y entre eux pr permettre suppression superpositions
		X.append(0)


	for i in recap:
		a=globals()['y%s' % to]  ## Utilisation de tableau avec des noms différent pour remplir les horraires en fonction de chaque matière
		Y.append(a)
		L.append(i)
		cpt=0


		for j in range (tps):
			for cpt in range(k1):
					# print('chaud chaud',k)
				m=m+globals()['y%s' % cpt][j]
					# print(globals()['y%s' % cpt][j])
					
				# print('salut',m)
				# print('hey',j)
			X[j]=m
			m=0

		if k==0:
			col.append('yellow')		
		elif k==1:
			col.append('green')
		elif k==2:
			col.append('grey')
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
			col.append('blue')
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
		
		figure(1)
		barWidth = 0.8
		r = range(len(a))
		plt.bar(r, a, width = barWidth,bottom=X ,color = col[k], edgecolor = ['blue' for i in y1], linestyle = 'solid', hatch ='/',linewidth = 3, label=recap[k])
		plt.xticks([r + barWidth for r in range(len(a))], x)
		print("c'est aaaaaa",X)
		k+=1;
		k1+=1
		to+=1;

	
	plt.xlabel('Numéro des Semaines')
	plt.ylabel("Nombre d'Heures")
	plt.title("Nombre d'heures par matière sur la période demandé")
	plt.legend()
	
	return(recap,time4,time3,time2,time,lst,Semaine,nb_mat,nb_heure,matiere);