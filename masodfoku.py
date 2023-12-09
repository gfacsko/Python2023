#
# Segédprogramok a "(VH-MIT009) Python programozás alapok" c. tárgyhoz
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
# --------------------------------------------------------------------------
#
import math

# Az egyenlet megadása
print ("Adja meg az f(x)=a x^2 + b x + c = 0 egyenlet együtthatóit! ")
print ("a= ")
strA=input()
print ("b= ")
strB=input()
print ("c= ")
strC=input()

# String -> float konverzió
a,b,c=int(strA),int(strB),int(strC)

print(str(a)+ "x^2 + " + str(b) + " x + " + str(c) + " = 0")

# Diszkrimináns
d = b ** 2 - 4 * a * c
#d = math.pow(b) - 4 * a * c

print ("A diszkrimináns értéke D = " + str(d))

'''
if (d>0):
    x1 = (-b - math.sqrt(d))/2/a
    x2 = (-b + math.sqrt(d))/2/a
    print ("Az egyenletnek két megoldása van a valós számok halmazán,"
           " x1 = " + str(x1) + " x2 = " + str(x2))
if (d==0):
    x = -b/2/a
    print ("Az egyenletnek egy megoldása van a valós számok halmazán,"
           " x = " + str(x))

if (d<0):
    print ("Az egyenletnek nincs megoldása a valós számok halmazán.")
'''

# D előjele a matchez
signD = d/abs(d)

match signD:
    case 0:
        x = -b/2/a
        print ("Az egyenletnek egy megoldása van a valós számok halmazán,"
           " x = " + str(x))
    case 1:
        x1 = (-b - math.sqrt(d))/2/a
        x2 = (-b + math.sqrt(d))/2/a
        print ("Az egyenletnek két megoldása van a valós számok halmazán,"
           " x1 = " + str(x1) + " x2 = " + str(x2))
    case _:
        print ("Az egyenletnek nincs megoldása a valós számok halmazán.")
