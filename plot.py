import numpy as np
from matplotlib import pyplot as plt, gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D

# pretrained
# 2X3X3X3X1
# before
before="""0.506323,0.125622,0.167479
0.868289,0.245259,0.924985
0.0916172,0.792367,0.0989482
0.390526,0.898265,0.870884"""
# after
after="""0.0953641,0.233988,0.531217
0.918364,0.949002,0.999244
0.000698512,0.96767,0.0867855
0.0285391,0.999336,0.978114"""

# # 2X3X4X3X1
# # before
# before="""0.0843047,0.326058,0.188376
# 0.184513,0.948432,0.734432
# 0.798226,0.0518403,0.299272
# 0.909283,0.685386,0.841455"""
# # after
# after="""0.00762472,0.935584,0.137524
# 0.0524882,0.999811,0.979299
# 0.561904,0.101922,0.911496
# 0.891924,0.984246,0.999685"""

# # 2X4X2X3X1
# # before
# before = """0.0732405,0.389799,0.230927
# 0.66629,0.826228,0.0708355
# 0.287844,0.255446,0.93761
# 0.917524,0.725368,0.795373"""
# # after
# after = """0.232488,0.41725,0.708399
# 0.98919,0.994483,0.0739695
# 0.974552,0.0951076,0.99909
# 0.999925,0.960556,0.978106"""

a = before.split("\n")
b = []
for a_i in a:
    b.append([float(k) for k in a_i.split(',')])

c = after.split("\n")
d = []
for c_i in c:
    d.append([float(k) for k in c_i.split(',')])
v = np.array(b)
w = np.array(d)
print(b)
print(d)
t1 = np.array([1, 0, 0, 1])
t2 = np.array([1, 0, 0, 1])
fig = plt.figure()
gs = gridspec.GridSpec(2, 2)

ax1 = fig.add_subplot(gs[:, 0], projection='3d')
ax2 = fig.add_subplot(gs[:, 1], projection='3d')
ax1.set_title('before')
ax2.set_title('after')
ax1.scatter(v[:, 0], v[:, 1], v[:, 2], c=t1, s=500, marker='o')
ax2.scatter(w[:, 0], w[:, 1], w[:, 2], c=t2, s=500, marker='*')

plt.show()
