n = int(input())
b = bin(n)
o = oct(n)
h = hex(n)
space = " "
b1 = len(b)
o1 = len(o)
h1 = len(h)
print((b1-2)*space,"bin", +(b1+o1-3)*space, "oct", +(b1+h1-3)*space, "hex",)
print(space,b, + b1*space, o, +b1*space, h,)

 
