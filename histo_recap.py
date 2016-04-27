#!/usr/bin/python3
from heures_semaine import semaine
import time
import datetime
import random
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import pylab as plt


def histogramme():

	recap,time4,time3,time2,time,lst,Semaine,nb_mat=semaine();

	nb_heure=[];matiere=[];x=[]
	k=0;
	for i in time4:
		p=(i/3600)
		nb_heure.append(p)

	for j in recap:
		x.append(k)
		k=k+1
		matiere.append(j)


	##########################################################histogramme terminé######################################################################################
	plt.figure(1)
	plt.bar(x, nb_heure, align='center', edgecolor = 'red', hatch = '/')  # ces deux lignes permettent de mettre des string dans un histogrammes plutot que des entiers
	plt.xticks(x, matiere) # x est une liste composé du nombre d'éléments qe l'on veut mettre en horizontal
	plt.grid(True) # celà sert à mettre une grille dans le diagramme
	plt.xlabel('Matières') 
	plt.ylabel(u"Nombre d'heures")
	plt.title("Nombre d'heures par matière sur l'année")
	plt.text(600,500,'STCE=SOUTENANCE EW=Eval Wims')# a travailler


	

	return(recap,time4,time3,time2,time,lst,Semaine,nb_mat,nb_heure,matiere);
