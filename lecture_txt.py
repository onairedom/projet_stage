#!/usr/bin/python3
import datetime
import calendar
#import numpy as np


test="BEGIN:VENENT";
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
Type=""
lignes,colonnes=10,9
lst=[]
a2=0;
a1=0;
i=0;
a3=0;
a4=0;
fichier=open("/home/clementperrousset/Documents/Fichier_Gpu/gpu2.txt", "r");

i= [line.rstrip('\n') for line in fichier]


for p in i :

	print (p);
	if deb==i:
		print("je suis la");
		a,c,T=i.partition('Paris:')
		Date,l,Time=T.partition('T')
		Date2=','.join(Date)
		Y=Date2[0]+Date2[2]+Date2[4]+Date2[6]
		M=Date2[8]+Date2[10]
		D=Date2[12]+Date2[14]
		Time2=','.join(Time)
		H=Time2[0]+Time2[2]
		Min=Time2[4]+Time2[6]
		Jour1=datetime.datetime(int(Y),int(M),int(D),int(H),int(Min))
		j+=1;	
	if fin==i:
		a,c,T=i.partition("Paris:")
		Date,l,Time=T.partition('T')
		Date3=','.join(Date)
		Y1=Date3[0]+Date3[2]+Date3[4]+Date3[6]
		M1=Date3[8]+Date3[10]
		D1=Date3[12]+Date3[14]
		Time3=','.join(Time)
		H1=Time3[0]+Time3[2]
		Min1=Time3[4]+Time3[6]
		Jour2=datetime.datetime(int(Y1),int(M1),int(D1),int(H1),int(Min1))
		Duree=str(Jour2-Jour1)
		W=datetime.date(int(Y), int(M), int(D)).isocalendar()[1]
		W1=datetime.date(int(Y1), int(M1), int(D1)).isocalendar()[1]
		j+=1;
	if loc==i:
		a,b,Emplacement=i.partition(':')
		j+=1;
		
	if Sum in i:
		a,temp,b = i.partition(':')
		Sujet,temp1,b1 = b.partition(' ')
		Semestre,d,b2=b1.partition(' ')
		g,h,T=b2.partition(' ')
		Type,k,l=T.partition(' ')
		if Type in ("TP1","TP2","TP3","TP4","TP5","TP6","TP7","TP8","TP9"):
			a1=1;
			a2=0;
			a3=0;
			a4=0;
		elif Type in ("TD1","TD2","TD3","TD4","TD5","TD6","TD7","TD8","TD9"):
			a1=0;
			a2=1;
			a3=0;
			a4=0;
		elif Type in ("Cours1","Cours2","Cours3","Cours4","Cours5","Cours6","Cours7","Cours8","Cours9"):
		
			a1=0;
			a2=0;
			a3=1;
			a4=0;
		elif Type=='Soutenances':
			
			a1=0;
			a2=0;
			a3=0;
			a4=1;
		j+=1;


	if j==4:
		
		lst+=([Sujet,a2,a1,a3,a4,str(Jour1.date()),Duree,W,Semestre])
		j=0;

"""print(lst[0][0][0][0][1][5])
print(lst.count('Info1'))"""
print("c'est moi",lst)

fichier.close();


