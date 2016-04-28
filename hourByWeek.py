#!/usr/bin/python3
import time
import datetime
import random
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import pylab as plt


def hourByWeek(inputTuple, subjects):
	###########################################création tableau pour toutes les semaines###################################################################

	l=54 # on créé une variable qui rpz le nb de semaine plus 1 pour le nombre de matière (oui il y a 53 semaines dans l'année)
	k=0
	Weeks=[]
	for i in range(l):
		Weeks.append([]);


	Weeks[0].append(0)
	for i in subjects:	# On créé le nb de colonnes qui correspondent au nombre de matière plus 1
		Weeks[0].append(i)

	numberSubjects=len(subjects)
	member=0;
	for j in Weeks:		#On créé le nombre des semaines dans la colonne 0 du tableau
		if k>0:
			Weeks[k].append(k)
			for m in range(numberSubjects):		#On ajoute les colonnes vide à chaque ligne
				Weeks[k].append(0)
		k+=1

	for j in inputTuple:		#On va chercher le nombre d'heure par matière par semaine pour compléter ce nouveau tableau
		subject=j[0]
		if subject=='SOUTENANCE':
			subject='STCE';
		elif subject=='Eval Wims':
			subject='EW'
		elif subject=='Férié':
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

		if subject in Weeks[0]:  #Recherche le nom de la matière dans la première ligne du tableau semaine pour lui assigné la position de la matière dans le tableau par la suite
			index=Weeks[0].index(subject)
		Weeks[s][index]=time2+Weeks[s][index]
	return(Weeks,numberSubjects);