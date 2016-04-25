#!/usr/bin/python3
from temps_recap import temps
import time
import datetime
import random
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import pylab as plt


def semaine():
	###########################################création tableau pour toutes les semaines###################################################################
	recap,time4,time3,time2,time,lst=temps();

	print(type(lst))
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
		elif m=='Férié':
			break;
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
			t1=t1*0.5
		elif j[0]=='AM2':
			t1=t1*0.5
		elif j[5]=='_TD':
			t1=t1*0.5
		time=t1.total_seconds()

		time2=time/3600
		if m in Semaine[0]:  #Recherche le nom de la matière dans la première ligne du tableau semaine pour lui assigné la position de la matière dans le tableau par la suite
			index=Semaine[0].index(m)
		Semaine[s][index]=time2+Semaine[s][index]
	return(recap,time4,time3,time2,time,lst,Semaine,nb_mat);