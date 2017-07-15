# Logical Operator
## Identity Operator
###Example:  is operator
a = ["Retention",3,None]#None is the built-in null object
b = ["Retention",3,None]
print('list comparison using is operator:',a is b)
# it will return False , since is operator only check whether two object reference referring to the same object
# with the same memory address. The example above are two distinct list object with the same value insdie
###Try is operator in str or int type
a = "Hello World"
b = 'Hello World'
print("str comparison using is operator with 'mutiple str':",a is b)
a = "Hello"
b = "Hello"
print('str comparison using is operator with "single str":',a is b)
# is comparison is not good to compare string since it depends on different python implemented inside

# Pratically we use 
#>> is None 
#>> is not None
#to check whether the object reference exist or not

# To solve above problem, we could use == != operator

print('str comparison using == operator with "single str":',a == b)


#Membership Operator   :  in
tuple_p = ('frog',1,2,'lion')
print("Is frog in tuple_p? :",'frog' in tuple_p)
print("dog is not in tuple_p ?:", "dog" not in tuple_p)

phrase = "Hello Vegapunk"
print('Is "Vega" in  Hello Vegapunk','Vega' in phrase)

# In python character is a string with length 1
# The membership operator can be used to test the substring of any length



# Logical Operator:   and   or   not
# In python's world the logical operator return the value of the object reference by default 
# so in many cases it didn't return the boolean value Ture or False
# And the logical operator also have the short-circuit logic 
five = 5
two = 2
print(five and two)# it would show up 2
print(two or five)# it would show up 2 because of short-circuit 

#  not operator would only return the boolean value   True  or False
print(not two) # it would return false





#if else in Python
lines = 5000
if lines < 1000:
    print('smaller than 1000')
elif lines < 10000:
    print('Between 1000 ~ 10000')
else:
    print('Larger than 10000')
    
#the indentation is officially 4 space for the block suite
# colon(:)  is used for indicating the suite
#pass is a function do nothing in the block (in Python the block means the suite)



list_1 = [1,2,3,4,5]
#while loop
i = 1
while True:
    item = list_1[i]
    if item == 5:
        print("Find item == 5 and break")
        break
    i = i+1



#  for loop usage

for country in ["Denmark","Taiwan","China","the USA"]:
    print(country)

countries = ["UK","Canada","Australia","Japan"]
for country in countries:
    print(country)

# above example show that country is actually a iteratable that would iterate in the collection data types




#Exception Handling
s = input("Enter an integer :")

try:
    i = int(s)
    print("Valid integer entered:", i )
except ValueError as err:
    print(err)

