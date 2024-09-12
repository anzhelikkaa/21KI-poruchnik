vova = ["Bobik", 5.14, "Hello", 16, True, 23, 60]
vova1 = [type(x) for x in vova]

u = 0 
r = 0
m = 0
q = 0
for x in vova:
    if type(x) == str:
        u += 1
    elif type(x) == int:
        r += 1
    elif type(x) == float:
        m += 1
    elif type(x) == bool:
        q += 1
if u>r and u>m and u>q:
    print("str")
if r>u and r>m and r>q:
    print("int")
if m>u and m>r and m>q:
    print("float")
if q>u and q>r and q>m:
    print("bool")
