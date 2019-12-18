#Appending array B to array A
import numpy as np
a=[10,9,8,7,6]
b=[5,4,3,2,1]
for i in range(0,len(b)):
	 a.append(b[i])
print a
c=np.array([10,9,8,7,6])
d=np.array([5,4,3,2,1])
e=np.append(c,d)
print e
