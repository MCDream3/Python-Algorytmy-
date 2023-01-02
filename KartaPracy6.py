#Zad1

# a = int(input())
# b = int(input())
# c = int(input())
# if b-a == c-b:
#   print("to jest ciag arytmetyczny")
# if b/a == c/b:
#   print("jest to ciag geometryczny")

#Zad2

# suma = 0
# for i in range(100,1000):
#   if (i % 8 == 0 and i % 16 != 0):
#     suma += i
# print (suma)

#Zad3
# podzielnik = 0
# for i in range(9,99):
#   if i % 7 == 0:
#     podzielnik = i
#     break
# suma = 0

# for j in range(100,1000):
#   if j % podzielnik == 0:
#     suma += j
# print(suma)

#Zad4

# ilosc = 0
# cd = 0
# cj = 0
# for i in range(10,100):
#   cd = i / 10;
#   cj = i % 10;
#   if (cd >= 2 * cj):
#     ilosc += 1
# print(ilosc)

#Zad5

# ilosc = 0
# suma = 0
# cd = 0
# cj = 0
# for i in range(100,1000):
#   cd = i/100
#   cj = i%100
#   if cd >= 2*cj:
#     ilosc +=1
#     suma +=1
# print(suma + ilosc)

#Zad6

# n = int(input())
# for i in range(10,19+19*n):
#   if i % 19 == 0:
#     print(i)

# #Zad7
# skladnik = 0
# suma = 0
# n = int(input())
# for i in range(100,999):
#   if i % 37:
#     skladnik = i
#     break

# for j in range(0,n):
#   suma += skladnik - 37 * j
#   print (suma)

#Zad8

# import Math
# suma = 0
# n = int(input())
# for i in range(1, i <=n):
#   suma = suma + (3 * i - 1) * Math.pow(-1, i, 1)
# print(suma)

#To było zrobione w domu ale zweryfikowane na infie