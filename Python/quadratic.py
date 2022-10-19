import math
import sys


While True:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    d = ((-1 * b) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    e = ((-1 * b) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)

    print(f"x = {d} or {e}")
