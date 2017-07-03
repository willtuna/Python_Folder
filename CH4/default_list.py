def append_if(x, lst = None):
     if lst == None:
             lst = []
     if x %2 == 0:
             lst.append(x)
     return lst

def append_if2(x,lst = []):
	if x % 2 == 0:
		lst = [x]# this always assign a new list to local variable lst, it would be clear when function is finished
	return lst

def append_if3(x,lst = []):
	if x % 2 ==0:
		lst.append(x) # since every time the function run, it always append the default lst, so the default lst would aggregate
	return lst


x = append_if2(2)
print(x)
y = append_if2(3)
print(y)