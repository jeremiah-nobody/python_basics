a = 20
b = 19
for i in range (11):
    for j in range(40):
        if j == a or j == b:
            print("0", end="")
        else:
            print(".",end="")
    print("")
    if i < 5:
        a+=3
        b-=3
    else:
        a-=3
        b+=3