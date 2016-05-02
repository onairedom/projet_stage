#!/usr/bin/python3
from createTab import *
from creation_tuple import *
from hourByYear import *
from hourByWeek import *
from histoByYear import *
from histoByWeek import *
from histoByChoice import *
from txtRecap import *
from createTxt import *
#from pdftk import *
import os 
# import time
# import datetime
# import random
# import calendar
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import math
# import pylab as plt
# import sys
# import tkinter 
# import tkinter.filedialog
# import os

# root = tkinter.Tk()
# currdir = os.getcwd()+'/input/'



# recap,time4,time3,time2,time,lst,Semaine,nb_mat,nb_heure,matiere=histo();

def main():
	enable=0; tab1=0
	size=getNumberFiles()
	cpt=0
	full_list=[]
	for i in range (size):
		#acquiert chemin du fichier contenant infos pr fichier i
		path, cpt=getFilePath(cpt)

		#créer tableau récapitulatif
		lst, tab1 = createTab(path,enable) #debug 
		enable=1

		# ajouter lst à full_list
		full_list += lst
		
	##supprimer élément vide
	full_list = recondition(full_list)
	
	##utiliser create_tuple
	lst_tup = tuple1(full_list)

	## Creation file txt
	fileTxt, fileT = createTxt()

	##creation listes temps en fonction de matière et liste de matière (voir hourByYear.py)
	subjects, secondWithCoeff, second, hourWithCoeff, hour=getHourByYear(lst_tup)
	## erreur sur le calcul du nb d'heure sur l'année

	##Créer tableau Heure/semaine et la variable nb de matière(voir hourByWeek.pŷ)
	Weeks, numberSubjects = hourByWeek(lst_tup, subjects)

	##Créer premier histogramme (voir histo_recap.py)
	histoByYear(subjects, secondWithCoeff, fileTxt)

	
	# ##Créer 2ème histogramme sur l'année( voir  histo2.py)
	histoByWeek(subjects, Weeks, numberSubjects, fileTxt)

	##Créer 3eme histogramme en fonction de l'utilisateur et afficher les 3 histogrammes(voir Periode.py)
	duration, week1, week2 = histoByChoice(subjects, Weeks, numberSubjects, fileTxt,fileT)

	## Concatenate pdf
	os.system('pdftk figure1.pdf figure2.pdf cat output Res.pdf')

	##Créer fichier texte récapitulatif
	txtRecap(subjects, secondWithCoeff, duration, week1, week2, Weeks, fileTxt, fileT)

	## Concatenate pdf
	os.system('pdftk Res.pdf figure3.pdf cat output Resultat.pdf')
	os.system('pdftk Resultat.pdf ben.pdf cat output Recapitulatif.pdf')
	os.system('rm -rf figure1.pdf figure2.pdf figure3.pdf Resultat.pdf Res.pdf')



## supprime éléments vides
def recondition(full_list):
	# for elem in full_list:
	# 	if elem == []:
	cpt1=0
	for cpt in full_list:
		if cpt==[]:
			cpt1+=1
	for cpt2 in range(cpt1):
		full_list.remove([])

	return full_list;

## input function
def getNumberFiles():
	nb_files=int(input('Cb de fichier?'))
	return nb_files


def getFilePath(cpt):
	path=input('chemin?')
	if cpt==0:
		path='input/gpu.txt'
	else :
		path='input/EPU.ics'
	# root.withdraw() #use to hide tkinter window
	# path = tkinter.filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
	# root.deiconofy()
	cpt+=1
	return (path, cpt)






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

