import cmath
z = complex(input())
r = abs(z)
q = cmath.phase(complex(z.real,z.imag))

print(r,'\n',q)
