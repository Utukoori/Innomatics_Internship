import re

for line in range(int(input())):
    string = ''
    string = re.sub(r'(?<= )&&(?= )','and',input())
    string = re.sub(r'(?<= )\|\|(?= )','or',string)
    print (string)
