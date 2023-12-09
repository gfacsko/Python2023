#
# Fuggvenyek példaprogram
#
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, Hungary, 2023
#

import math as m

'''
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
        z1 = -b/(2*a)
        z2 = m.sqrt(abs(d))/(2*a)
        return ([z1,z2])


# 3. Az ax2 + bx + c = 0 alakú másodfokú egyelet megoldása az (x ∈ C) komplex számok halmazán, ahol a, b, c ∈ Z.
#
# (a) Vegyen fel tetszőleges egész a, b és c változót! Írja ki ax2 + bx + c = 0 alapban!

a = 1
b = 2
c = 0

print (str(a) + "x^2+"+str(b)+"x+"+str(c)+"=0")

# A determináns értéke
d=determinans(a,b,c)

# Az egyenlet megoldása
x=gyokok(a,b,d)

# Eredmények a diszkrimináns értéke alapján
if (d>0):
    print ("Az egyenletnek két valós gyöke van.")
    print ("Az egyenlet gyökei: x1=" + str(x[0]) + " és x2=" + str(x[1]))

if (d==0):
    print ("Az egyenletnek egy valós gyöke van.")
    print ("Az egyenlet gyöke: x=" + str(x))

if (d<0):
    print ("Az egyenletnek két complex gyöke van.")
    print ("Az egyenlet complex gyökei: x1=" + str(x[0]) + "-i" + str(x[1]) + "és x2=" +
           str(x[0]) + "+i" + str(x[1]))
'''

# ====================================================================================================
'''
# Faktoriális számítás rekurzióval

def fact(n):
    if (n>0):
        return n*fact(n-1)
    else:
        return 1

print (fact(20))
'''



# ====================================================================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps

# Iteráció
# x_{n+1} = x_{n}^2+c, ha n>1
#           c, ha n=1
# ahol c komplex szám
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
xMin=-1#-2
xLength=0.5#2.5
xMax=xMin+xLength
yMin= 0#-1.5
yLength=0.5#3.0
yMax=yMin+yLength
xStep = xLength/N
yStep = yLength/N

# Az x és y tengely [-2,2] intervallumban
x = np.arange(xMin,xMax+xStep,xStep)
y = np.arange(yMin,yMax+yStep,yStep)

# Eredmények
mx = []
my = []
mc = []

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
        if (z[0] < M):
            mx.append(c1)
            my.append(c2)
            mc.append(i)

# Ábrazolás
plt.scatter(mx,my,s=1,c=mc,cmap=plt.colormaps['jet'])
# Határok beállítása
plt.xlim([xMin,xMax])
plt.ylim([yMin,yMax])
# Cím
plt.title("Maldenbrot halmaz")
# tengelyfeliratok
plt.xlabel("Valós")
plt.ylabel("Képzetes")
# Colorbar
plt.colorbar()

# Ábrázolás
plt.show()
