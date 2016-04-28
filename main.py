#!/usr/bin/python3
# from Periode import periode_semaine
# from histo_recap import histogramme
# from histo2 import histo
from createTab import *
from creation_tuple import *
from hourByYear import *
from hourByWeek import *
from histoByYear import *
from histoByWeek import *
from histoByChoice import *
from txtRecap import *
# import time
# import datetime
# import random
# import calendar
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import math
# import pylab as plt




# recap,time4,time3,time2,time,lst,Semaine,nb_mat,nb_heure,matiere=histo();

def main():
	size=getNumberFiles()
	full_list=[]
	for i in range (size):
		#acquiert chemin du fichier contenant infos pr fichier i
		path=getFilePath()

		#créer tableau récapitulatif
		lst = createTab('input/gpu.txt') #debug 
		#lst=createTab(path)

		# ajouter lst à full_list
		full_list += lst

	##utiliser create_tuple
	lst_tup=tuple1(full_list)

	##creation listes temps en fonction de matière et liste de matière (voir hourByYear.py)
	subjects, secondWithCoeff, second, hourWithCoeff, hour=getHourByYear(lst_tup)
	
	##Créer tableau Heure/semaine et la variable nb de matière(voir hourByWeek.pŷ)
	Weeks, numberSubjects = hourByWeek(lst_tup, subjects)

	##Créer premier histogramme (voir histo_recap.py)
	histoByYear(subjects, secondWithCoeff)
	
	##Créer 2ème histogramme sur l'année( voir  histo2.py)
	histoByWeek(subjects, Weeks, numberSubjects)
	
	##Créer 3eme histogramme en fonction de l'utilisateur et afficher les 3 histogrammes(voir Periode.py)
	duration, week1, week2 = histoByChoice(subjects, Weeks, numberSubjects)

	##Créer fichier texte récapitulatif
	txtRecap(subjects, secondWithCoeff, duration, week1, week2, Weeks)





## input function
def getNumberFiles():
	nb_files=int(input('Cb de fichier?'))
	return nb_files


def getFilePath():
	path=input('chemin?')
	return path






main()








# def demande():
# 	# Récupérer tous les tab à partir des fichiers
# 	list_tab = []
# 	for
# 		path = getFilePath()
# 		tab.append(txt2tab(path))

# 	# Rassembler les tab en 1 seul
# 	tab = assemble_tab(list_tab)

# 	# Transformer table en tuple
# 	tup = tab2tuple(tab)

# 	# a=int(input("Combien de fichiers voulez vous charger ?"))

# 	# for e in range(b1):
# 	# 	a=input('Donnez le chemin du fichier')
# 	# 	lst=tableau(a)
# 	return(lst)

