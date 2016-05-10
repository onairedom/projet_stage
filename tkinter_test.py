#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import * 
from tkinter.filedialog import *
from createTab import *
from creation_tuple import *
from createTxt2 import *
from hourByYear import *
from hourByWeek import *
from histoByYear import *
from histoByWeek import *
from histoByChoice2 import *
from txtRecap import *
import os 



def main():
	global fenetre
	global nbw; nbw = 0; 
	global week1; global week2
	global Wk1; global Wk2
	week1=0; week2=0
	fenetre = Tk()  #Défini la fenètre tkinter au nom de fenètre

	
	##creation du texte pour
	L2 = Label(fenetre, text="Première semaine")
	L2.grid(row=2, column=2)

	L3 = Label(fenetre, text="Deuxième semaine")
	L3.grid(row=3, column=2)
	
	Wk1 = Entry(fenetre)
	Wk1.grid(row=2, column=3)

	Wk2 = Entry(fenetre)
	Wk2.grid(row=3, column=3)

	ok= Button(fenetre, text ='OK', command=weekByChoice)
	ok.grid(row=1, column=3)

	L4 = Label(fenetre, text = 'Nom du fichier pdf')
	L4.grid(row = 3, column = 0)

	global nameFile
	nameFile = Entry(fenetre)
	nameFile.grid(row=3,column=1)

	if nbw == 0:
		Wk1.configure(state='disabled')
		Wk2.configure(state='disabled')

	bouton = Checkbutton(fenetre, text="Choisir semaines", command = nbWeek)
	bouton.grid(row=1, column=2)


	L1 = Label(fenetre, text="Nombre de documents")
	L1.grid(row=2, column=0)

	global Entree
	Entree = Entry(fenetre)
	Entree.grid(row=2, column=1)
	valeur = Button(fenetre, text =' Valider', command=repondre)
	valeur.grid(row=0, column=0)
	fenetre.mainloop()

	##Creation de tuple
	lst_tup = tuple1(full_list)

	##creation fichier texte et pdf
	fileTxt, fileT=askOpenTxt()

	##creation listes temps en fonction de matière et liste de matière (voir hourByYear.py)
	global subjects
	subjects, secondWithCoeff, second, hourWithCoeff, hour=getHourByYear(lst_tup)

	##Créer tableau Heure/semaine et la variable nb de matière(voir hourByWeek.pŷ)
	global Weeks
	global numberSubjects
	Weeks, numberSubjects = hourByWeek(lst_tup, subjects)

	##Créer premier histogramme (voir histo_recap.py)
	histoByYear(subjects, secondWithCoeff, fileTxt)

	##Créer 2ème histogramme sur l'année( voir  histo2.py)
	histoByWeek(subjects, Weeks, numberSubjects, fileTxt)
		
	##Création PDF avec toutes les infos
	creationPdf(subjects, secondWithCoeff, week1, week2, Weeks, fileTxt, fileT)
	

def askOpenTxt():
	if not nameFile.get():
		return
	else : 
		## Creation file txt
		global fileT
		global fileTxt
		nameFichier = nameFile.get()
		fileTxt, fileT = createTxt(nameFichier)
		return(fileTxt, fileT)

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



def weekByChoice():
	if not Wk1.get():
		print('HEY')
		return
	else :
		##Créer 3eme histogramme en fonction de l'utilisateur et afficher les 3 histogrammes(voir Periode.py)
		print('Salut')
		week1 = Wk1.get()
		week2 = Wk2.get()
		week1 = int(week1)
		week2 = int(week2)
		print(type (week1))
		duration, week1, week2 = histoByChoice(subjects, Weeks, numberSubjects, fileTxt, fileT, week1, week2)
		return(duration, week1, week2)
		

def repondre():
	global full_list
	full_list=[]
	cpt = Entree.get()
	cpt=int(cpt)
	for i in range (cpt):
		filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.ics'),('all files','.*')] and [('txt files','.txt'),('all files','.*')] )
		fichier = open(filename, "r")
		content = fichier.read()
		
		##Creation de listes
		lst=createTab(filename)
		
		full_list+=lst

		##Suppression éléments vide
		full_list = recondition(full_list)
		fichier.close()
	fenetre.quit()


def choix():
	

	menubar = Menu(fenetre)
	menu1 = Menu(menubar, tearoff=0)
	menu1.add_command(label="Créer", command=choix)
	menu1.add_command(label="Editer", command=choix)
	menu1.add_separator()
	menu1.add_command(label="Quitter", command=fenetre.quit)
	menubar.add_cascade(label="Fichier", menu=menu1)
	fenetre.config(menu=menubar)
	fichier = Frame(fenetre, borderwidth=2, relief=GROOVE)
	fichier.pack(side=LEFT, padx=30, pady=30)
	Label(fichier, text="Charger Fichier").pack(padx=10, pady=10)
	

	##Creation de tuple
	lst_tup = tuple1(full_list)

	## Creation file txt
	fileTxt, fileT = createTxt()
	fenetre.quit()

	##creation listes temps en fonction de matière et liste de matière (voir hourByYear.py)
	subjects, secondWithCoeff, second, hourWithCoeff, hour=getHourByYear(lst_tup)

def creationPdf(subjects, secondWithCoeff, week1, week2, Weeks, fileTxt, fileT):
	## Concatenate pdf
	os.system('pdftk figure1.pdf figure2.pdf cat output Res.pdf')

	##Créer fichier texte récapitulatif
	txtRecap(subjects, secondWithCoeff, week1, week2, Weeks, fileTxt, fileT)

	## Concatenate pdf
	if nbw==0 :
		os.system('pdftk Res.pdf ben.pdf cat output Recapitulatif.pdf')
	else :	
		os.system('pdftk Res.pdf figure3.pdf cat output Resultat.pdf')
		os.system('pdftk Resultat.pdf ben.pdf cat output Recapitulatif.pdf')

	## Suppression pdf inutile
	os.system('rm -rf figure1.pdf figure2.pdf figure3.pdf Resultat.pdf Res.pdf ' + fileT +'.pdf')
	fenetre.quit()

def nbWeek():
	##active entry for futur histogram
	Wk1.configure(state='normal')
	Wk2.configure(state='normal')


	


# def validationSemaine():
# 	week1 = Wk1.get()
# 	week2 = Wk2.get()
# 	print(week1)
# 	print(week2)
	

main()