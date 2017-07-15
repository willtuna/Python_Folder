# Python Data Type is classified to int and str category
# Python's integer max is defined by user memory, so it suppot a whole larger number.


# type_conversion:
print( 'str(45) return', str(45), 'in',type(str(45)) )# return 45 in '45'
print( "int('45') return",  int('45') ,'in', type(int('45')))  # return 45

# type() return the data type or so called class inside the ()


#Object Reference Concept
#In python there is no concept of variable, since it only use the object reference technique


x = 'blue' # an 'blue' str object is referenced by x,
x = 19     # x now reference to int object 19, so the 'blue' is now schedule in the garbage-collection

# Python use dynamic typing, object reference can be rebound to refer to a different object.
# In contrast, C use strong typing, it only refer to defined data type.
# However, we could still apply some constraint on python.



# A collection of data type:   list, tuple
# tuple is immutable collection of data, and all the element inside the tuple could be different 
# data type.  

#inside the tuple and list, they store the object reference rather than the data item

#tuple: immutable collection of data             
#usage of tuple
tuple3 = ('Denmark','Finland','Norway')
tuple1 = ('one',) # a tuple with one element "one"
empty_tuple = ()
print(tuple3[2])

print("The lenght of tuple3 is :",len(tuple3) ,"\nEmpty_tuple is: ", len(empty_tuple))


#list: mutable collection of data
#usage of list
list1 = [1,4,59,6,10]
list2 = ['Hi',"Vegapunk",26]
print(list2[1])
#since list is the mutable collection of data it must support some method to change the element is list
#actually list is a kind of class with object-oreinted concept, it has member-function like method
#Example of member function append()
#method 1 use member-function calling like method
list2.append("NCTU")
print(list2)
#method 2 use class-owned like calling method
list.append(list2,"NTU")
print(list2)

