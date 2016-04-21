#!/usr/bin/python3
import datetime
import calendar


test="BEGIN:VENENT";
test2="END:VENENT"
chaine1="DTSTAMP";
deb="DTSTART";
Sum="SUMMARY";
loc="LOCATION";
fin="DTEND";
UID="UID";
end="END:VCALENDAR"
Sujet=[25];
Emplacement=[25];
j=0;
Type="";b="";Time=""
lignes,colonnes=10,9
lst=[];tab=0



fichier=open("Fichier_Gpu/UPU.ics", "r");
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

for tab in range(Nb):
	lst.append([])



a,b,c=S0.partition("BEGIN:VEVENT")
d,k,f=c.partition("END:VEVENT")
for e in range (Nb-3):
	l1,b1,c1=f.partition("BEGIN:VEVENT")
	l2,b2,f=c1.partition('END:VEVENT')
	if 'Férié' in l2:
		lst[tab1].append("Férié")
		print(f)
		l1,b1,c1=f.partition("BEGIN:VEVENT")
		l2,b2,f=c1.partition('END:VEVENT')
		print('salut',f)
		tab1+=1
	elif f==' \sEND:VCALENDAR\s':
		break;
	else:
		a,c,T=l2.partition(deb)
		T=T[1:]
		Date,l,Time=T.partition('T')
		Tim=Time
		Time=Time[:6]
		Date2=','.join(Date)	#Range tous les caractères de la date dans une chîne de caractère séparé par une virgule
		print(Time)
		Y=Date2[0]+Date2[2]+Date2[4]+Date2[6] #Associe uniquement les caractère qui nous intéresse modulo 2 car virgule
		M=Date2[8]+Date2[10]
		D=Date2[12]+Date2[14]
		Time2=','.join(Time) #Range tous les caractères de l'heure dans une chaîne de caractère séparé par une virgule
		H=Time2[0]+Time2[2]
		Min=Time2[4]+Time2[6]
		Jour1=datetime.datetime(int(Y),int(M),int(D),int(H),int(Min))
		j+=1;
		a,c,T=Tim.partition(fin)
		Time=Tim		
		Date,l,Time=T.partition('T')		#utilisation de partition pour récuperer chaîne de caractère placé dans une autre chaine de caractère séparé par des virgules
		Date=Date[1:]
		Time=Time[:6]
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
		l3,b3,c3=Tim.partition(Sum)
		print("VOILA PK",Tim)
		c3=c3[1:]
		if c3[:8]=='LANGUAGE':
			d3,e3,f3=c3.partition(' ')
			Semestre=0
		if f3[:2]=='- ':
			f3=f3[2:]
		l4,b4,S4=f3.partition(' ')
		Sujet,l5,b5=S4.partition(' ')

		if Sujet=='Asservissements&Automatisme':
			Sujet='Auto';
		if 'TD' in Tim:
			d6,Type,e6=b5.partition('TD')
			a1=0;a2=1;a3=0;a4=0;
		elif 'TP' in Tim:
			d6,Type,e6=b5.partition('TP')
			a1=1;a2=0;a3=0;a4=0;
		elif 'SOUTENANCE' in Tim:
			d6,Type,e6=b5.partition('SOUTENANCE')
			a1=0;a2=0;a3=0;a4=1;
		elif 'Cours' in Tim:
			d6,Type,e6=b5.partition('Cours')
			a1=0;a2=0;a3=1;a4=0;
		if e6[:1].isnumeric==True:
			Type=Type+e6[:1]
			if e6[1:2].isnumeric==True:
				Type=Type+e6[1:2]
		a5=' '
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
print(lst)