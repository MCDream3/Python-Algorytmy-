#zad 1

# x = int(input())
# wynik = 0
# while x>0:
#   wynik+= x%10
#   x //=10
# print(wynik)

#zad 2

# a = int(input())
# temp=0
# for i in range(2,a):
#   if a%i == 0:
#     temp += 1
# if temp>3:
#   print("chyba tak")
# else:
#   print("no nie")

#zad 3 - doskonale- dzielniki dodane do siebie daja tą liczbe nie liczac jej samej

# n = int(input())
# suma = 0
# for i in range(1,n):
#   if n%i == 0:
#     suma +=i
# if suma == n:
#    print("jest doskonała")
# else:
#   print("you idoit its not")

#zad 4 - względnie pierwsze- ich nwd = 1

# x = int(input())
# y = int(input())
# while  x!=y:
#   if x>y: x-=y
#   if y>x:y-=x
# if x == 1:
#   print("liczby są względnie pierwsze")
# else:
#   print("liczby takie nie są")

#zad 5

# m = int(input())
# for i in range(10,20):
#   x = m
#   y = i
#   while y>0:
#     x,y=y, x%y
#     NWD = x
#     if x == 1:
#       print(f"mamy parę :0 : {m},{i}")

#zad 6
# a = int(input())
# b = int(input())
# x,y = a,b
# while x!=y:
#   if x>y:x-=y
#   if y>x:y-=x 
# c = a//x
# d = b//x
# print(f"{a}/{b}={c}/{d}")

#zad 7

#zad 8
# T = []
# for i in range(2,10001):
#   suma1 = 0
#   for j in range(1,i):
#     if i % j == 0:
#       suma1 += j
#   T.append(suma1)
#   suma2 = 0
#   for k in range(1,suma1):
#     if suma1 % k == 0:
#         suma2 += k
#   if i == suma2 and suma1 != suma2 and suma1 not in T:
#     print(f"({suma1},{suma2})")

#zad 9
# def czy_pierwsza(n):
#   for i in range(2,n):
#     if n % i == 0:
#       return False
#   return True

# for i in range(10,100):
#   for j in range(2,i):
#     if i % j == 0:
#       if czy_pierwsza(j) and czy_pierwsza(i//j):
#         print(i, end=" ")
#         break