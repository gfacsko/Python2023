#
# Python zh programjai
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
# ---------------------------------------------------------------------------------------------------------------
#

# 1. Függvények, rekurzió
# (a) Számı́tsa ki az első 1000 természetes szám összegét rekurzı́v függvénnyel és ı́rja ki a képernyőre!

# Eddig számolunk
N = 500

# Rekurzív függvény
def recSum(n):
    if (n==1):
        return 1
    if (n>1):
        return (n+recSum(n-1))

# Itt hívom meg
print (recSum(N))

# (b) A Fibonacci-számok egy ismert sorozat elemei. Számolja ki a sorozat első 100 elemét és ı́rja ki a képernyőre.

# Függvény
def fib(a,b):
    return (a+b)

# Eddig számolok
N=100

# Inicilizálás
f=[0,1]

# Az értékek kiszámítása
for n in range(2,100):
    #f.append(f[n-1]+f[n-2])
    f.append(fib(f[n-1],f[n-2]))

# Eredmény kiírása
print (f)

# (c) Számolja ki a fenti Fibonacci-sorozat első 100 elmét rekurzióval és ı́rja ki őket a képernyőre.

# Rekurzív függvény
def recFib(n):
    if (n==0):
        return 0;
    if (n==1):
        return 1;
    if (n>1):
        return (recFib(n-2)+recFib(n-1))

# Eddig számolunk
N = 10

f=[]

# Meghívjuk a függvényt
for n in range(0,N):
    f.append(recFib(n))

# Eredmény kiírása
print (f)

# 2. Állományok beolvasása, ábrázolás, adatelemzés.
# (a) Az oktatójuk 2023. szeptember 16-án szombaton délután kerékpározni ment. Az mellkasi
# pulzusmérőjéhez csatlakozott Polar Beat alkalmazás a facsko bevprogzh-20231127.txt szö-
# veges állományban rögzı́tette a rekreációs edzés adatait. Az állomány első oszlopát és az
# időbélyegeket figyelmen kı́vül hagyva, olvassák be a földrajzi szélesség és hosszúság, illetve a
# magassági adatokat!

import numpy as np
import matplotlib.pyplot as plt

# Initialisation
workdir=""
datafile="pythonzh-20231127.txt"

# Megnyitandó állomány neve
filename=workdir+datafile

# Állomány megnyitása
sourcefile = open(filename)
mylist = sourcefile.readlines()
# Az első sort eltávolítjuk
mylist_without_t = []
for e in mylist:
    if (not e.startswith('t')):
        mylist_without_t.append(e)
sourcefile.close()

# Az időt külön kezelem, de ez nagyon bonyolult, ezért egy sima számtömbbel helyettesítem
t=range(0,len(mylist_without_t))
# Ez a tömb az állomány 2 oszlopában lévő adatokat tárolja el
a=np.zeros((len(mylist_without_t),6))

# Állomány aktuális hossza, egyfajta ciklus változó
i = 0
# Az állomány feldolgozása és felkészülés az elemzésre --------------------------------------
for line in mylist_without_t:
    # A sort több szóra vágja szét (ezek az oszlopok)
    split_line = line.split()
    # Az oszlopkat a megfelelő altömbökbe tárolja el
    for j in range(2,5):
        astr=split_line[j+1]
        aa=float(astr)
        a[i,j]=aa
    # Következő sor
    i=i+1
# Az állomány feldolgozásának a vége

# (a) Ábrázolják az edzés útvonalát úgy, hogy átszámı́tják a földrajzi fokokat km-re. Hány km-t tekert az oktatójuk? Az
# ábrának legyenek feliratozott tengelyei és cı́me is. A szöveges választ kommentként adják meg a forráskódban.

# fok->km
a[:,2] *= 111
a[:,3] *= 111

# Kellemesebb koordinátarendszer
a[:,2] = a[:,2]-min(a[:,2])+1
a[:,3] = a[:,3]-min(a[:,3])+1

plt.figure()
plt.scatter(a[:,3], a[:,2], s=1,alpha=0.5, c='k')
plt.title("Bringatúra")
plt.xlabel("Kelet-Nyugat [km]")
plt.ylabel("Észak-Dél [km]")
plt.xlim([0,12])
plt.ylim([0,8])

# Ábra megjelenítése
plt.show()

#sum = 0.0
drArray = []
for i in range(1,len(a[:,3])):
    dx = a[i,3]-a[i-1,3]
    dy = a[i,2]-a[i-1,2]
    dr = (dx**2 + dy**2)**0.5
    #sum += dr
    drArray.append(dr)
    #print([dx,dy,sum])


print ("A túra hossza " + str(np.sum(drArray)) + " km volt.")

# (c) Mi volt az oktatójuk sebessége az edzés alatt? Készı́tsen egy idő-sebesség diagrammot!

# Sebsség számítás
drArray=np.multiply(drArray,3600)

# Ábra
plt.plot(drArray,'k.',markersize=0.5)
plt.ylim([0,20])
plt.xlim([0,12000])
plt.title("Sebesség")
plt.xlabel("Time [s]")
plt.ylabel("V [km/h]")

# Ábra megjelenítése
plt.show()

# (d) Az idő mekkora részében száguldott az oktatójuk 0-5 km/h, 5-10 km/h, 10-15 km/h, 15-20 km/h,
# 20 km/h vagy nagyobb sebességgel? Készı́tsen oszlopdiagrammot és olvassa le róla az eredményt.

limits = [0,5,10,15,20,1000]
counts=np.histogram(drArray,limits)
#labels =['0-5','5-10','10-15','15-20','20-']

print(limits)
print(counts[0].tolist())

plt.bar(limits[0:5],counts[0].tolist()/np.sum(counts[0]/100.0),color='k',width=4)#label=labels)
plt.title("Sebességeloszlás")
plt.ylim([0,100])
plt.ylabel("%")

# Ábra megjelenítése
plt.show()
