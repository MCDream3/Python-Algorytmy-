#sposób liczenia ułamków

a,b,c,d = int(input()),int(input()),int(input()),int(input())
x = b
y = d
iloczyn = x*y

while y<0:
  x,y = y,x%y
  NWW=iloczyn//x
  
  e=(NWW//b)*a
  f=(NWW//d)*c
  g=e+f

print(f"{a}/{b}+{c}/{d}={e}/{NWW}+{f}/{NWW}={g}/{NWW}")
