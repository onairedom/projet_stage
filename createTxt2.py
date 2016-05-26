import os
	
def createTxt(fileT):
	fileTxt = fileT+'.txt'
	file = open (fileTxt,'w')
	fileT,g,g1=fileTxt.partition('.')
	file.close()
	file = open (fileTxt,'a')
	file.close()
	return(fileTxt,fileT)
