#!/usr/bin/python3
import datetime
import calendar
#benoit

test="BEGIN:VENENT";
test2="END:VENENT"
chaine1="DTSTAMP";
deb="DTSTART";
Sum="SUMMARY";
loc="LOCATION";
p='PRIORITY'
fin="DTEND";
UID="UID";
end="END:VCALENDAR"
Sujet=[25];
Emplacement=[25];
j=0;
Type="";b="";Time=""
lignes,colonnes=10,9
lst=[];tab=0
ll=[]



def createTab(path):

	fichier=open(path, "r");
	Nb=0
	S0='';S1=''
	S=[]
	j=0;
	tab1=0
	tab=0
	for i in fichier:	#Rentre toutes les lignes du fichiers dans la variable S1	
		S1=S1+i
		
		Nb=i.count("BEGIN:VEVENT")+Nb;	#Permet de trouver le nombre de 'BEGIN:VEVENT'
	for l in S1: # Parcours le fichier et lui supprime ses sauts de lignes en space
		if l=='\n':
			l='\s';
		S0=S0+l

	for tab in range(Nb-1):
		lst.append([])
		ll.append([])
	#### Après avoir créer le tableau de la bonne taille par rapport au nombre de BEGIN:VEVENT#################
	##########Je Met n'importe quel fichier sous la forme d'une seule grande ligne qui peut être par la suite partitionné le nb de fois nécessaire pour récupérer les informations afin de remplir mon tableau###############
	a,b,c=S0.partition("BEGIN:VEVENT") 
	d,k,f=c.partition("END:VEVENT") #######Je coupe la première info entre BEGIN et END VEVENT que j'envoie ensuite dans la boucle###############
	for e in range (Nb-1):
		l1,b1,c1=f.partition("BEGIN:VEVENT")
		l2,b2,f=c1.partition('END:VEVENT')
		if 'Férié' in l2:  ################### Il es possible que certains jour soit férié et le tableau de cours ne doit pas en tenir compte
			lst[tab1].append("Férié")
			l1,b1,c1=f.partition("BEGIN:VEVENT")
			l2,b2,f=c1.partition('END:VEVENT')
			if len(f)<20 and 'END:VCALENDAR' in f:  ############### J'arrête la boucle si on trouve END:VCALENDAR
				break;
			tab1+=1
		
		else:
			a,c,T=l2.partition(deb)   ############## Je partitionne par rapport à DSTART pour récupérer les horraires
			if 'Paris' in l2:
				a,c,T=T.partition('Paris') ####Je vérifie la possibilité qu'il y ai Paris pour indiqué l'heure

			T=T[1:]
			Date,l,Time=T.partition('T') ############Récupération heure et date
			Tim=Time

			Time=Time[:6]
			Date2=','.join(Date)	#Range tous les caractères de la date dans une chîne de caractère séparé par une virgule
			Y=Date2[0]+Date2[2]+Date2[4]+Date2[6] #Associe uniquement les caractère qui nous intéresse modulo 2 car virgule
			M=Date2[8]+Date2[10]
			D=Date2[12]+Date2[14]
			Time2=','.join(Time) #Range tous les caractères de l'heure dans une chaîne de caractère séparé par une virgule
			H=Time2[0]+Time2[2]
			Min=Time2[4]+Time2[6]
			Jour1=datetime.datetime(int(Y),int(M),int(D),int(H),int(Min))
			j+=1;
			a,c,T=Tim.partition(fin)
			if 'Paris' in T:
				a,c,T=T.partition('Paris')		#########Même chose que vu ci-dessus pour l'heure de fin de cours
			Date,l,Time=T.partition('T')
			Date=Date[1:]
			Time=Time[:6]
			Date3=','.join(Date)#utilisation de partition pour récuperer chaîne de caractère placé dans une autre chaine de caractère séparé par des virgules
			Y1=Date3[0]+Date3[2]+Date3[4]+Date3[6]
			M1=Date3[8]+Date3[10]
			D1=Date3[12]+Date3[14]
			Time3=','.join(Time)
			H1=Time3[0]+Time3[2]
			Min1=Time3[4]+Time3[6]
			Jour2=datetime.datetime(int(Y1),int(M1),int(D1),int(H1),int(Min1))		#utilisation library datetime
			Duree=str(Jour2-Jour1)					#Différence d'une durée entre 2 jours à l'aide de datetime
			W=datetime.date(int(Y), int(M), int(D)).isocalendar()[1]
			W1=datetime.date(int(Y1), int(M1), int(D1)).isocalendar()[1]
			j+=1;
			if Tim.index(Sum) < Tim.index(loc):  ##########Certains fichiers dispose de SUMMARY avant LOCATION
				l3,b3,c3=Tim.partition(Sum)      ###########Coparaison utile pour savoir comment récupérer les informations
				g1,g2,g3=c3.partition(loc)
			else:
				l3,b3,c3=Tim.partition(Sum)
				g1,g2,g3=c3.partition(p)
			
			c3=c3[1:]
			if c3[:8]=='LANGUAGE':            #####Certains ont cette constante en plus je vérifie sa présence qui peut fausser la récupération d'infos
				d3,e3,f3=c3.partition(' ')
				Semestre=0
			else :
				Sujet,e3,f3=c3.partition(' ')

			if f3[:2]=='- ':
				f3=f3[2:]
				l4,b4,S4=f3.partition(' ')
				Sujet,l5,b5=S4.partition(' ')

			if Sujet=='Asservissements&Automatisme':
				Sujet='Auto';
			if Sujet=='SOUTENANCE':
				Type='SOUTENANCE';
				Semestre="Fin d'Année";
			if Sujet=='Eval':
				if 'Wims' in f3:
					Sujet='Eval Wims'
				
			Semestre,z,z1=f3.partition(' ')
			if 'S' not in Semestre:
				Semestre='0'
			if 'TD' in g1:
				Type='TD'
				ab=g1.index('TD');ab+=1;
				aa=1+ab
				while int(aa) <len(g1) and g1[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
					Type=Type+(g1[aa])
					aa+=1;
				a1=0;a2=1;a3=0;a4=0;
			elif 'Groupe' in g1:
				Type='TP'
				a1=1;a2=0;a3=0;a4=0;
			elif 'TP' in g1:
				Type='TP'
				ab=g1.index('TP');ab+=1;
				aa=1+ab
				while int(aa) <len(g1) and g1[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
					Type=Type+(g1[aa])
					aa+=1;
				a1=1;a2=0;a3=0;a4=0;
			elif 'SOUTENANCE' in g1:
				Type='SOUTENANCE'
				ab=g1.index('SOUTENANCE');ab+=1;
				aa=1+ab
				while int(aa) <len(g1) and g1[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
					Type=Type+(g1[aa])
					aa+=1;
				a1=0;a2=0;a3=0;a4=1;
			elif 'Cours' in g1:
				Type='Cours'
				ab=g1.index('Cours');ab+=1;
				aa=1+ab
				while int(aa) <len(g1) and g1[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
					Type=Type+(g1[aa])
					aa+=1;
				a1=0;a2=0;a3=1;a4=0;
			# if e6[:1].isnumeric==True:
			# 	Type=Type+e6[:1]
			# 	if e6[1:2].isnumeric==True:
			# 		Type=Type+e6[1:2]
			a5='0'
			j+=1;
			if j==3:
				lst[tab1].append(Sujet)
				lst[tab1].append(a3)
				lst[tab1].append(a2)
				lst[tab1].append(a1)
				lst[tab1].append(a4)
				lst[tab1].append(a5)
				lst[tab1].append(str(Jour1.date()))
				lst[tab1].append(Duree)
				lst[tab1].append(W)
				lst[tab1].append(Semestre)
				tab1+=1;
				a5=0
			
			j=0;
	return(lst)
	fichier.close();
	# Jour1=0
	# Jour2=0
	# fichier=open("Fichier_Gpu/EPU.ics", "r");
	# Nb=0
	# S0='';S1=''
	# S=[]
	# tab=0
	# j=0;
	# for i in fichier:	#Rentre toutes les lignes du fichiers dans la variable S1	
	# 	S1=S1+i
	# 	Nb=i.count("BEGIN:VEVENT")+Nb;	#Permet de trouver le nombre de 'BEGIN:VEVENT'
		
	# for l in S1: # Parcours le fichier et lui supprime ses sauts de lignes en space
	# 	if l=='\n':
	# 		l='\s';
	# 	S0=S0+l

	# for tab in range(Nb-3):
	# 	lst.append([])
	# 	ll.append([])

	# a,b,c=S0.partition("BEGIN:VEVENT")
	# d,k,f=c.partition("END:VEVENT")
	# for e in range (Nb-1):
	# 	l1,b1,c1=f.partition("BEGIN:VEVENT")
	# 	l2,b2,f=c1.partition('END:VEVENT')
	# 	if 'Férié' in l2:
	# 		lst[tab1].append("Férié")
	# 		l1,b1,c1=f.partition("BEGIN:VEVENT")
	# 		l2,b2,f=c1.partition('END:VEVENT')
	# 		if len(f)<20 and 'END:VCALENDAR' in f:
	# 			break;
	# 		tab1+=1
		
	# 	else:
	# 		a,c,T=l2.partition(deb)
	# 		if 'Paris' in l2:
	# 			a,c,T=T.partition('Paris')

	# 		T=T[1:]
	# 		Date,l,Time=T.partition('T')
	# 		Tim=Time
	# 		Time=Time[:6]
	# 		# print(Time)
	# 		Date2=','.join(Date)	#Range tous les caractères de la date dans une chîne de caractère séparé par une virgule
	# 		Y=Date2[0]+Date2[2]+Date2[4]+Date2[6] #Associe uniquement les caractère qui nous intéresse modulo 2 car virgule
	# 		M=Date2[8]+Date2[10]
	# 		D=Date2[12]+Date2[14]
	# 		Time2=','.join(Time) #Range tous les caractères de l'heure dans une chaîne de caractère séparé par une virgule
	# 		H=Time2[0]+Time2[2]
	# 		Min=Time2[4]+Time2[6]
	# 		Jour1=datetime.datetime(int(Y),int(M),int(D),int(H),int(Min))
	# 		j+=1;
	# 		a,c,T=Tim.partition(fin)
	# 		if 'Paris' in T:
	# 			a,c,T=T.partition('Paris')		
	# 		Date,l,Time=T.partition('T')
	# 		Date=Date[1:]
	# 		Time=Time[:6]
	# 		# print(Time)
	# 		Date3=','.join(Date)#utilisation de partition pour récuperer chaîne de caractère placé dans une autre chaine de caractère séparé par des virgules
	# 		Y1=Date3[0]+Date3[2]+Date3[4]+Date3[6]
	# 		M1=Date3[8]+Date3[10]
	# 		D1=Date3[12]+Date3[14]
	# 		Time3=','.join(Time)
	# 		H1=Time3[0]+Time3[2]
	# 		Min1=Time3[4]+Time3[6]
	# 		Jour2=datetime.datetime(int(Y1),int(M1),int(D1),int(H1),int(Min1))		#utilisation library datetime
	# 		Duree=str(Jour2-Jour1)					#Différence d'une durée entre 2 jours à l'aide de datetime
	# 		W=datetime.date(int(Y), int(M), int(D)).isocalendar()[1]
	# 		W1=datetime.date(int(Y1), int(M1), int(D1)).isocalendar()[1]
	# 		j+=1;
	# 		if Tim.index(Sum) < Tim.index(loc):
	# 			l3,b3,c3=Tim.partition(Sum)
	# 			g1,g2,g3=c3.partition(loc)
	# 		else:
	# 			l3,b3,c3=Tim.partition(Sum)
	# 			g1,g2,g3=c3.partition(p)
			
	# 		c3=c3[1:]
	# 		if c3[:8]=='LANGUAGE':
	# 			d3,e3,f3=c3.partition(' ')
	# 			Semestre=0
	# 		else :
	# 			Sujet,e3,f3=c3.partition(' ')

	# 		if f3[:2]=='- ':
	# 			f3=f3[2:]
	# 			l4,b4,S4=f3.partition(' ')
	# 			Sujet,l5,b5=S4.partition(' ')

	# 		if Sujet=='Asservissements&Automatisme':
	# 			Sujet='Auto';
	# 		if Sujet=='SOUTENANCE':
	# 			Type='SOUTENANCE';
	# 			Semestre="Fin d'Année";

	# 		Semestre,z,z1=f3.partition(' ')
	# 		if 'S' not in Semestre:
	# 			Semestre='0'
	# 		if 'TD' in g1:
	# 			Type='TD'
	# 			ab=g1.index('TD');ab+=1;
	# 			aa=1+ab
	# 			while int(aa) <len(g1) and g1[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
	# 				Type=Type+(g1[aa])
	# 				aa+=1;
	# 			a1=0;a2=1;a3=0;a4=0;
	# 		elif 'Groupe' in g1:
	# 			Type='TP'
	# 			a1=1;a2=0;a3=0;a4=0;
	# 		elif 'TP' in g1:
	# 			Type='TP'
	# 			ab=g1.index('TP');ab+=1;
	# 			aa=1+ab
	# 			while int(aa) <len(g1) and g1[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
	# 				Type=Type+(g1[aa])
	# 				aa+=1;
	# 			a1=1;a2=0;a3=0;a4=0;
	# 		elif 'SOUTENANCE' in g1:
	# 			Type='SOUTENANCE'
	# 			ab=g1.index('SOUTENANCE');ab+=1;
	# 			aa=1+ab
	# 			while int(aa) <len(g1) and g1[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
	# 				Type=Type+(g1[aa])
	# 				aa+=1;
	# 			a1=0;a2=0;a3=0;a4=1;
	# 		elif 'Cours' in g1:
	# 			Type='Cours'
	# 			ab=g1.index('Cours');ab+=1;
	# 			aa=1+ab
	# 			while int(aa) <len(g1) and g1[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
	# 				Type=Type+(g1[aa])
	# 				aa+=1;
	# 			a1=0;a2=0;a3=1;a4=0;
	# 		a5='0'
	# 		j+=1;
	# 		if j==3:
	# 			lst[tab1].append(Sujet)
	# 			lst[tab1].append(a3)
	# 			lst[tab1].append(a2)
	# 			lst[tab1].append(a1)
	# 			lst[tab1].append(a4)
	# 			lst[tab1].append(a5)
	# 			lst[tab1].append(str(Jour1.date()))
	# 			lst[tab1].append(Duree)
	# 			lst[tab1].append(W)
	# 			lst[tab1].append(Semestre)
	# 			tab1+=1;
	# 			a5=0
			
	# 		j=0;
	
	# return(lst)
	# fichier.close();

