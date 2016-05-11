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



def creationPdf(subjects, secondWithCoeff, Weeks, fileTxt, fileT):
	## Concatenate pdf
	os.system('pdftk figure1.pdf figure2.pdf cat output Res.pdf')
	
	#Créer fichier texte récapitulatif
	
	## Concatenate pdf
	if os.path.exists('figure3.pdf') :
		os.system('pdftk Res.pdf figure3.pdf cat output Resultat.pdf')
		os.system('pdftk Resultat.pdf '+fileT+'.pdf cat output Recapitulatif.pdf')
		## Suppression pdf inutile
		os.system('rm -rf figure1.pdf figure2.pdf figure3.pdf Resultat.pdf Res.pdf ' + fileT +'.pdf')
		
	else :	
		os.system('pdftk Res.pdf '+ fileT +'.pdf cat output Recapitulatif.pdf')
		## Suppression pdf inutile
		os.system('rm -rf figure1.pdf figure2.pdf Res.pdf ' + fileT +'.pdf')

class HistogramWindow:
	def __init__(self):
		self.fenetre = Tk()
		self.week1 = 0
		self.week2 = 0
		self.Wk1 = Entry(self.fenetre)
		self.Wk1.grid(row=2, column=3)

		self.Wk2 = Entry(self.fenetre)
		self.Wk2.grid(row=3, column=3)
	 
##creation du texte pour
		self.L2 = Label(self.fenetre, text="Première semaine")
		self.L2.grid(row=2, column=2)

		self.L3 = Label(self.fenetre, text="Deuxième semaine")
		self.L3.grid(row=3, column=2)
	
	

		self.ok= Button(self.fenetre, text ='OK', command=self.weekByChoice)
		self.ok.grid(row=1, column=3)

		self.L4 = Label(self.fenetre, text = 'Nom du fichier text')
		self.L4.grid(row = 3, column = 0)

		self.nameFile = Entry(self.fenetre)
		self.nameFile.grid(row=3,column=1)


# if nbw == 0:
		self.Wk1.configure(state='disabled')
		self.Wk2.configure(state='disabled')

		self.bouton = Checkbutton(self.fenetre, text="Choisir semaines", command = self.nbWeek)
		self.bouton.grid(row=1, column=2)


		self.L1 = Label(self.fenetre, text="Nombre de documents")
		self.L1.grid(row=2, column=0)


		self.Entree = Entry(self.fenetre)
		self.Entree.grid(row=2, column=1)
		self.valeur = Button(self.fenetre, text =' Valider', command=self.validate)
		self.valeur.grid(row=0, column=0)
		self.addButton = Button(self.fenetre, text =' Ajouter', command=self.openFiles)
		self.addButton.grid(row=0, column=2)
		self.fenetre.mainloop()


	def openFiles(self):
		self.fileTxt, self.fileT = self.askOpenTxt()
		self.full_list = self.repondre()


	def nbWeek(self):
		##active entry for futur histogram
		self.Wk1.configure(state='normal')
		self.Wk2.configure(state='normal')
		# nbw = 1

	def validate(self):
		##creation fichier texte et pdf
		##Creation de tuple
		lst_tup = tuple1(self.full_list)
		##creation listes temps en fonction de matière et liste de matière (voir hourByYear.py)

		self.subjects, secondWithCoeff, second, hourWithCoeff, hour = getHourByYear(lst_tup)
		##Créer tableau Heure/semaine et la variable nb de matière(voir hourByWeek.pŷ)
		self.Weeks, self.numberSubjects = hourByWeek(lst_tup, self.subjects)

		##Créer premier histogramme (voir histo_recap.py)
		histoByYear(self.subjects, secondWithCoeff, self.fileTxt)

		##Créer 2ème histogramme sur l'année( voir  histo2.py)
		histoByWeek(self.subjects, self.Weeks, self.numberSubjects, self.fileTxt)

		if(not self.Wk1.get() or not self.Wk2.get()):
			txtRecap(self.subjects, secondWithCoeff, 0, 0, self.Weeks, self.fileTxt, self.fileT)
		else:
			##Création PDF avec toutes les infos
			week1 = int(self.Wk1.get())
			week2 = int(self.Wk2.get())
			txtRecap(self.subjects, secondWithCoeff, week1, week2, self.Weeks, self.fileTxt, self.fileT)

		creationPdf(self.subjects, secondWithCoeff, self.Weeks, self.fileTxt, self.fileT)

		plt.show()
		
			
	def weekByChoice(self):
		if not self.Wk1.get():
			print('HEY')
			return
		else:
			##Créer 3eme histogramme en fonction de l'utilisateur et afficher les 3 histogrammes(voir Periode.py)
			week1 = self.Wk1.get()
			week2 = self.Wk2.get()
			week1 = int(week1)
			week2 = int(week2)
			duration, useless_week1, useless_week2 = histoByChoice(self.subjects, self.Weeks, self.numberSubjects, self.fileTxt, self.fileT, week1, week2)
			print('week',week1,week2)
			return (duration, week1, week2)
			




	def askOpenTxt(self):
		if not self.nameFile.get():
			return
		else : 
			## Creation file txt
			nameFichier = self.nameFile.get()
			fileTxt, fileT = createTxt(nameFichier)
			return (fileTxt, fileT)

	def repondre(self):
		full_list = []
		cpt=int(self.Entree.get())
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
		return full_list
	

#main()
win = HistogramWindow()