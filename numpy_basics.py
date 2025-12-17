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
arr = np.array([1,2,3,4],ndmin = 5)

print(arr)
print('number of dimensions', arr.ndim)

lst = [1,2,3,4,4]
arr = np.array([1,2,3,4,4])
print(lst)
print(arr)
print(type(lst))
print(type(arr))

arr1d = np.array([1,2,3])
arr2d = np.array([[1,2,3],[4,5,6]])
arr3d = np.array([[[1,2,3],[4,5,6],[2,5,6]]])
print(arr3d)
print("shape of 1d",arr1d.shape)
print("shape of 2d",arr2d.shape)
print("shape of 3d",arr3d.shape)
print(arr2d.size)
print(arr3d.size)
print(arr3d.ndim)
print(arr2d.dtype)

num = np.array([[1,2.1,3],[1,2,3]],dtype = int)

print(num.dtype)

print(np.ones((3,3),dtype=int))

print(np.full((2,3),10))


a = np.array([1,2,3])
b  = np.array([30,12,13])

print(a + b)
print(a - b)
print(a % b)
print(a * b)

for i in a:
    i + 10

print(i)

a = np.array([5,10,15])
b = [5,5,5]

print(a +b)

d =np.array([10,11,12])
e = np.array([[10,11,12],[12,34,56]])

print(d + e)

arr = np.array([[10,15,20],[20,30,50]])
print("sum:",np.sum(arr))
print("sum:",np.sum(arr, axis = 0))
print("sum:",np.sum(arr, axis = 1))
print("sum:0",np.sum(arr[arr>10]) )
"""
#indexing
arr =np.array([1,2,3,4,5])
print(arr[2])

arr2d = np.array([[1,2,3],[4,5,6],[3,4,6]])
print(arr2d[2][0])
