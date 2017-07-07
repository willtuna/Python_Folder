import time
time.time() #number of second from 1970 Jan 1st 
def numbers(max):
    time1 = time.time()
    for i in range(0,max):
        print(i)
    time2 = time.time()

    return time2 - time1 


print(numbers(10000))




currrentTime = time.asctime()

print('Current Time:', currrentTime)

tup =(2000, 10, 15, 8, 45, 12 ,6 ,0, 0)
print(time.asctime(tup) )

time.localtime() 

for i in range(0,5):
    print(i)
    time.sleep(1)


