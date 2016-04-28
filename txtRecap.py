from pylab import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pylab as plt

def txtRecap(subjects, secondWithCoeff, duration, week1, week2, Weeks):
	Hour=[]; cptSemaine=0;wcpt='';cptH=0
	for i in range(len(secondWithCoeff)):
		Hour.append([])
		Hour[i]=float(secondWithCoeff[i]/3600)

	cpt=0
	for subject in subjects:
		print ("Dans l'année vous avez", Hour[cpt], "H de", subject)
		cpt+=1;
	
	for week in range(len(Weeks)):
		if week==0:
			wcpt=Weeks[week][0]

		# print(week)
		# print(Weeks[week][0])
		if Weeks[week][0]>=week1 and Weeks[week][0]<=week2:
			cptH=1
			for subject in subjects:
				if Weeks[week][cptH]!=0:
					print("Dans la semaine", Weeks[week][0],"Vous avez eu", Weeks[week][cptH],"H de", subject)
					cptSemaine = cptSemaine + Weeks[week][cptH] 
				cptH+=1
			if cptSemaine != 0 :
				print("Cette Semaine vous avez fait", cptSemaine)
			cptSemaine=0
		elif week2<week1:
			if Weeks[week][0]>=week1 and Weeks[week][0]<=52:
				cptH=1
				for subject in subjects:
					if Weeks[week][cptH]!=0:
						print("Dans la semaine", Weeks[week][0],"Vous avez eu", Weeks[week][cptH],"H de", subject)
						cptSemaine = cptSemaine + Weeks[week][cptH] 
					cptH+=1
				if cptSemaine !=0:
					print("Cette Semaine vous avez fait", cptSemaine)
				cptSemaine=0
			if Weeks[week][0]==53:
				Weeks[week][0]=0;

			elif Weeks[week][0]>0 and Weeks[week][0]<=week2:
				cptH=1
				for subject in subjects:
					if Weeks[week][cptH]!=0:
						print("Dans la semaine", Weeks[week][0],"Vous avez eu", Weeks[week][cptH],"H de", subject)
						cptSemaine = cptSemaine + Weeks[week][cptH] 
					cptH+=1
				if cptSemaine!=0:
					print("Cette Semaine vous avez fait", cptSemaine)
				cptSemaine=0


	plt.show()