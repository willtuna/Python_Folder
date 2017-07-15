#! /usr/bin/env python3
# decorator exposed 1
def expose(func):
    func.exposed = True
    return func

@expose
def myview():
    # do stuff
    return dict(records=records)

# example2 

def expose2(template):
    def mark_exposed(func):
        func.exposed = True
        func.template = template
        return func
    return mark_exposed

@expose2('view.html')
def myview2():
    #do stuff
    return dict(records=records)


# example3

def memoize(func):
    def check_cache(*args):
        if not hasattr(func, 'results'):
            func.results = {}
        if args not in func.results:
            func.results[args] = func(*args) # we could direct access through decorator
        return func.results[args] #wrapping of result we could access
    return check_cache # wrapping the function itself

@memoize
def find_user(user_id):
    #'query databas and load User object'
    return User.m.get(_id = user_id)

# example4 , result is the same as 

from decorator import decorator
@decorator
def memoize(func, *args):
    if not hasattr(func, 'results'):
        func.results = {}
    if args not in func.results:
        func.results[args] = func(*args)
    return func.results[args]
# the above is like   decorator(memoize)



# funcor, class as function
class say_something(object): # inherit from object class
    def __init__(self, catchphrase):
        self.catchphrase = catchphrase

    def __call__(self):
        print(self.catchphrase)


# class function as decorator
class memoize(object):
    def __init__(self, max):
        self.max = max
    def __call__(self, func):
        return decorator(self.check_cache, func)

    def check_cache(self, func, *args): #the decorator inside the class function
        # TODO: use self.max
        if not hasattr(func, 'results'):
            func.results = {}
        if args not in func.results:    
            func.results[args] = func(*args)
        return func.results[args]

# class decorator
from functools import total_ordering

@total_ordering
class Student:
    def __eq__(self, other):
        return ((self.lastname.lower(), self.f ) == ((other.lastname.lower()), other.f))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.f ) < ((other.lastname.lower()), other.f))



print(myview.exposed)
print(myview2.template)
buzz_lightyear = say_something("To Infinity, and beyond !")

buzz_lightyear()



















