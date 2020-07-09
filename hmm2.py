l1 = [1, 3 ,5, 7, 9, 10, 11]
l2 = [2, 4, 6, 8, 10, 11]

def func2(l1, l2):
    l3 = []

    for i in l1:
        if i in l2:
            l3.append(i)
    print(l3)

func2(l1, l2)