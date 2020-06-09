a = [1, 2, 3, 4, 5, 6, 7]
b = []
for i in a:
    if i%2 ==0:
        I= i*0
        b.append(I)
    else:
        H = i**2
        b.append(H)
print(a, b)
