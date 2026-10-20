def f_1(n):
    if n <= 0:
        return 1
    return n - g_1(n - 1)


def g_1(n):
    if n <= 0:
        return 0
    return n - f_1(n - 1)


inputs = list(range(25))
f_values = [f_1(n) for n in inputs]
g_values = [g_1(n) for n in inputs]

for i in range(len(inputs)):
    print(f"f_1({inputs[i]}) = {f_values[i]}, g_1({inputs[i]}) = {g_values[i]}")
