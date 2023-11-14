# Vezérlési szerkezetetek, string kezelés
#
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# ---------------------------------------------------------
#

'''

# Nem csinál semmit
pass

# -----------------------------------------------------------

# Értékadás több változónak
a,b = 2,137

print(a,b)

# A változók értékének a cseréje, egy sorban, segédváltozó nélkül
a,b = b,a

print(a,b)

# -----------------------------------------------------------

if (a<b):
    print("A(z) ",a," kisebb a(z) ",b,"-nél.")
else:
    print("A(z) ", a, " nagyobb a(z) ",b, "-nél.")

# -----------------------------------------------------------

i = 0
N = 100
while (i<N):
    print(i)
    if (i==10):
        break
        #continue
    i+=1

for j in range(N):
    print(j)

for s in ["aaa", "bbb", "rrr"]:
    print(s)
'''
import random

#s = "Indul a görög aludni."

#print(s)

'''
# Benne van-e az adotgt karakter?
print("ni" in s)
# Konkatenáció
print(s + " Mert álmos.")
# Többszörözi a karaktereket
print(s*5)
'''
'''
# 5. karakter
print(s[4])
# 0-5 karakter szelet
print(s[0:5])
# Minden harmadik karakter írja ki
print(s[0:len(s):3])
# A string hossza
print(len(s))
# A legkisebb ASCII számú karakter
print(min(s))
# A legnagyobb ASCII számú karakter
print(max(s))
'''

# Az első karaktert nagy betűssé alakítja
#print(s.capitalize())

# Megszámolja a karakterek előfordulásait
#print(s.count("ö"))

# Szétvágja a szeparátor mentén a stringet.
#print(s.rsplit(" "))

#print(s.endswith("ni."))
#print(s.find("gö"))

#s="Indul a {0} aludni"
#print(s.format("török"))

# Kiírja az indexet, vagy -1
#print(s.find("nu."))
# Kiírja az indexet, vagy kivételt dob.
#print(s.index("nu."))

'''
print(s.isalnum()) # Szám vagy betű.
print(s.isalpha()) # Betű
print(s.isspace()) # Csak space
print(s.istitle()) # Csupa nagybetűvel kezdődik egy szó
print(s.isupper()) # Csak nagybetűk vannak a szavakban


list = ["aaa","bbb","www","137","42","uuu"]
sep=", "

s2=sep.join(list)


print(s2)
print(type(s2))


print(s.lower())
print(s.upper())
print(s.partition(" "))
print(s.replace("ö","o"))
'''

import numpy as np

n = 20

a = np.array(range(1,n+1))

i = 0
while (i<len(a)):
    #print(a[i])
    a[i]=random.randint(1,255)
    i +=1

print(a)

print(a.max())

print(a.tolist())

print(np.sqrt(a))

print(np.max(a))