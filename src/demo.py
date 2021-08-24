import time

import numpy as np


class Foo:
    val: float

    def __init__(self, val):
        self.val = val


x = 500000
# y = 2
B = np.array([2., -1., 4.])
C = np.array([[True, 0., 4.]])
print("SUM")
print(B * C)
D = np.random.randint(1, 101, x)
E = np.random.randint(1, 101, x)

foo = Foo(D[0])
print(str(foo.val))
print(str(D[0]))
D[0] = 123.
print(str(foo.val))
print(str(D[0]))

print("F")
F = np.array([[1., 2., 3.], [5, 6, 7], [8, 9, 0]])
print(F)
F[1].fill(42)
print(F)
# C = np.append(C, C)
output = []
output_manual = [x]


def main_calc():
    global output
    output = np.dot(D, E)


def main_calc_manual():
    global output_manual
    global x
    for i in range(x):
        output_manual[0] += (D[i] * E[i])


start_time = time.time()
main_calc()
time_numpy = (time.time() - start_time)
print("numpy array--- %s seconds ---" % time_numpy)

start_time = time.time()
main_calc_manual()
time_manual = (time.time() - start_time)
# print("manual     --- %s seconds ---" % time_manual)
# print("ratio      --- %s ---" % (time_manual / time_numpy))
print(output)
print(output_manual)
