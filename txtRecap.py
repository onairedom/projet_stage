from pylab import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pylab as plt

def txtRecap(subjects, secondWithCoeff, duration, week1, week2, Weeks, fileTxt):
	Hour=[]; cptSemaine=0;wcpt='';cptH=0
	file = open (fileTxt,'a')
	for i in range(len(secondWithCoeff)):
		Hour.append([])
		Hour[i]=float(secondWithCoeff[i]/3600)

	cpt=0
	for subject in subjects:
		print ("Dans l'année vous avez", Hour[cpt], "H de", subject)
		file.write("Dans l'année vous avez "+str(Hour[cpt])+ " H de "+ str(subject)+"\n")
		cpt+=1;
	
	for week in range(len(Weeks)):
		if week==0:
			wcpt=Weeks[week][0]
		if Weeks[week][0]>=week1 and Weeks[week][0]<=week2:
			cptH=1
			for subject in subjects:
				if Weeks[week][cptH]!=0:
					print("Dans la semaine", Weeks[week][0],"Vous avez eu", Weeks[week][cptH],"H de", subject)
					file.write("Dans la semaine "+str(Weeks[week][0])+" Vous avez eu "+ str(Weeks[week][cptH])+" H de "+str(subject)+'\n')
					cptSemaine = cptSemaine + Weeks[week][cptH] 
				cptH+=1
			if cptSemaine != 0 :
				print("Cette Semaine vous avez fait", cptSemaine)
				file.write("Dans la semaine "+str(Weeks[week][0])+ "vous avez eu "+str(cptSemaine)+' H\n')
			cptSemaine=0
		elif week2<week1:
			if Weeks[week][0]>=week1 and Weeks[week][0]<=52:
				cptH=1
				for subject in subjects:
					if Weeks[week][cptH]!=0:
						print("Dans la semaine", Weeks[week][0],"Vous avez eu", Weeks[week][cptH],"H de", subject)
						file.write("Dans la semaine "+ str(Weeks[week][0])+" Vous avez eu "+ str(Weeks[week][cptH])+" H de "+subject+"\n")
						cptSemaine = cptSemaine + Weeks[week][cptH] 
					cptH+=1
				if cptSemaine !=0:
					print("Cette Semaine vous avez fait", cptSemaine)
					file.write("Dans la semaine "+str(Weeks[week][0])+ "vous avez eu "+str(cptSemaine)+' H\n')
				cptSemaine=0
			if Weeks[week][0]==53:
				Weeks[week][0]=0;

			elif Weeks[week][0]>0 and Weeks[week][0]<=week2:
				cptH=1
				for subject in subjects:
					if Weeks[week][cptH]!=0:
						print("Dans la semaine", Weeks[week][0],"Vous avez eu", Weeks[week][cptH],"H de", subject)
						file.write("Dans la semaine "+ str(Weeks[week][0])+" Vous avez eu "+str(Weeks[week][cptH])+" H de "+ subject+"\n")
						cptSemaine = cptSemaine + Weeks[week][cptH] 
					cptH+=1
				if cptSemaine!=0:
					print("Cette Semaine vous avez fait", cptSemaine)
					file.write("Dans la semaine "+str(Weeks[week][0])+ "vous avez eu "+str(cptSemaine)+' H\n')
				cptSemaine=0
	file.close()

	plt.show()