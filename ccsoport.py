# Géptermi zárthelyi feladatok, 2023. október 30-án
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# ---------------------------------------------------------
# "C" csoport
# ---------------------------------------------------------
#
# 1. Szövegfeldolgozás:
# (a) Deklaráljon kilenc szövegváltozót és inicializálja az alábbi vers soraival. Írja ki a változókat a képernyőre!
#
# ”— The Viking Prayer
# “Lo, there do I see my father.
# Lo, there do I see my mother,
# and my sisters, and my brothers.
# Lo, there do I see the line of my people,
# Back to the beginning!
# Lo, they do call to me.
# They bid me take my place among them,
# In the halls of Valhalla!
# Where the brave may live forever!”
#
# — Michael Alexander, Risen from Ashes
import numpy as np

s1 ="Lo, there do I see my father."
s2 ="Lo, there do I see my mother,"
s3=" and my sisters, and my brothers."
s4="Lo, there do I see the line of my people,"
s5="Back to the beginning!"
s6="Lo, they do call to me."
s7="They bid me take my place among them,"
s8="In the halls of Valhalla!"
s9="Where the brave may live forever!”"

print(s1,s2,s3,s4,s5,s6,s7,s8,s9)

# (b) Egyesı́tse egy string változóban a sorokat szóközzel elválasztva! Írja ki a változó tartalmát a képernyőre!

s=" ".join([s1,s2,s3,s4,s5,s6,s7,s8,s9])

print(s)

# (c) Darabolja fel a szöveget szavakra! Melyik szóból hány darab található a szövegben? Írja ki a szó–szavak száma
# a szövegben párokat egymás alá!

# Kisbetűssé alakítom
s=s.lower()
# Kiszedem az írásjeleket belőle
s=s.replace('.','')
s=s.replace('!','')
s=s.replace('?','')
s=s.replace(',','')

# Szavakra bontom (listává alakítom).
words=s.split()
# Rendezem a szavakat
words.sort()

#print(words)

# Kiválogatom az egyedi szavakat. Ezeket nézem meg, hogy hányszor szerepelnek a szövegben.
uwords=np.unique(words)

#print(uwords)

# A szó-szavak száma párok kiírása
for uw in uwords:
    print(uw+" "+str(words.count(uw)))

# 2. Adatszerkezetek
# Hozzon létre komplex számsı́kot reprezentáló adatszerkezetet, amelynek mérete egy önkényesen felvett N ∈ Z+ pozitı́v
# természetes szám (pl. 20). Írja ki a számokat!

import math as m

# Konstans
N = 20

# Elmentem a számokat
komplexRange = []
# Komplex számok
for i in range(0,N):
    komplexRange.append(-2+i*4/N) # Az numpy arange-e erre jobb megoldás, de azt akkor még nem tanultunk.
    for j in range(0,N):
        print ([-2+i*4/N,-2+j*4/N])

# (b) A fent megvalósı́tott komplex számsı́k elemeiről döntse el, hogy melyik a Maldenbrot halmaz része!

# Maldenbrot halmaz

# Iterációk maximális száma
M=80
# A maximális érték, amíg nem divergens az elem
vMax=2

# Képzetes tengely - Megcserélem, hogy vizszintes legyen a Maldenbrot halmaz.
for c2 in komplexRange:
    # A Maldenbrot halmaz karakteres megjelenítése
    line=' '
    # Valós tengely
    for c1 in komplexRange:
        i = 0
        x1 = c1
        x2 = c2
        # Iterációk
        while ((m.sqrt(m.pow(x1,2)+m.pow(x2,2))<vMax) and i<M):
            i += 1
            x1 = x1 * x1 - x2 * x2 + c1
            x2 = x1 * x2 + x2 * x1 + c2

        if (i<M):
            line=line+' '
        else:
            line=line+'.'

    print(line)
    line=''
