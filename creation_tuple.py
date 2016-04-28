from createTab import *

# APPEND TUPLE VERSION
def tuple1(lst):
	# init tuple
	tup = ()
	
	# fill tuple
	for list_element in lst:
		# transform list element in tuple element
		tup = tup + (tuple(list_element),)

	return tup
