# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# Fuggvenyek példaprogramok
#
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, Hungary, 2023
#

import math as m

'''
# A determináns kiszámítása
def determinans(a,b,c):
    return (m.pow(b,2)-4*a*c)

# A gyökök kiszámítása
def gyokok (a,b,d):
    if (d>0):
        x1 = (-b-m.sqrt(d))/(2*a)
        x2 = (-b+m.sqrt(d))/(2*a)
        return ([x1,x2])
    if (d==0):
        x = -b/(2*a)
        return (x)
    if (d<0):
        x0 = -b/(2*a)
        x1 = m.sqrt(abs(d))/(2*a)
        x2 = m.sqrt(abs(d))/(2*a)
        return ([x0,x1,x2])



# 3. Az ax2 + bx + c = 0 alakú másodfokú egyelet megoldása az (x ∈ C) komplex számok halmazán, ahol a, b, c ∈ Z.
#
# (a) Vegyen fel tetszőleges egész a, b és c változót! Írja ki ax2 + bx + c = 0 alapban!

a = 1
b = 2
c = 2

print (str(a) + "x^2+"+str(b)+"x+"+str(c)+"=0")

# A determináns értéke
d=determinans(a,b,c)

# Az egyenlet megoldása
x=gyokok(a,b,d)

if (d>0):
    print ("Az egyenletnek két valós gyöke van.")
    print ("Az egyenlet gyökei: x1=" + str(x[0]) + " és x2=" + str(x[1]))

if (d==0):
    print ("Az egyenletnek egy valós gyöke van.")
    print ("Az egyenlet gyöke: x=" + str(x))

if (d<0):
    print ("Az egyenletnek két complex gyöke van.")
    print ("Az egyenlet complex gyökei: x1=" + str(x[0]) + "-" + str(x[0]) + "i és x2=" +
           str(x[0]) + "+" + str(x[2]) + "i")
'''

# Maldenbrot-halmaz
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
list(colormaps)

# Iteráció
# x1 x1 + x1 x2 i + i x2 x1 + i x2 i x2 = x1 x1 - x2 x2 + i (x1 x2 + x2 x1)
def xnp(x1,x2,c1,c2):
    return ([x1 * x1 - x2 * x2 + c1, x1 * x2 + x2 * x1 + c2])

# Felbontás
N = 800

# Max iteráció
M = 80

# Limit
vMax = 2

# Boundaries
xMin=-2.0#0.66#-2.0
yMin=-1.5#0.34#-1.5
xSize=3.0#4.0#0.02#3.0
ySize=3.0#0.02#3.0
xMax=xMin+xSize
yMax=yMin+ySize
xStep = xSize/N
yStep = ySize/N

# Az x és y tengely [-2,2] intervallumban
x = np.arange(xMin,xMax+xStep,xStep)
y = np.arange(yMin,yMax+yStep,yStep)

# Eredmények
mx = []
my = []
mc = []

# Maldenbrot halmaz
# Valós tengely
for c1 in x:
    # Képzetes tengely
    for c2 in y:
        i = 0
        x1 = c1
        x2 = c2
        # Iterációk
        while ((m.sqrt(m.pow(x1,2)+m.pow(x2,2))<vMax) and i<M):
            i += 1
            z = xnp(x1,x2,c1,c2)
            x1 = z[0]
            x2 = z[1]
        # Szinek eltárolása
        if (i <= M):
            mx.append(c1)
            my.append(c2)
            mc.append(i)

'''
# Julia halmaz
c1=-0.6 # c=-0.6+0.45i
c2=0.45
#c1=-1.037 # c=-1,037+0,17i
#c2=0.17
#c1=-0.52 # c=-0,52+0,57i
#c2=0.57
#c1=0.295# c=0,295+0,55i
#c2=0.55
#c1=-0.624# c=-0,624+0,435i
#c2=0.435

# Csak az x és az y változik nem a c
for x1 in x:
    # Képzetes tengely
    for x2 in y:
        i = 0
        z1 = x1
        z2 = x2
        # Iterációk
        while ((m.sqrt(m.pow(z1,2)+m.pow(z2,2))<vMax) and i<M):
            i += 1
            z = xnp(z1,z2,c1,c2)
            z1 = z[0]
            z2 = z[1]
        # Szinek eltárolása
        if (i <= M):
            mx.append(x1)
            my.append(x2)
            mc.append(i)
'''

# Ábrazolás
plt.scatter(mx,my,s=1,c=mc,cmap=plt.colormaps['RdBu'],alpha=0.5)
# Határok beállítása
plt.xlim([xMin,xMax])
plt.ylim([yMin,yMax])
# Cím
plt.title("Maldenbrot halmaz")
#plt.title("Julia halmaz c=" + str(c1) + "+i" + str(c2))
# tengelyfeliratok
plt.xlabel("Valós")
plt.ylabel("Képzetes")
# Colorbar
plt.colorbar()

# Ábrázolás
plt.show()

