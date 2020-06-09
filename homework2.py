l1 = [1, 2, 3, 1, 2, 3, 4]
l2 = []
l1.sort()
for i in l1:
    if(i in l2):
        print(i)
    else:
        l2.append(i)
    
print (l2)
