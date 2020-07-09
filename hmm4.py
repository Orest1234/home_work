a = {'zero': 0, 'one': 1, 'two': 2, 'tree': 3}
print(a)


def func4(a):
    val = a.values()
    keys = a.keys()
    l = reversed(keys)
    b = dict(zip(l,val))
    print(b)


func4(a)