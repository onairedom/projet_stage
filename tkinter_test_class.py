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

class Histogram:
	def __init__(self):
		self.full_list = []
		self.lst_tup = ()
		self.subjects = ""
		self.secondWithCoeff = 0
		self.second = 0
		self.hourWithCoeff = 0
		self.hour = 0
		self.Weeks = []

	def set_output_file(self, filename):
		self.fileTxt, self.fileT = createTxt(filename)

	def add_file(self, filename):
		fichier = open(filename, "r")
		content = fichier.read()
			
		##Creation de listes
		lst=createTab(filename)
		
		self.full_list+=lst

		##Suppression éléments vide
		self.full_list = recondition(self.full_list)
		fichier.close()

		self.lst_tup = tuple1(self.full_list)
		self.subjects, self.secondWithCoeff, self.second, self.hourWithCoeff, self.hour = getHourByYear(self.lst_tup)
		##Créer tableau Heure/semaine et la variable nb de matière(voir hourByWeek.pŷ)
		self.Weeks, self.numberSubjects = hourByWeek(self.lst_tup, self.subjects)

	def create_by_year(self):
		histoByYear(self.subjects, self.secondWithCoeff, self.fileTxt)

	def create_by_week(self):
		histoByWeek(self.subjects, self.Weeks, self.numberSubjects, self.fileTxt)


	def create_by_choice(self, week1, week2):
		##Créer 3eme histogramme en fonction de l'utilisateur et afficher les 3 histogrammes(voir Periode.py)
		week1 = week1
		week2 = week2
		duration = histoByChoice(self.subjects, self.Weeks, self.numberSubjects, self.fileTxt, self.fileT, week1, week2)
			
	def text_recap(self, week1, week2):
		txtRecap(self.subjects, self.secondWithCoeff, week1, week2, self.Weeks, self.fileTxt, self.fileT)

	def create_pdf(self):
		creationPdf(self.subjects, self.secondWithCoeff, self.Weeks, self.fileTxt, self.fileT)

class HistogramWindow:
	def __init__(self):
		self.hist = Histogram()

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
		self.hist.set_output_file(self.nameFile.get())
		self.repondre()


	def nbWeek(self):
		##active entry for futur histogram
		self.Wk1.configure(state='normal')
		self.Wk2.configure(state='normal')
		# nbw = 1

	def validate(self):
		##creation fichier texte et pdf
		##Creation de tuple
		
		##creation listes temps en fonction de matière et liste de matière (voir hourByYear.py)
		self.hist.create_by_week()
		self.hist.create_by_year()

		if(self.Wk1.get() and self.Wk2.get()):
			##Création PDF avec toutes les infos
			week1 = int(self.Wk1.get())
			week2 = int(self.Wk2.get())
			self.hist.create_by_choice(week1, week2)
			self.hist.text_recap(week1, week2)
		else:
			self.hist.text_recap(0, 0)

		self.hist.create_pdf()
		plt.show()
		

	def askOpenTxt(self):
		if not self.nameFile.get():
			return
		else : 
			## Creation file txt
			fileTxt, fileT = createTxt(nameFichier)
			return (fileTxt, fileT)

	def repondre(self):
		for i in range(int(self.Entree.get())):
			filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.ics'),('all files','.*')] and [('txt files','.txt'),('all files','.*')] )
			self.hist.add_file(filename)
	

#main()
win = HistogramWindow()