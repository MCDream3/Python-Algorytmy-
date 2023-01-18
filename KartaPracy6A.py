#zad 1 ez B)

x = int(input())
wynik = 0
while x>0:
  wynik+= x%10
  x //=10
print(wynik)

#zad 2

a = int(input())
temp=0
for i in range(2,a):
  if a%i == 0:
    temp += 1
if temp>3:
  print("chyba tak")
else:
  print("no nie")

#zad 3 - doskonale- dzielniki dodane do siebie daja tą liczbe nie liczac jej samej <--

n = int(input())
suma = 0
for i in range(1,n):
  if n%i == 0:
    suma +=i
if suma == n:
   print("jest doskonała")
else:
  print("you idoit its not")

#zad 4 - względnie pierwsze- ich nwd = 1

x = int(input())
y = int(input())
while  x!=y:
  if x>y: x-=y
  if y>x:y-=x
if x == 1:
  print("liczby są względnie pierwsze")
else:
  print("liczby takie nie są")

#zad 5 mamy parę?

m = int(input())
for i in range(10,20):
  x = m
  y = i
  while y>0:
    x,y=y, x%y
    NWD = x
    if x == 1:
      print(f"mamy parę :0 : {m},{i}")

#zad 6
      
a = int(input())
b = int(input())
x,y = a,b
while x!=y:
  if x>y:x-=y
  if y>x:y-=x 
c = a//x
d = b//x
print(f"{a}/{b}={c}/{d}")

#zad 7 ułamki ;~;
a = int(input("Licznik: "))
b = int(input("Mianownik: "))
calosc=a//b
reszta=a%b
if reszta==0:
  print(f"Ulamek niewlasciwy to: {calosc}")
else:
  print(f"Ulamek niewlasciwy to: {calosc} i {reszta}/{b}")
  
#zad 8 i tabela w pytongu XD
T = []
for i in range(2,10001):
  suma1 = 0
  for j in range(1,i):
    if i % j == 0:
      suma1 += j
  T.append(suma1)
  suma2 = 0
  for k in range(1,suma1):
    if suma1 % k == 0:
        suma2 += k
  if i == suma2 and suma1 != suma2 and suma1 not in T:
    print(f"({suma1},{suma2})")

#zad 9
    
def czy_pierwsza(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

for i in range(10,100):
  for j in range(2,i):
    if i % j == 0:
      if czy_pierwsza(j) and czy_pierwsza(i//j):
        print(i, end=" ")
        break

#Zad10 :D :Depression
n = int(input())
ile1 = 0
ile2 = 0
for i in range(n - 2):
    if n % i == 0:
        ile1 += 1
for j in range(n + 2):
    if n % j == 0:
        ile2 += 1
if ile1 < 3 and ile2 < 3:
    print(f"Liczby blizniacze do {n} to {n - 2} i {n + 2}")
elif ile1 < 3 and ile2 > 2:
    print(f"Liczba blizniacza do {n} to tylko liczba {n - 2}")
elif ile1 > 2 and ile2 < 3:
    print(f"Liczba blizniacza do {n} to tylko liczba {n + 2}")
else:
    print("sory ale liczba nie ma blizniakow :(")