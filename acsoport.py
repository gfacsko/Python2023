#
# Géptermi zárthelyi feladatok, 2023. október 30-án
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# ---------------------------------------------------------
# "A" csoport
# ---------------------------------------------------------
#
# 1. Szövegfeldolgozás:
# (a) Deklaráljon hat szövegváltozót és inicializálja az alábbi vers soraival. Írja ki a változókat a # képernyőre!
#
# Testem-létem utánad nyúl
# a tér sem szabhat határt
# időfolyamok végtelen sodrában
# élek hát miattad tovább
# majd beérlek, lecsapok rád
# és megvı́vjuk a holtak harcát.
#
# (Vilmer Battinos, 2007-2123)
#

s1="Testem-létem utánad nyúl"
s2="a tér sem szabhat határt"
s3="időfolyamok végtelen sodrában"
s4="élek hát miattad tovább"
s5="majd beérlek, lecsapok rád"
s6="és megvı́vjuk a holtak harcát."

print(s1, s2, s3, s4, s5, s6)


# (b) Egyesı́tse egy string változóban a sorokat szóközzel elválasztva! Írja ki a változó tartalmát a # képernyőre!

s=s1+" "+s2+" "+" "+s3+" "+s4+" "+s5+ " "+s6

print(s)

# (c) Cserélje ki a magyar ékezetes karaktereket a Latin1 kiosztás karaktereire! Írja ki az eredményt a képernyőre!

s=s.replace("á","a")
s=s.replace("é","e")
s=s.replace("í","i")
s=s.replace("ö","o")
s=s.replace("ó","o")
s=s.replace("ő","o")
s=s.replace("ú","u")
s=s.replace("ü","u")
s=s.replace("ű","u")

print(s)

# (d) Hány magán- és mássalhangzó van a szövegben? Írja ki a képernyőre!

nMaganhangzo=0
for c in "aeiou":
    nMaganhangzo += s.count(c)

print ("A szövegben " + str(nMaganhangzo) + " db magánhangzó van.")

nMassalhangzo=0
for c in "bcdfghjklmnrpqstwzyxv":
    nMassalhangzo += s.count(c)

print ("A szövegben " + str(nMassalhangzo) + " db mássalhangzó van.")

# (e) Melyik karakterből mennyi található a szövegben? Írja ki a megtalálható karaktereket és mellé a számukat a
# szövegben tartalmazó párokat egymás alá!

print ("A betűk eloszlása a szövegben a következő: ")

for c in "aeioubcdfghjklmnrpqstwzyxv":
    print (c + " " + str(s.count(c)))

print("\n")

# 2. Listák összefűzése
# (a) Generáljon két maximum 20 elem hosszúságú listát, amely 0 és 255 közötti egészszámokat tartalmaz! Írja ki őket
# a képernyőre!

import random as rnd

nA = 15
nB = 20

a=[]
b=[]

for i in range(1,nA):
    a.append(rnd.randint(0, 255))

for i in range(1,nB):
    b.append(rnd.randint(0, 255))

print("Az első lista elemei:   " + str(a))
print("A második lista elemei: " + str(b))

# (b) Fűzze össze a listákat úgy, hogy előbb az egyikből, majd a másikból vegyen ki egy elemet és helyeze az új
# listába! Amikor az rövidebb lista elemei elfogynak, a maradék listából vegye az elemeket! Írja ki az új lista
# elemeit egymás mellé!

newList = []

for i in range(0,len(a)):
    newList.append(a[i])
    newList.append(b[i])

for i in range(len(a),len(b)):
    newList.append(b[i])

print ("Az összefűzött lista elemei: " + str(newList))

print("\n")

# 3. Az ax2 + bx + c = 0 alakú másodfokú egyelet megoldása az (x ∈ C) komplex számok halmazán, ahol a, b, c ∈ Z.
#
# (a) Vegyen fel tetszőleges egész a, b és c változót! Írja ki ax2 + bx + c = 0 alapban!

a = 1
b = 2
c = 2

print (str(a) + "x^2+"+str(b)+"x+"+str(c)+"=0")

# (b) Hány komplex (x ∈ C) és hány valós (x ∈ R) gyöke van az egyenletnek? Kezelje az összes lehetséges variációt
# a kódban!

import math as m

d=m.pow(b,2)-4*a*c

if (d>0):
    print ("Az egyenletnek két valós gyöke van.")

if (d==0):
    print ("Az egyenletnek egy valós gyöke van.")

if (d<0):
    print ("Az egyenletnek két complex gyöke van.")

# (c) Írja ki az egyenlet gyökeit! A komplex gyököket ı́rja ki e + f · i alakban, ahol e, f ∈ R és i = 1 imaginárius
# egység.

if (d>0):
    print ("Az egyenlet gyökei: x1=" + str((-b-m.sqrt(d))/(2*a)) + " és x2=" + str((-b+m.sqrt(d))/(2*a)))

if (d==0):
    print ("Az egyenlet gyöke: x=" + str(-b/(2*a)))

if (d<0):
    print ("Az egyenlet complex gyökei: x1=" + str(-b/(2*a)) + "-" + str(m.sqrt(abs(d))/(2*a)) + "i és x2=" +
           str(-b/(2*a)) + "+" + str(m.sqrt(abs(d))/(2*a)) + "i")

