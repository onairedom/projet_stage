#!/usr/bin/python3
from creation_tuple import tuple1
import time
import datetime
import random
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import pylab as plt
from creation_tuple import tuple1

def temps():

	k=0;Heure=0;Min=0
	recap=[];time=[];time2=[];time3=[];time4=[]
	semaine=[];
	lst=tuple1()
	j=0
	var=""
	for i in lst:	# Parcours grand tableau
		if lst[k][0] not in recap: #récupère élément tableau
			recap.append(lst[k][0]) #ajoute élément dans petit tableau
		if 'Férié' in recap:
			recap.remove('Férié')
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
				if j=='Férié':
					break;
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

	return(recap,time4,time3,time2,time,lst);
	