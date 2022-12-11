#Funkcja ord()-zwraca kod ascii dla danego znaku.

# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

#Funkcja chr()-zwraca znak do danego kodu ascii.

# print(chr(65))
# print(chr(75))
# print(chr(89))

# <--można je łączyć..-->
# C=C
# Cnr2=D
# wpisaną 'chr','ord' literę wupisuje a w drugim przypadku podaje kolejną literę z rzędu

# print(chr(ord("C")))
# print(chr(ord("C")+1))

# <--napisz alfabet za pomocą pętli for-->
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# i w range-u 65,91, wypisuje duże litery z alfabetu

# for i in range(65,91):
#   print(chr(i), end=" ")

#<--jak wydobyć literki z napisu..-->
# MCDream=7 M C D r
# tekst w 'napis', wypisuje ilość liter oraz zależnie od ilości print-ów wypisuje litery jedną pod drugą

# napis="MCDream"
# print(len(napis))
# print(napis[0])
# print(napis[1])
# print(napis[2])
# print(napis[3])

#<--napisz pętlę wyciągającą z napisu literki-->
# MCDream=M C D r e a m
# napisany tekst, wypisuje kolejne litery jedną pod drugą

# napis=input()
# for i in range(len(napis)):
#   print(napis[i])

# <--napisz pętlę wyciągającą kody ascii z napisu-->
# A=65
# a=97
#MCDream= 77 67 68 114 101 97 109
# wpisany tekst, wypisuje każdą literę jako kod z liczby

# napis=input()
# for i in range(len(napis)):
#   print(ord(napis[i]))

#<--zaszyfruj napis Cezarem w kluczu = 3-->
# a=d
# b=e
# c=f
# wpisana litera oznacza kolejną trzecią

# napis=input()
# szyfr=""
# for i in range(len(napis)):
#   szyfr=szyfr+chr(ord(napis[i])+3)
# print(napis,szyfr)

