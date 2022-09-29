import time
import math


def fn(x):
    return math.exp(x - 2) - x


start_time = time.time()
a = -2
b = 6

d = 0.1
l = 1
Fn = l / d


def halving(a, b):
    count = 0
    fib_nums = []
    gr = []
    f0 = 1
    f1 = 1
    fib_nums.append(f0)
    fib_nums.append(f1)

    n = 0
    while n < Fn:
        n = f0 + f1
        fib_nums.append(n)
        f0 = f1
        f1 = n

    print(fib_nums)
    for i in range(len(fib_nums) - 1, 1, -1):
        gr.append(fib_nums[i - 1] / fib_nums[i])
    iterations = len(gr)
    gr.append(1)
    print(gr)

    x1 = b - gr[0] * (b - a)
    x2 = a + gr[0] * (b - a)
    f_x1 = fn(x1)
    f_x2 = fn(x2)

    while iterations != 0:
        count += 1
        if f_x1 < f_x2:
            print("Iteration", count, "x1=", round(x1), "x2=", round(x2))
            iterations -= 1
            b = x2
            x2 = x1
            f_x2 = f_x1
            x1 = b - gr[count] * (b - a)
            f_x1 = fn(x1)

        else:
            print("Iteration", count, "x1=", round(x1), "x2=", round(x2))
            iterations -= 1
            a = x1
            x1 = x2
            f_x1 = f_x2
            x2 = a + gr[count] * (b - a)
            f_x2 = fn(x2)

    return x1, x2


x1, x2 = halving(a, b)
print("X value:", (x1 + x2) / 2)
print("Minima is :", fn((x1 + x2) / 2))
end_time = time.time()
print("Time taken:", end_time - start_time)
