def func11(a, b, c):
    def func11_(x):
        return a*x**2 + b*x + c
    return func11_

func11__ = func11(1, 2, 3)
print(func11__(0))