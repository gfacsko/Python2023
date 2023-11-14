# Ábrázolás példaprogram
#
# Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# -----------------------------------------------
#

# Példa beolvasásra

#print ("Írjon be valamit! ")
#line = input()

#print ("Ezt írta be: ")
#print (line)

import numpy as np
import matplotlib.pyplot as plt

# Initialisation
workdir="X:"
datafile="data_themisc-20080706.txt"

# Megnyitandó állomány neve
filename=workdir+datafile

# Állomány megnyitása
sourcefile = open(filename)
mylist = sourcefile.readlines()
# Ez egy THEMIS szonda mérési adata. A header #-pal kezdődik, ezt eltávolítjuk
mylist_without_sharp = []
for e in mylist:
    if (not e.startswith('#')):
        mylist_without_sharp.append(e)
sourcefile.close()

# Az időt külön kezelem, de ez nagyon bonyolult, ezért egy sima számtömbbel helyettesítem
t=range(0,len(mylist_without_sharp))
# Ez a tömb az állomány 12 oszlopában lévő adatokat tárolja el
a=np.zeros((len(mylist_without_sharp),12))

# Állomány aktuális hossza, egyfajta ciklus változó
i = 0
# Az állomány feldolgozása és felkészülés az elemzésre --------------------------------------
for line in mylist_without_sharp:
    # A sort több szóra vágja szét (ezek az oszlopok)
    split_line = line.split()
    # Az oszlopkat a megfelelő altömbökbe tárolja el
    for j in range(0,12):
        astr=split_line[j+1]
        aa=float(astr)
        a[i,j]=aa
    # Következő sor
    i=i+1
# Az állomány feldolgozásának a vége

# Ábrázolás

# Első ábra
plt.subplot(2,2,1)
plt.plot(t,a[:,0],color='Black',markersize=0.01,linestyle='-',linewidth=0.2,label='B')
plt.plot(t,a[:,1],color='Blue',markersize=0.01,linestyle='-',linewidth=0.2,label='Bx')
plt.plot(t,a[:,2],color='Green',markersize=0.01,linestyle='-',linewidth=0.2,label='By')
plt.plot(t,a[:,3],color='Red',markersize=0.01,linestyle='-',linewidth=0.2,label='Bz')


# A tengelyek intervallumai
plt.xlim([0,8000])#len(t)])
plt.ylim([-60,60])
# Az ábra címe és a tengelyek feliratai
plt.title('THC 20080706')
#plt.xlabel('Time [HH:MM]')
plt.ylabel('B, Bx, By, Bz [nT]')

# Magyarázat
plt.legend()

# Második ábra
plt.subplot(2,2,3)
#plt.plot(t,a[:,4],color='Black',markersize=0.01,linestyle='-',linewidth=0.2,label='V')
plt.plot(t,a[:,5],color='Blue',markersize=0.01,linestyle='-',linewidth=0.2,label='Vx')
plt.plot(t,a[:,6],color='Green',markersize=0.01,linestyle='-',linewidth=0.2,label='Vy')
plt.plot(t,a[:,7],color='Red',markersize=0.01,linestyle='-',linewidth=0.2,label='Vz')


# A tengelyek intervallumai
plt.xlim([0,8000])#len(t)])
plt.ylim([-400,200])
# Az ábra címe és a tengelyek feliratai
#plt.title('THC 20080706')
plt.xlabel('Time [HH:MM]')
plt.ylabel('Vx, Vy, Vz [km/s]') # V,

# Magyarázat
plt.legend()

# Harmadik ábra
#plt.subplot(2,2,2)
#plt.scatter(t, a[:,8], s=a[:,11],c=a[:,11], alpha=0.5)

# A tengelyek intervallumai
#plt.xlim([0,8000])#len(t)])
#plt.ylim([-400,200])
# Az ábra címe és a tengelyek feliratai
#plt.title('Szines pöttyök')
#plt.xlabel('Time [HH:MM]')

# Negyedik ábra - histogram
plt.subplot(2,2,4)
plt.hist(a[:,1],bins=21) # ,histtype='step',stacked=True, fill=False

# A tengelyek intervallumai
plt.xlim([-10,10])

# Az ábra címe és a tengelyek feliratai
plt.title('B eloszlása')
plt.xlabel('B [nT]')

# Plot figure
plt.show()