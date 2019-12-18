#Taking two arrays A,B from user in runtime and appending array B to array A
import numpy as np
a=input("Enter the first array: ")
b=input("Enter the second array: ")
c=a
d=b
for i in range(0,len(b)):
	 a.append(b[i])
print a
e=np.append(c,d)
print e

