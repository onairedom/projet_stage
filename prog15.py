#!/usr/bin/python3
import datetime
import calendar

def tableau():

	test="BEGIN:VENENT";
	test2="END:VENENT"
	chaine1="DTSTAMP";
	deb="DTSTART;";
	Sum="SUMMARY";
	loc="LOCATION";
	fin="DTEND;";
	UID="UID";
	end="END:VCALENDAR"
	Sujet=[25];
	Emplacement=[25];
	Heure1=Heure2=[25];
	j=0;
	Type="";b=""
	lignes,colonnes=10,9
	lst=[];tab=0

	a2=0;a1=0;i=0;a3=0;a4=0;a5=0;e=0

	tab1=0
	fichier=open("Fichier_Gpu/gpu.txt", "r");
	for i in fichier:			
		Nb=i.count("BEGIN:VEVENT");	#Permet de trouver le nombre de 'BEGIN:VEVENT'
		print(Nb)
		for tab in range(Nb-1):
			lst.append([])
		a,b,c=i.partition("BEGIN:VEVENT")
		d,k,f=c.partition("END:VEVENT")	#Sépare les caractères entre BEGIN:VEVENT et END:VEVENT
		for e in range (Nb):
			
			a,b,c=f.partition("BEGIN:VEVENT")
			d,k,f=c.partition("END:VEVENT")
			if deb in d:
				a,c,T=d.partition('Paris:')
				Date,l,Time=T.partition('T')			
				Date2=','.join(Date)		#Range tous les caractères de la date dans une chîne de caractère séparé par une virgule
				Y=Date2[0]+Date2[2]+Date2[4]+Date2[6] #Associe uniquement les caractère qui nous intéresse modulo 2 car virgule
				M=Date2[8]+Date2[10]
				D=Date2[12]+Date2[14]
				Time2=','.join(Time) #Range tous les caractères de l'heure dans une chaîne de caractère séparé par une virgule
				H=Time2[0]+Time2[2]
				Min=Time2[4]+Time2[6]
				Jour1=datetime.datetime(int(Y),int(M),int(D),int(H),int(Min))
				j+=1;	#incrémentation de j pour valider la création de la ligne
			if fin in d:
				a,c,T=d.partition("DTEND;TZID=Europe/Paris:")
				Date,l,Time=T.partition('T')		#utilisation de partition pour récuperer chaîne de caractère placé dans une autre chaine de caractère séparé par des virgules
				Date3=','.join(Date)
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
			if Sum in d:
				a,temp,b = d.partition('SUMMARY:')
				Sujet,temp1,b1 = b.partition(' ')

				if ' _TD' in b:
					a1=0;a2=0;a3=0;a4=0;a5='_TD'
							
				if Sujet=='SOUTENANCE':
					Type='SOUTENANCE';
					Semestre="Fin d'Année";
				elif Sujet=='Eval':
					temp,Suj,b1=b.partition('Eval Wims ')
					S=Suj.split(' ')
					Sujet=S[0]+' '+S[1]
					Semestre,d,b2=b1.partition(' ')
					Type,p,z=b2.partition(' ')
				else :
					Semestre,d,b2=b1.partition(' ')
					g,h,T=b2.partition(' PRIORITY')
					k,l,Type=g.partition(' ')
					g.split(' ')

				if 'TP' in g:					#Recherche chaîne de caractère tp pour ensuite vérifier le nombre de chiffre qui suivent et l'ajouter dans la variable adequate
					Type='TP';
					a=g.index('TP');a+=1;
					aa=1+a
					while int(aa) <len(g) and g[aa].isnumeric()==True :		#ajoute des caractère dans la chaine en question tant qu'on es moins long que la chaine de caractère et que l'on a encore des chiffre par la suite
						Type=Type+(g[aa])
						aa+=1;
					a1=1;a2=0;a3=0;a4=0;
				elif 'TD' in g:
					Type='TD'
					a=g.index('TD');a+=1;
					aa=1+a
					while int(aa) <len(g) and g[aa].isnumeric()==True :
						Type=Type+(g[aa])
						aa+=1;
					a1=0;a2=1;a3=0;a4=0;
				elif 'Cours' in g:
					Type='Cours'
					a=g.index('Cours');a+=4;
					aa=1+a
					while int(aa) <len(g) and g[aa].isnumeric()==True :
						Type=Type+(g[aa])
						aa+=1;
					a1=0;a2=0;a3=1;a4=0;

				elif 'SOUTENANCE' in g:
					a1=0;a2=0;a3=0;a4=1;
				
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
	fichier.close()



