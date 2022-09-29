from mpl_toolkits import mplot3d
from matplotlib import *
import matplotlib.pyplot as plt
import numdifftools as nd
import numpy as np
from sympy import *

x, y = symbols('x y')
x_0 = [10, -5]
b = [0, 0]


# def g(x):
#     return (1-x[0])**2 + 100*(x[1]-x[0]**2)**2
def g(x):
    return 0.5*(x[0])**2 + x[0]*x[1] + x[1]**2

# def s(x, y):
#     return (1-x)**2 + 100*(y-x**2)**2


def s(x, y):
    return 0.5*x**2 + x*y + y**2


# --------------------------------------
df_x = diff(s(x, y), x)
df_y = diff(s(x, y), y)

# Gradient
v1 = df_x.subs([(x, x_0[0]), (y, x_0[1])])
v2 = df_y.subs([(x, x_0[0]), (y, x_0[1])])
u_0 = np.array([round(-v1), round(-v2)])
u_0_T = u_0.transpose()

# Hessian
H = nd.Hessian(g)([x_0[0], x_0[1]])

# print(H)

n = 2
l = []
while n > 0:
    alp_num = u_0_T.dot(H).dot(x_0) + u_0_T.dot(H).dot(b)
    alp_den = u_0_T.dot(H).dot(u_0)
    alp = round(alp_num / alp_den)

    # x1 calculations
    x_1 = x_0 - (alp * u_0)
    print(x_1, "x")

    v1 = df_x.subs([(x, round(x_1[0])), (y, round(x_1[1]))])
    v2 = df_y.subs([(x, round(x_1[0])), (y, round(x_1[1]))])
    del_f = np.array([round(v1), round(v2)])

    # beta calculations
    beta_num = del_f.transpose().dot(H).dot(u_0)
    beta_den = u_0_T.dot(H).dot(u_0)
    beta = round(beta_num / beta_den)
    u_i = -del_f + beta * u_0
    u_i_T = u_i.transpose()

    x_0 = x_1
    u_0 = u_i
    l.append(x_0)
    n = n - 1


# ----------------------------
# graph
xx = np.linspace(-6, 6, 50)
yy = np.linspace(-6, 6, 50)

X, Y = np.meshgrid(xx, yy)
Z = s(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z,200, cmap="cool")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D contour')
# plt.show()

x_x = []
y_y = []
x_x.append(10)
y_y.append(-5)
for i in l:
    x_x.append(i[0])
    y_y.append(i[1])

plt.plot(x_x, y_y,'bo',linestyle="--")
plt.show()