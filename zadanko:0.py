a = int(input("licznik:"))
b = int(input("mianownik:"))
c = int(input("licznik2:"))
d = int(input("mianownik2:"))
iloczyn=b*d

while b!=d:
  if d>b: d-=b
  else: b-=d
    
wspln_mian=iloczyn/b

if b == d:
  lcznk=a+c
  mnwnk=b
  print(f"{lcznk}/{wspln_mian}")