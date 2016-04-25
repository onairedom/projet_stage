from prog16 import tableau


def tuple1():

	lst=tableau()
	o=0;
	for i in lst:
		lst[o]=tuple(lst[o])
		# print(lst[o])
		o+=1
	lst=(tuple(lst))
	return(lst)
