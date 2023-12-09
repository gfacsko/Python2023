# Adatszerkezetek példaprogram
#
# Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# -----------------------------------------------
#


# Matematikai műveletek, tömbök
import numpy as np
# Ábrázolás könyvtárak betöltése
import matplotlib.pyplot as plt
'''
N=100

x = range(0,N)

y = np.power(x,2)


A=[[1,2,3],[2,2,2],[3,2,2]]

print(A)

print(np.linalg.det(A))
print(np.linalg.inv(A))

print(y)

'''

# Initialisation
workdir="" #X:
datafile="loremipsum.txt"

# Megnyitandó állomány neve
filename=workdir+datafile

# Beolvasás
sourcefile = open(filename)
myList = sourcefile.readlines()
sourcefile.close()

# Probléma csökkentés: minden kisbetű és kiveszem az írásjeleket
myList[0]=myList[0].replace('.','')
myList[0]=myList[0].replace(',','')
myList[0]=myList[0].replace('?','')
myList[0]=myList[0].replace('!','')
myList[0]=myList[0].lower()

# A hosszú szöveget listává alakítom
newMyList=myList[0].split(' ')
# Az eredményül kapott listá rendezem
newMyList.sort()

# Az azonos szavakból csak egyet hagyok
szoLista=[]
for i in range(0,len(newMyList)):
    if (len(szoLista)==0):
        szoLista.append(newMyList[i])
    if (len(szoLista)>0 and newMyList[i-1]!=newMyList[i]):
        szoLista.append(newMyList[i])

# Az összes szónak megnézem, hogy hányszor szerepel
nSzo=[]
for sz in szoLista:
    nSzo.append(newMyList.count(sz))

# Barchart készítése
plt.figure()

# Oszlopdiagram
plt.bar(szoLista,nSzo,color='k')
# y és x tengely határai
plt.ylim(0,12)
plt.xlim(0,len(szoLista))
# Az ábra címe és a tengelyek feliratai
plt.title("A szavak eloszlása a szövegben")
plt.ylabel("A szavak száma")
plt.xlabel("A szavak")
# Az x tengely címkéinek elforgatása
plt.xticks(rotation=-90)

# Ábra mejelenítése
plt.show()

