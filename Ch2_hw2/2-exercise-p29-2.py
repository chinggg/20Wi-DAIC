import numpy as np

steps  = 10
wlk = np.random.normal(0, 1, size=(3, steps))
pos = wlk.cumsum(axis = 1)
print("每步走完后物体在三维空间的位置")
print(pos)
dists = np.sqrt(pos[0]**2 + pos[1]**2 + pos[2]**2)
np.set_printoptions(precision = 2)
print("每步走完后物体到原点的距离(只显示两位小数)")
print(dists)
print("物体在z轴上到达的最远距离")
print(abs(pos[2]).max())
print("物体在三维空间距离原点的最近值")
print(dists.min())
