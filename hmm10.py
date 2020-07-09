def func10(a, b, c, d=0):
    D = b ** 2 - 4 * a * c
    print('Дискримінант', D)
    d_d = D**0.5
    print('Корінь з дискримінанту', d_d)
    x1 = (-b +d_d) / (2*a)
    x2 = (-b -d_d) / (2*a)
    print('x1=', x1)
    print('x2=', x2)
func10(1, 3, -4, )
