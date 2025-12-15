import numpy as np
"""
a = np.array(42)
b =np.array([1,2,3,4,5])
c = np.array([[1,2,3],[2,3,4]])
d = np.array([[[1,2,3],[2,3,4],[4,5,6]]])
e = np.array([[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)
"""
arr = np.array([1,2,3,4],ndmin = 5)

print(arr)
print('number of dimensions', arr.ndim)