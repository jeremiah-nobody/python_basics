import os
import sys
import time

clear = lambda: os.system('cls')
clear()


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(26):
     sys.stdout.write(a[i])
     time.sleep(1)
     sys.stdout.write("\b")
     sys.stdout.flush()
