value = input("Expression: ")

a, b, c = value.split()

a = float(a)
c = float(c)
#answer = a b c
if b == "+":
    sums = a + c
elif b == "-":
    sums = a - c
elif b == "/":
    sums = a / c
elif b == "*":
    sums = a * c

print(sums)