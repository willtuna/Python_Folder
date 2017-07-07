import sys
def quarters(next_quarter=0.0):
    while True:
        received = (yield next_quarter)
        if received is None:
            next_quarter += 0.25
        else:
            next_quarter = received

result = []
generator = quarters() # generator is just a reference of quaters fucntion
while len(result) < 5:
    x = next(generator) # next just iterate the next 
    if abs(x-0.5) < sys.float_info.epsilon:
        x = generator.send(1.0)
    result.append(x)

print(result)
