
class Students:
    # initialize the object , constructor
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    #member function
    def displayStudent(self):
        return("Student names is", self.name, "and age is ", str(self.age))
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.grade == other.grade


class Freshman(Students):
    #initalize the object
    def __init__(self, enroll_y, name , age = 19, grade = 1):
        super.__init__(name, age, grade)
        self.enroll_y = enroll_y
    def __eq__(self, other):
        return  self.enroll_y == other.enroll_y and super.__eq__(self,other)



student1 = Students("Bob", 12, "6th")
student2 = Students("Lily", 32, "1st")
# Check whether student1 has attribute age inside
hasattr(student1, "age")

hasattr(student2, "Birthday")


# Adding attribute to class
# But this only apply to student1
setattr(student1, "Birthday", "Jun 1st")

getattr(student1, "grade")

delattr(student1, "Birthday")





'''
>>> class Students:
    ... def __init__(self, name):
>>> class Students:
    ...     def __init__(self,name):
    ..             self.name = name
    ..     def displayStudent(self):
       ...             return("Student name is ", str(self.name))
       ... 
       >>> stu1 = Students("Holy")
       >>> stu2 = Students("Goods")
       >>> stu1.displayStudent()
       ('Student name is ', 'Holy')
       >>> hasattr(stu2,"name")
       True
       >>> hasattr(stu2,"age")
       False
       >>> setattr(stu2,"gender")
       Traceback (most recent call last):
             File "<stdin>", line 1, in <module>
             TypeError: setattr expected 3 arguments, got 2
             >>> setattr(stu2,"gender","male")
             >>> stu2.gender
             'male'
             >>> hasattr(stu1,"gender")
             False
             >>> hasattr(stu2,"gender")
             True
             >>> getattr(stu2,"gender")
             'male'
             >>> delattr(stu2,"name")
             >>> stu2.displayStudent()
             Traceback (most recent call last):
               File "<stdin>", line 1, in <module>
                 File "<stdin>", line 5, in displayStudent
                 AttributeError: 'Students' object has no attribute 'name'
                 >>> 
'''




class Parent:
    Counter = 10

    def __init__(self):
        print("Class initialized")

    def parentFunc(self):
        print("Parent being called ")

    def setCounter(self, num):
        Parent.Counter = num

    def showCounter(self):
        print(str(Parent.Counter))


class Child(Parent):# Inherit from Parent Class
    def __init__(self):
        print("Child class being initialized")

    def childFunc(self):
        print("Child Class being called")

    def showCounter(self):
        print("Counter funciton from parent is overrided !\n")

# Child class inherit the attribute and method all from the Parent Class
