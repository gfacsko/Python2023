# NegyedikOra: Demonstrációs anyag
#
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, Hungary, 2023
# --------------------------------------------------------
#
#x = "666"   # string
#a = 9       # egész szám

# egész változónak adok szöveg
#a = x

#print(a)

# Szövegnek adok egész értéket
#x = 9

#print(x)

# Elágazás
'''
a = 43

if (a % 2 == 0):
    print("A(z) szám páros.")
else:
    print("A(z) szám páratlan.")
'''

# While ciklus
'''
i = 1
N = 20

while (i<=N):
    print(i)
    i=i+1
'''

# For ciklus
'''
N = 20

for i in range(N):
    print(i)
'''

# Listák
szamok = [1.3, 4.5, 10.2, 3.14, 2.71, 9.8]
szovegek = ["aaa", "bbb", "ccc", "ddd", "eee", "fff"]
merge = []

print(szamok)
print(szovegek)

i = 0
while (i < len(szamok)):
    merge.append(szovegek[i])
    merge.append(szamok[i])
    i = i + 1

print(merge)


'''
# Kiválasztás
nKuszob = 0
kuszob = 4
for i in szamok:
    if (i < kuszob):
        print(i)
        nKuszob = nKuszob + 1

print(nKuszob)
'''

'''
# Maximum keresés
iMax = 0
vMax = szamok[0]
for i in szamok:
    if (vMax<i):
        vMax=i

print(szamok.index(vMax))
print(vMax)
'''
'''
# Maximum keresés while ciklussal
iMax = 0
vMax = szamok[0]
i = 0
while (i<len(szamok)):
    if (vMax<szamok[i]):
        vMax = szamok[i]
        iMax = i
    i = i + 1

print(iMax)
print(vMax)
'''



'''
szovegek.reverse()

szovegek.insert(2,'4')

szovegek.sort()

szovegek.remove("aaa")

szovegek.extend('hhh')


print(szovegek)
'''

'''
for i in range(len(szovegek)):    # i = 0 ... len(szamok)-1
    print(szovegek[i])

for i in szamok:
    print(i)
'''

'''
# A print képes kezelni a listát
print(szamok)
# A type() utasítás kiírja a változó típusát
print(type(szamok))
# A len() utasítás kiírja a lista hosszát
print(len(szamok))

# Kiíratás for ciklussal
for i in szamok:
    print(i)

# A lista elemei 0 kezdetű indexeléssel elérhetőek
print(szamok[1])
'''

# A lista elemeinek feldolgozása while ciklussal
'''
i = 0
while i < len(szamok):  # i = 0 ... i = 4
    print(szamok[i])
    i += 1
'''
'''
# A negítív indexekkel a végéről lehet elérni a lista elemeit
#print(szamok[-2])

szamok.append(0.12345678)

#print(szamok)

#szamok.pop(-3)

print(szamok)

#szamok.append('q')

#print(szamok)

#szamok.sort()
#szamok.clear()
#numbers=szamok.copy()

print(szamok.count(4.5))

print(szamok.index(3.14))

#szamok.insert(2,'e')

szamok.sort()
szamok.reverse()

print(szamok)
'''