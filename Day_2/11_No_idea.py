n,m=list(map(int, input().split()))
N=list(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))
result=0
for x in N:
    if x in A:
        result+=1
    elif x in B:
        result-=1
print(result)
