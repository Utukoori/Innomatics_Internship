import re

n = int(input())

for i in range(n):
    tel = input()
    pattern = '^[789][0-9]{9}$'
    print("{}".format("YES" if bool(re.match(pattern, tel)) else "NO"))
