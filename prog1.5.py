#!/usr/bin/python3
import datetime
import calendar
#import numpy as np



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
Type=""
lignes,colonnes=10,9
lst=[]
a2=0;
a1=0;
i=0;
a3=0;
a4=0;
b=""
e=0

fichier=open("/home/clementperrousset/Documents/Fichier_Gpu/gpu.txt", "r");
for i in fichier:
	Nb=i.count("BEGIN:VEVENT");
	a,b,c=i.partition("BEGIN:VEVENT")
	d,k,f=c.partition("END:VEVENT")
	for e in range (Nb):
		
		a,b,c=f.partition("BEGIN:VEVENT")
		d,k,f=c.partition("END:VEVENT")
		if deb in d:
			a,c,T=d.partition('Paris:')
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
		if fin in d:
			a,c,T=d.partition("DTEND;TZID=Europe/Paris:")
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
		if loc in d:
			a,b,Emplacement=d.partition(':')
			j+=1;
			
		if Sum in d:
			a,temp,b = d.partition('SUMMARY:')
			Sujet,temp1,b1 = b.partition(' ')
			if Sujet=='SOUTENANCE':
				Type='SOUTENANCE';
				Semestre="Fin d'Année";
			elif Sujet=='Eval':
				temp,Sujet,b1=b.partition('Eval Wims ')
				Semestre,d,b2=b1.partition(' ')
				Type,p,z=b2.partition(' ')

			else :
				Semestre,d,b2=b1.partition(' ')
				g,h,T=b2.partition(' PRIORITY')
				k,l,Type=g.partition(' ')
				g.split(' ')
			if 'TP' in g:
				Type='TP';
				a=g.index('TP');a+=1;
				aa=1+a
				while int(aa) <len(g) and g[aa].isnumeric()==True :
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
				a1=0;a2=1;a3=0;a4=0;

			elif 'SOUTENANCE' in g:
				a1=0;a2=0;a3=0;a4=1;
			j+=1;
		if j==4:
			lst=lst,[Sujet,a2,a1,a3,a4,str(Jour1.date()),Duree,W,Semestre]
			j=0;


# M=""

# print("Le tableau est composé de", len(lst),"chaque colonnes dispose donc de",(len(lst)/9))
# """
# print("Si vous êtes intéressé par info1 tapez i")
# print("OL1 tapez O")
# print("Ma1 tapez M")
# print("Au3 Tapez A")

# Demande=input("Quel cours avez vous choisis?")
# switcher ={
# 	'A' or 'a': 
# }"""
# M='Info1'
# N='Ma1'
# O='Au3'
# P='DS'
# L='Eval Wims'
# Q='AM2'
# R='SOUTENANCE'
# cours1=0;cours2=0;cours3=0;cours4=0;cours5=0;cours6=0;
# for cpt in lst:
# 	if j%9==0:
# 		if lst[j]==M:
# 			cours1+=1
# 			Cours1=lst[j]
# 		elif lst[j]==N:
# 			cours2+=1
# 			Cours2=lst[j]
# 		elif lst[j]==O:
# 			cours3+=1
# 			Cours3=lst[j]
# 		elif lst[j]==P:
# 			cours4+=1
# 			Cours4=lst[j]
# 		elif lst[j]==L:
# 			cours4+=1
# 			Cours4=lst[j]
# 		elif lst[j]==Q:
# 			cours5+=1
# 			Cours5=lst[j]
# 		elif lst[j]==R:
# 			cours6+=1
# 			Cours6=lst[j]
# 	j+=1

# print("Vous avez dans l'année",cours1,"H de",Cours1)
# print("Vous avez dans l'année",cours2,"H de",Cours2)
# print("Vous avez dans l'année",cours3,"H de",Cours3)
# print("Vous avez dans l'année",cours4,"H de",Cours4)
# print("Vous avez dans l'année",cours5,"H de",Cours5)
# print("Vous avez dans l'année",cours6,"H de",Cours6)
print(lst)
fichier.close();


