a = input()
a_int = a.isdigit()
a_str = a.isalpha()

if a_int == True:
    print('int')
elif a_str == True:
    print('str')
else:
    print('float')
