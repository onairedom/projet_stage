#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import * 
from tkinter.filedialog import *
from createTab import *
from creation_tuple import *
from createTxt import *
from hourByYear import *
from hourByWeek import *

# from histoByYear import *
# from histoByWeek import *
# from histoByChoice import *
# from txtRecap import *

# import os 

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

def repondre():
	full_list=[]
	cpt = Entree.get()
	cpt=int(cpt)
	for i in range (cpt):
		filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt','.ics'),('all files','.*')])
		fichier = open(filename, "r")
		content = fichier.read()
		
		##Creation de listes
		lst=createTab(filename)
		
		full_list+=lst

		##Suppression éléments vide
		full_list = recondition(full_list)
		print(full_list)
		fichier.close()
	graphic(full_list)

def graphic(full_list):
	##Creation de tuple
	lst_tup = tuple1(full_list)

	## Creation file txt
	fileTxt, fileT = createTxt()
	fenetre.quit()

	##creation listes temps en fonction de matière et liste de matière (voir hourByYear.py)
	subjects, secondWithCoeff, second, hourWithCoeff, hour=getHourByYear(lst_tup)
	

	##Créer tableau Heure/semaine et la variable nb de matière(voir hourByWeek.pŷ)
	Weeks, numberSubjects = hourByWeek(lst_tup, subjects)

	# ##Créer premier histogramme (voir histo_recap.py)
	# histoByYear(subjects, secondWithCoeff, fileTxt)



	print(Weeks)

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

	print(subjects)
	
def main():
	global fenetre
	fenetre = Tk()  #Défini la fenètre tkinter au nom de fenètre
	L1 = Label(fenetre, text="Nombre de documents")
	L1.grid(row=1, column=0)
	# E1 = Entry(fenetre, bd =5)

	global Entree
	Entree = Entry(fenetre)
	Entree.grid(row=2, column=0)

	valeur = Button(fenetre, text =' Valider', command=repondre)

	valeur.grid(row=0, column=0)

	fenetre.mainloop()


# bouton=Button(fenetre , text="Valider", command=choix)


main()