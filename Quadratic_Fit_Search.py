from matplotlib import pyplot as plt
import numpy as np


def fn(x):
    return x*x + 54/x


x1, x2, x3 = (1, 2, 6)
precision = 0.01


def val_xq(x1, x2, x3):
    return 1 / 2 * (((x3 ** 2 - x2 ** 2) * fn(x1) + (x1 ** 2 - x3 ** 2) * fn(x2) + (x2 ** 2 - x1 ** 2) * fn(x3)) / (
            (x3 - x2) * fn(x1) + (x1 - x3) * fn(x2) + (x2 - x1) * fn(x3)))


def QFS(x1, x2, x3, precision):
    arr = []
    xq = val_xq(x1, x2, x3)
    x_q_1 = 0
    while abs(xq - x_q_1) > precision and ((x3 - x2) * fn(x1) + (x1 - x3) * fn(x2) + (x2 - x1) * fn(x3)) != 0:
        x_q_1 = xq
        if x2 < xq:
            if fn(x2) < fn(xq):
                x3 = xq
            else:
                x1 = x2
                x2 = xq
        else:
            if fn(x2) < fn(xq):
                x1 = xq
            else:
                x3 = x2
                x2 = xq

        xq = val_xq(x1, x2, x3)
        print("(x1,x2,x3)", "(", x1, x2, x3, ")")
        a = np.array([[1, x1, x1 ** 2],
                      [1, x2, x2 ** 2],
                      [1, x3, x3 ** 2]])
        y = np.array([fn(x1), fn(x2), fn(x3)])
        X = np.linalg.solve(a, y)
        arr.append(X)
    return arr


def expr(c0, c1, c2):
    return c0 + c1 * x + c2 * x * x


x = np.linspace(x1, x3)
plt.plot(x, fn(x), color="black")
a = QFS(x1, x2, x3, precision)
print(a)
for i in range(len(a)):
    plt.plot(x, expr(a[i][0], a[i][1], a[i][2]), label=f"Iteration {i + 1}")
plt.xlabel("X")
plt.ylabel("F(x)")
plt.title("Quadratic Fit Search")
plt.legend()
plt.show()
