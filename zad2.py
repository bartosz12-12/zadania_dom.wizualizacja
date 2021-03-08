import math
from math import *
#zad1
# int
a = 1
b = 2
# float
c = 1.5
d = 1.3
# complex
e = 1+1j
f = 2+2j
# string
str1 = "string1"
str2 = "string2"

#print(a, b, c, d, e, f, str1, str2)




#Zad2
a=9
b=7

dodawanie = a + b
#print(dodawanie)

odejmowanie = a - b
#print(odejmowanie)

mnozenie = a * b
#print(mnozenie)

dzielenie = a / b
#print(dzielenie)

potegowanie = a ** 2
#print(potegowanie)

pierwiastkowanie = a**(1/b)
#print(pierwiastkowanie)

#Zad3




#Zad4
var1 = math.e **10
var2 = log(5+sin(8)**2)**1/6
var3 = floor(3.55)
var4 = ceil(4.80)
#print(var1, var2, var3, var4)


#Zad5
imie = "BARTOSZ"
nazwisko = "LIPINSKI"
#print(imie.capitalize() + " " + nazwisko.capitalize())



#Zad6
tekst = "spiewam sobie la la la la la la la la la"
#print(tekst.count(" la"))


#Zad7
imie = "Natalia"
#print(imie[0], imie[-1])




#Zad8
tekst = "ala ma kota"
#print(tekst.split())


#Zad9
a = 1000000
b = 10.01
c = "napis"
print("Szesnastkowy: %(a)x float: %(b)f i string %(c)s" %{'a':a, 'b':b, 'c':c})