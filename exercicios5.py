import random

def intersec(a,b):
	return (set(a)&set(b))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print (intersec(a,b))


c= random.sample(range(30),13)
d= random.sample(range(30),12)

#I'll print both c and d just to verify if it's really doing the intersection

print (c)
print (d)

# After that we can do everything in one line as per below

print(set(c).intersection(d))
