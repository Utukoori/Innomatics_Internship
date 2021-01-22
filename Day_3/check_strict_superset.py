A=set(input().split(' '))
n=int(input())
b=([])
c=set()
for i in range(n):
    B=set(input().split(' '))
    b.append(B)
for i in range(len(b)):
    if(b[i].intersection(A)==b[i]):
        c.add(True)
        continue
    else:
      c.add(False)
      break
if(False in c):
    print(False)
else:
    print(True)
