import math
import time

start_time = time.time()
print(start_time)


def fn(x):
    return math.exp(x) - math.sin(x)


a = -1
b = 1
d = 0.1
cal = math.log(d / (b - a)) / math.log(0.618)
iterations = cal // 1 + 1
print("No of iterations:", iterations)
x1 = b - (0.618 * (b - a))
x2 = a + (0.618 * (b - a))
f_x1 = fn(x1)
f_x2 = fn(x2)

while iterations != 0:
    if f_x1 < f_x2:
        print("x1:", x1, "x2:", x2)
        iterations -= 1
        b = x2
        x2 = x1
        x1 = b - (0.618 * (b - a))
        f_x2 = f_x1
        f_x1 = fn(x1)

    else:
        print("x1:", x1, "x2:", x2)
        iterations -= 1
        a = x1
        x1 = x2
        x2 = a + (0.618 * (b - a))
        f_x1 = f_x2
        f_x2 = fn(x2)


print("Minima is approximately = ", ((b + a) / 2))
print("TIme taken is:", float(time.time() - start_time))
