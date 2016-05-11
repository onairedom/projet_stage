#!/usr/bin/python3
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
import pylab as plt
from matplotlib.backends.backend_pdf import PdfPages


def histoByYear(subjects, secondWithCoeff, fileTxt):

	nb_heure=[];
	for i in secondWithCoeff:
		p=(i/3600)
		nb_heure.append(p)

	x=[]
	k=0;
	for j in subjects:
		x.append(k)
		k=k+1


	##########################################################histogramme terminé######################################################################################
	plt.figure(1)
	plt.bar(x, nb_heure, align='center', edgecolor = 'red', hatch = '/')  # ces deux lignes permettent de mettre des string dans un histogrammes plutot que des entiers
	plt.xticks(x, subjects) # x est une liste composé du nombre d'éléments qe l'on veut mettre en horizontal
	plt.grid(True) # celà sert à mettre une grille dans le diagramme
	plt.xlabel('Matières') 
	plt.ylabel(u"Nombre d'heures")
	plt.title("Nombre d'heures par matière sur l'année")
	plt.savefig('figure1'+'.pdf')