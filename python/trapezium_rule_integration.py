import math

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    print(f"{h=}")
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result


def func(x):
    return math.sqrt(4-x**2)  # semicircle with radius 2 at (0, 0)


a = 0
b = 2
#  num of trapezoids, more trapezoids = more accurate answer
n = 1000

integral = trapezoidal_rule(func, a, b, n)
print(f"Integral: {integral}")
