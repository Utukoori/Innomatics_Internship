num = int(input())

set_a = set()
set_b = set()

for i in map(int,input().strip().split()):
    if i not in set_a:
        set_a.add(i)
    else:
        set_b.add(i)
print(sum(set_a-set_b))
