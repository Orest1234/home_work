l = [1, 2, 3, 4, 5, 100]

def func1(l = [], n = 2):
     l1 = []
     for i in range(n):
          a = max(l)
          l1.append(a)
          b = l.index(a)
          del l[b]
     return l1
print(func1(l))





