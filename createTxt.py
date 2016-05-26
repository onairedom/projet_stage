import os
	
def createTxt():
	print('Creating new text file') 
	fileTxt = input('Enter name of text file: ')+'.txt'
	file = open (fileTxt,'w')
	fileT,g,g1=fileTxt.partition('.')
	file.close()
	file = open (fileTxt,'a')
	file.close()
	return(fileTxt,fileT)


