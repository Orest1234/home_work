def func7(n):
    if n == 1:
        return 1
    return n + func7(n - 1)


n = int(input())
print(func7(n))