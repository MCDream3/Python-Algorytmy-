#Funkcja ord()-zwraca kod ascii dla danego znaku.

# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

# # #Funkcja chr()-zwraca znak do danego kodu ascii.

# print(chr(65))
# print(chr(75))
# print(chr(89))

# # #można je łączyć..

# print(chr(ord("C")))
# print(chr(ord("C")+1))

# #napisz alfabet za pomocą pętli for

# for i in range(65,91):
#   print(chr(i), end=" ")

#jak wydobyć literki z napisu..

# napis="POLSKA"
# print(len(napis))
# print(napis[0])
# print(napis[1])

#napisz pętlę wyciągającą z napisu literki

# napis=input()
# for i in range(len(napis)):
#   print(napis[i])

# #napisz pętlę wyciągającą kody ascii z napisu
# napis=input()
# for i in range(len(napis)):
#   print(ord(napis[i]))

#zaszyfruj napis Cezarem w kluczu = 3

napis=input()
szyfr=""
for i in range(len(napis)):
  szyfr=szyfr+chr(ord(napis[i])+3)
print(napis,szyfr)

