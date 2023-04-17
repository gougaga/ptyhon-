import numpy as np
a = np.array([2, 5, 6, 8, 65, 6, 7])
print(a)
print(type(a))
b = np.array(80)
print(b)
print(type(b))
c = np.zeros((6, 9), dtype=np.uint8)
print(c)
print(type(c))
d = np.ones((3, 3), dtype=np.uint8)
print(d)
print(type(d))
#
print(a.max())
print(a.min())
a.sort()
print(a)
print(a.shape)

q = np.array([[3, 8, 9], [5, 8, 1], [7, 6, 4]])
print(q)
print(np.median(q))
print(np.median(q, axis=1))
print(np.median(q, axis=0))

print(np.mean(q))
print(np.mean(q, axis=1))
print(np.mean(q, axis=0))

w = np.array([8, 5, 9, 4, 2, 7])
print(np.var(w))
print(np.std(w))

e = np.arange(9, dtype=np.float64).reshape(3, 3)
r = np.array([90, 90, 90])
print(e)
print(r)
print(np.add(e, r))
print(np.subtract(e, r))
print(np.multiply(e, r))
print(np.divide(e, r))

t = np.array([20.66, 90, 66.555, 20, 0.25, 25.36, 9])
print(np.around(t))
print(np.floor(t))
print(np.ceil(t))


#
x = np.dtype([('sex', 'U1'), ('height', 'f4')])
per = np.loadtxt(r'C:\Users\86186\Desktop\student-data.txt', dtype=x, skiprows=9, usecols=(1, 3))
print(per)
girlisg = per['sex'] == 'F'
data = per['height'][girlisg]
print(data)
print(np.mean(data))


boylisg = per['sex'] == 'M'
data1 = per['height'][boylisg]
print(data1)
print(np.median(data1))



