import numpy as np 
from numpy.linalg import inv, det
a = np.array([[1,2,3], [4,5,6]])
b = np.array([[7,8],[9,10],[11,12]])

c = a @ b
print(c)
x = np.matmul(a,b)
print("x", x)

y = np.dot(a,b)
print("y", y)

#INVERSE

z = np.array([[4,7],[2,6]])
inverse_z = inv(z)
print(inverse_z)

#determinant
a = np.array([[4,6],[3,8]])
deter = det(a)
print(int(round(deter)))

# solve real life problems

s = np.array([[118.4, 135.2]])
m = np.array([[3, 3.5],[3.2, 3.6]])


child, adult = np.matmul(s, inv(m))
print("child is :", int(round(child)))
print("adult", int(round(adult)))