

with open('/etc/passwd') as f:
    for line in f:
        print line.split(':')[1]

''' The same as

try:
    f = open('/etc/passwd')
    for line in f:
        print line.split(':')[1]
finally:
    f.close()


# Context Manager alwayse make sure f.close() called
'''




# Create our own context manamger, that is with statement

class working_dir(object):
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.org_dir = os.getcwd()

    def __enter__(self): 
        os.chdir(self.new_dir) # change directory to new_dir

    def __exit__(self, exc_type, exc_val, exc_traceback):
        os.chdir(self.org_dir)


# Alternative context manager

import contextlib

@contextlib.contextmanager
def working_dir(new_dir):
    org_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yeild  #end of __enter__
    finally:
        os.chdir(org_dir)



from urllib2 import urlopen
from contextlib import closing

with closing(urlopen(some_api)) as foo, closing(urlopen(other_api)) as bar:
        # do your stuff here


# super greate usage of contextmanager
class my_error_handling(object):
    def __enter__(self): pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if issubclass(exc_type, UnicodeError):
            print ('annoying')
        elif issubclass(exc_type, ValueError):
            print ('hrmm')
        elif issubclass(exc_type, OSError):
            print('other')
        else:
            print 'other'
        return True

with my_error_handling():
    #do stuff



