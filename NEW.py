import random
import os
print("select random numbeer from list")
elements=[1,2,3,4,5]
print(random.choice(elements))
print(random.choice(elements))
print(random.choice(elements))
print("\n select a random element from a set:")
elements=set([1,2,3,4,5])
#convert to tuple because sets are invalid inputs
print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))
print(random.choice(tuple(elements)))
print("\n select a random value from a dictionary:")
d={"a":1,"b":2,"c":3,"d":4,"e":5}
key=random.choice(list(d))
print(d[key])
key=random.choice(list(d))
print(d[key])
key=random.choice(list(d))
print(d[key])
print("\n select a random file from a dictionary:")
print(random.choice(os.listdir("/")))