import re
s = input()
h = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])',s,re.IGNORECASE)
if h:
    for i in h:
            print(i)
else:
    print(-1)        
