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
print("RAND")
print(B * C)
print(np.random.default_rng().uniform(0.1, 0.3, 10))
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
print("FILL")
F1 = np.array([False, False, True])
F2 = F1 * 1
print(F1)
print(F2)

print("DATA NON INPUT")
data = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 1., 0.8])
print(data)
weights = np.array([
    [0., 0., 0., 0., 0., 0., 0.],  # 1
    [0., 0., 0., 0., 0., 0., 0.],  # 2
    [0., 0., 0., 0., 0., 0., 0.],  # 3
    [0., 0., 0., 0., 0., 0., 0.],  # 4
    [0., 0., 0., 0., 0., 0., 0.],  # 5
    [0.1, 0.1, 0.1, 0.1, 0.1, 0., 0.7],  # 6
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.4, 0.],  # 7
])
is_enabled = np.array([False, False, False, False, False, True, False])
is_input = np.array([True, True, True, True, True, False, False])

expected = [0., 0., 0., 0., 0., 0., 0.4]

data_filtered = data * np.invert(is_input) * is_enabled
print("data_filtered")
print(data_filtered)
res = np.dot(data_filtered, weights.T)
print("RES")
print(res)
print("SIGM")


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


sigmoid_v = np.vectorize(sigmoid)
sigm_in = np.random.default_rng().uniform(0., 1, 10 * x)

print("SIGM END")

print("Input ID detect")

inputNeurons = np.array([True, False, True, False, True, True])
inputData = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
inputIdList = []
for i in range(len(inputNeurons)):
    if inputNeurons[i]:
        inputIdList.append(i)
print(inputIdList)
print("Input clean check")
print(inputData * np.invert(inputNeurons))


def main_calc():
    global output
    # output = np.dot(D, E)
    # sigm_out = sigmoid_v(sigm_in)  SLOW!

    sigm_out = np.apply_along_axis(sigmoid, -1, sigm_in)  # FAST SIGMOID
    # print(sigm_in)
    print(sigm_out)
    # print(sigm_out0)


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
