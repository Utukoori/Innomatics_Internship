num = int(input())
data = set(map(int, input().split()))
op = int(input())

for x in range(op):
  operation = input().split()
  if operation[0] == "remove":
    data.remove(int(operation[1]))
  elif operation[0] == "discard":
    data.discard(int(operation[1]))
  else:
    data.pop()

print(sum(data))
