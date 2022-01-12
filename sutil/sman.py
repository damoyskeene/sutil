import collections 

def bw(letter, list):
	le =  letter

	exi = [i for i in list if i.lower().startswith(le.lower())]
	return exi 

def compare(x,y):
	if(x == y):
		return "True"
	else: 
		return "False"



