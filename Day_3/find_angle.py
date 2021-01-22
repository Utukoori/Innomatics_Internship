import cmath
import math


ab = float(input())
bc = float(input())
ph = cmath.phase(complex(bc,ab))
print(str(round(math.degrees(ph)))+u"\N{DEGREE SIGN}")
