N=int(input())
for i in range(N):
    n=int(input())
    A=set(map(int, input().split()))
    m=int(input())
    B=set(map(int, input().split()))
    if(A.intersection(B)==A):
        print(True)
    else:
        print(False)
