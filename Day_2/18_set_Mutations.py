n=int(input())
s=set(input().split())
m=int(input())
for i in range(m):
    command,k=input().split()
    p=set(input().split())
    if(command=="intersection_update"):
        s.intersection_update(p)
    elif(command=="update"):
        s.update(p)
    elif(command=="difference_update"):
        s.difference_update(p)
    else:
        s.symmetric_difference_update(p)
l=list(s)
sum=0
for i in l:
    sum=sum+int(i)
print(sum)
