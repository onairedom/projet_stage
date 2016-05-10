import os
	
def createTxt(fileT):
	print('Creating new text file') 
	fileTxt = fileT+'.txt'
	print(fileTxt)
	file = open (fileTxt,'w')
	file.write('oho\n')
	fileT,g,g1=fileTxt.partition('.')
	file.close()
	file = open (fileTxt,'a')
	file.write("Hey\n")
	file.close()
	return(fileTxt,fileT)
