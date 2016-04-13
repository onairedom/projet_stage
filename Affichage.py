#!/usr/bin/python3
from prog15 import tableau
import datetime
import time
import calendar
import matplotlib.pyplot as plt

lst=tableau()

M=""
j=0
print("Le tableau est composé de", len(lst),"lignes et dispose donc de",(len(lst)*9),"élément")

# print("Si vous êtes intéressé par info1 tapez i")
# print("OL1 tapez O")
# print("Ma1 tapez M")
# print("Au3 Tapez A")


# Demande=input("Quel cours avez vous choisis?")
# switcher ={
# 	'A' or 'a': 
# }
M='Info1'
N='Ma1'
O='Au3'
P='DS'
L='Eval Wims'
Q='AM2'
R='SOUTENANCE'


cours1=0;cours2=0;cours3=0;cours4=0;cours5=0;cours6=0;cours7=0;cours8=0;

# print(lst)
# j=0;i=0;k=0;
# nb=[]
# cours=[]

# for i in range(len(lst)):
# 	nb.append([0]);
# 	cours.append([])

# for cpt in lst:
# 	test=cpt[0]
# 	cours[k]=test;
# 	k+=1;
# print("first",cours[0])
# test=cours[0]
# print(len(cours))
# print(cours)
# k=0

# indices=[i for i,x in enumerate(cours) if x==test]
# print (indices)


# i=0
# for i in range(j):
# 	print(cours[i])


k=0;Heure=0;Min=0
recap=[];hour=[]
j=0
var=""
for i in lst:
	if lst[k][0] not in recap:
		recap.append(lst[k][0])
	k+=1
print(recap)
k=0
for i in recap:
	for e in lst:
		for j in e:
			if i==j:
				print(e[6])
				t1=datetime.time(e[6]) # Pensez a utilise ce qui es fait ligne 90-100 pour extraire heure,min,sec et pouvoir faire datetime.time(h,min,sec)
			k+=1
# while j<(len(lst)):
# 	if lst[j][0]!=var:
		
				
# 	else:
# 		j+=1;
# print(Min2)
# print(k)	

# var=lst[j][0]Pour heure sans datetime
# for i in lst :
# 	if i[0]==var:
# 		Hour=','.join(i[6])
# 		H=Hour[0]
# 		if Hour[2].isnumeric()==True:
# 			H=Hour[0]+Hour[2]
# 		if Hour[6].isnumeric()==True and Hour[4].isnumeric()==True:
# 			M=Hour[4]+Hour[6]
# 		else:
# 			M=Hour[6]+Hour[8]
# 		H=int(H)
# 		k=int(H+k)
# 		M=int(M)
# 		Min=int(Min+M)
# 		Min2=Min%60
# 		hsup=Min//60
# 		k=k+hsup			

# print(var,k,"H",Min2,"min")
		


