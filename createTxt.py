
	
def createTxt():
	print('Creating new text file') 
	fileTxt = input('Enter name of text file: ')+'.txt'
	file = open (fileTxt,'w')
	file.write ('salut mec\n')
	file.write('oho\n')

	file.close()
	file = open (fileTxt,'a')
	file.write("Hey\n")
	file.close()
	return(fileTxt)