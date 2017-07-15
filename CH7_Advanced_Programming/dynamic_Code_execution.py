import math
code = '''
def area_of_Sphere(r):
    return 4*math.pi **2
'''

context ={}
context['math'] = math 
exec(code , context) # THIS IS THE SAME AS 
#                      exec code in context
exec(code , globals, locals) # This is the same as 
#                           exec code in globals, locals
# this just pass the math to the code , so it could use the imported math module
# with this , we know that to use dynmaic execution, we use dict as the interface to access the name ,
# good for security usage



