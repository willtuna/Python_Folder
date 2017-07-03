s = lambda x : '' if x == 1 else 's'
# s is refer to an anonymous function,with argument x.
count = 1
print("{0} file{1}".format(count, s(count)))
# if the count ==1 it print 1 file
# if count != 1 it print count file's'
