#! /usr/bin/env python3

import sys;

# partition practice
s = "/home/willvegapunk/Programming/Python3"

result = s.rpartition("/")

print(result)


# endswith()
filename = sys.argv[1]
if filename.lower().endswith((".jpg",".jpeg")):
    print(filename,"is a JPEG image")
#strip()
afterstrip = "(How are you) I am will".strip("()")
print(afterstrip)


print(  (afterstrip.replace("(","")).replace(")","") )



record = "Leo Tolstoy*1828-8-28*1910-11-20"

fields = record.split("*")
born = fields[1].split("-")
death = fields[2].split("-")
print("Name:",fields[0],"Lived ",int(death[0])-int(born[0]),"years","from",born,"to",death)


#format
x = "three"
s = "{0} {1} {2}"
print(s.format("The",x,"tops"))

"{who} turned {year} this year".format(who="she",year="23")
d = dict(animal="elephant", weight = 12000)
print("The {0[animal]} weighs {0[weight]}kg ".format(d))

print("{}{}{}".format("python","can","count"))

print("x is {x}, s is {s}".format(**locals()))

print("{animal} and {weight}".format(**d))

#we call {0} {1} {2} the replacement field

#format specification


print("{0:*^25}".format(x))

maxwidth = 100
print("{0}".format(s[:maxwidth]))
print("{0[0]:#^0{1}}".format(fields,maxwidth))




