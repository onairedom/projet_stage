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
import os 




def main():
	tab1=0
	size=getNumberFiles()
	cpt=0
	full_list=[]
	for i in range (size):
		#acquiert chemin du fichier contenant infos pr fichier i
		path, cpt=getFilePath(cpt)

		#créer tableau récapitulatif
		lst = createTab(path)

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
	txtRecap(subjects, secondWithCoeff, week1, week2, Weeks, fileTxt, fileT)

	## Concatenate pdf
	os.system('pdftk Res.pdf figure3.pdf cat output Resultat.pdf')
	os.system('pdftk Resultat.pdf ben.pdf cat output Recapitulatif.pdf')

	## Suppression pdf inutile
	os.system('rm -rf figure1.pdf figure2.pdf figure3.pdf Resultat.pdf Res.pdf ' + fileT +'.pdf')



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





