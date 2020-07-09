str1 = input()
str2 = input()
len_str2 = len(str2)//2
#print(len_str2)
str2_v2 = str2[:len_str2]
print(str2_v2)
str2_v3 = str2[::-1]
#print(str2_v3)
str2_v4 = str2_v3[:len_str2]
#print(str2_v4)
str2_v5 = str2_v4[::-1]
print(str2_v5)
print(str2_v2+str1+str2_v5)
