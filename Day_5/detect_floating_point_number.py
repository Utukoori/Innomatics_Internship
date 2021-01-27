import re

t = int(input())
for i in range(t):
    s = input()
    if re.search(r'^[+-]?\d*\.\d+$',s):
        print(True)
    else:
        print(False)
