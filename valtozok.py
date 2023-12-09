#
# Segédprogramok a "(VH-MIT009) Python programozás alapok" c. tárgyhoz
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
# --------------------------------------------------------------------------
#

'''
# Egész szám
n = 10

print (n)

# Hozzá lehet adni valós számot
n += 5.5

print (n)

# Nem tudja a print összefűzi -> konverzió str()-rel
print ("A változó értéke: " + str(n))

r = 3.14

print ("A másik változozó értéke: " + str(r))


strE = "2.71"

# Stringből float
print(r+float(strE))

strN = "100"

# Stringből egész szám
n = n + int(strN)

print (n)

print ("Írjon be egy pozitív egész számot! ")

# Input consolról
strSzam = input()

print (strSzam)

szam = int(strSzam)

# Elágazás
if (szam % 2 == 0):
    print ("Az " + strSzam + " páros.")
else:
    print ("Az " + strSzam + " páratlan.")
'''

'''

# Ciklusok + numpy
import numpy as np

for r in np.arange(0.1,10.1,0.5):
    print (r)

i = 0
N = 100
while (i<N):
    print (i)
    i += 1

print ("---" + str(i))
'''

'''

# Listák
lista = [137,42,0.1,1,3,3.14,"www"]

# Lista hossza
print (len(lista))

print(lista)

'''
for l in lista:
    print (l)

for i in range(0,len(lista)):
    print (lista[i])
'''

lista.append("Új elem.")

print (lista)

lista.pop()
lista.pop()

print (lista)

lista.sort()

print (lista)

print(lista.index(42))

print(lista.clear())
'''
