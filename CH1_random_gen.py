import random
def get_int(msg,minimum,default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None :# if no input msg && default is not none
                return default

            i = int(line) # turn the input to integer
            if i<minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)



rows = get_int("rows:", 1, None)
columns = get_int("columns:", 1 , None)
minimum = get_int("minimum(Or Enter to 0 ):",-100000,0)
default = 1000
if default < minimum:
    default = 2*minimum

maximum = get_int("maximum(Enter for " + str(default) + "):", minimum,default)


row = 0
while row < rows:
    line=""
    column = 0
    while column < columns:
        i = random.randint(minimum,maximum)
        s = str(i) # turn into string for output format
        while len(s)<10:
            s = " "+s
        line += s # print out whole row
        column +=1
    print(line)
    row +=1



