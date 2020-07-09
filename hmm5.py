str = "abbaeta"

def func5(st):
    val = []
    for letter in st:
        val.append(st.count(letter))
    b = dict(zip(st,val))
    print(b)


func5(str)