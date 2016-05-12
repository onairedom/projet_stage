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

def getHourByYear(inputTuple):
	# Init
	k=0;Heure=0;Min=0;cp=0
	subjects=[];hour=[];hourWithCoeff=[];second=[];secondWithCoeff=[]
	semaine=[];
	
	for i in inputTuple:	# Parcours grand tableau

		if inputTuple[k][0] not in subjects: #récupère élément tableau
			subjects.append(inputTuple[k][0]) #ajoute élément dans petit tableau
		if 'Férié' in subjects:
			subjects.remove('Férié')
		k+=1
	
	for m in range(len(subjects)):
		if subjects[m]=='SOUTENANCE':
			subjects[m]='STCE'
			
		elif subjects[m]=='Eval Wims':
			subjects[m]='EW'

	t2=datetime.timedelta(0,(0+0))
	t=datetime.timedelta(0,(0+0))
	t4=0;t5=0
	for subject in subjects: #tableau liste matière

		t2=datetime.timedelta(0,(0+0))
		t1=datetime.timedelta(0,(0+0))
		for elementTuple in inputTuple: #prend chaque ligne grand tableau

			cp+=1
			for member in elementTuple:  #Récup info dans chaque ligne
				
				if member=='SOUTENANCE':
					member='STCE';
				elif member=='Eval Wims':
					member='EW'
				if member=='Férié':
					break;
				if member==subject:  #Compare grand tableau et list matière
					#Récupère durée d'un cours
					Hour=','.join(elementTuple[7])  #Sépare  heure pour créer Heure avec datetime
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
					if elementTuple[1]==1:	#Permet d'augmenter heure faite en fonction type de séance cours,td,tp...
						t=t+t1*1.5
					if elementTuple[0]=='DS':
						t=t+t1*0.5
					elif elementTuple[0]=='AM2':
						t=t+t1*0.5
					else:
						t=t+t1
			
					t5=t.total_seconds()
					t3=t1.total_seconds()
					t4=int(t3+t4)
					t1=0
		secondWithCoeff.append(t5)	#Création de tableau qui garde la durée en seconds en tenant compte coeff
		second.append(t4)	#Création de tableau qui garde la durée en seconds sans coeff
		hourWithCoeff.append([str(t)])	#Création de tableau qui garde la durée en jours et heures avec datetime avec coeff
		hour.append([str(t2)])	#Création de tableau qui garde la durée en jours et heures avec datetime sans coeff
		t4=0
		t5=0
		t2=datetime.timedelta(0,(0+0))
		t=datetime.timedelta(0,(0+0))

	print(secondWithCoeff, second)
	return(subjects, secondWithCoeff, second, hourWithCoeff, hour);