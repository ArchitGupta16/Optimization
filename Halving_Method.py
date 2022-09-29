import time

start_time= time.time()

def fn(x):
    return math.exp(x) - math.sin(x)


import math

a = -1
b = 1
precision = 0.1
x = math.log(precision / (b - a)) / math.log(1 / 2)
iterations = x // 1 + 1


def halving_method(a, b, iterations):
    ans = 0

    while iterations != 0:
        m0 = (b + a) / 2

        if fn(m0) < fn(a) and fn(m0) < fn(b):
            iterations -= 1

            ans = m0
            m1 = (m0 + a) / 2
            m2 = (m0 + b) / 2

            if fn(m1) < fn(m0):
                b = m0
            elif fn(m2) < fn(m0):
                a = m0
            else:
                a = m1
                b = m2

        elif fn(m0) > fn(a) and fn(m0) < fn(b):
            iterations -= 1
            b = m0

        elif fn(m0) < fn(a) and fn(m0) > fn(b):
            a = m0
            iterations -= 1

        else:
            ans = m0
    return ans


final_ans = halving_method(a, b, iterations)
print("Output value", final_ans)
end_time = time.time()
print("TIme taken is:",end_time-start_time)