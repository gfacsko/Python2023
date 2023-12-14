#
# Géptermi zárthelyi feladatok, 2023. október 30-án
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# ---------------------------------------------------------
# "B" csoport
# ---------------------------------------------------------
#
# 1. Szövegfeldolgozás:
# (a) Deklaráljon négy szövegváltozót és inicializálja az alábbi vers soraival. Írja ki a változókat a képernyőre!
#
# “Álltak az állatok,
# előttük zárt ajtók.
# Lövöldöztek rájuk,
# eljött a haláluk.”
#
# – Egy kisfiú versikéje

s1="Álltak az állatok,"
s2="előttük zárt ajtók."
s3="Lövöldöztek rájuk,"
s4="eljött a haláluk.”"

print (s1)
print (s2)
print (s3)
print (s4)

# (b) Egyesı́tse egy string változóban a sorokat szóközzel elválasztva! Írja ki a változó tartalmát a # képernyőre!

s=s1+" "+s2+" "+s3+" "+s4

print(s)


# (c) Cserélje ki a magyar ékezetes karaktereket a Latin1 kiosztás karaktereire! Írja ki az eredményt a képernyőre!

s=s.replace("á","a")
s=s.replace("é","e")
s=s.replace("í","i")
s=s.replace("ö","o")
s=s.replace("ó","o")
s=s.replace("ő","o")
s=s.replace("ú","u")
s=s.replace("ü","u")
s=s.replace("ű","u")

print(s)

# (d) Hány dupla mássalhangzó van a szövegben? Írja ki a dupla mássalhangzókat és a számukat tartaslmazó párokat
# egymás alá!

nDuplaMassalhangzo=0
for c in ["bb", "cc", "dd", "ff", "gg", "hh", "jj", "kk", "ll", "mm", "nn", "rr", "pp", "qq", "ss", "tt", "ww", "zz", "yy", "xx", "vv"]:
    nDuplaMassalhangzo += s.count(c)
    print (c + " " + str(s.count(c)))

print ("A szövegben " + str(nDuplaMassalhangzo) + " db dupla mássalhangzó van.")

# 2. Műveletek listákkal.
# (a) Műholdak irányı́tásában és a kvantummechanikában alkalmazzuk a kvaterniókat. Ezek a + b i + c j + d  k alakban
# felı́rható számnégyesek, ahol a, b, c, d ∈ R, i^2 = j^2 = k^2 = ijk = −1, # továbbá i j = k, j k = i, k i = j,
# j i = −k, k j = −i, és i  k = −j. Valósı́tson meg két kvaterniót és ı́rja ki őket a képernyőre a + b i + c j + d k
# alakban, ahol a, b, c, d ∈ R!

q = [2, 3, 5, 7]
r = [11, 13, 17, 19]

print ("Első kvaternió: " + str(q))
print ("Második kvaternió: " + str(r))

# (b) Adja össze őket és ı́rja ki az összeadás eredményét a képernyőre!

sum = []
for i in range(0,4):
    sum.append(q[i]+r[i])

print ("A két kvaternió összege: " + str(sum))

# (c) Vonja ki őket egymásból őket és ı́rja ki a kivonás eredményét a képernyőre!

st = []
for i in range(0,4):
    st.append(q[i]-r[i])

print ("A két kvaternió különbsége: " + str(st))

# (d) Szorozza össze őket egymással és ı́rja ki a szorzás eredményét a képernyőre!
#
# (q1+i q[1]+j q3 + k q4) (r1+i r2+j r3 + k r4)=
# q1 r1 + i q1 r2 + j q1 r3 + k q1 r4 +
# i q2 r1 + i i q2 r2 + i j q2 r3 + i k q2 r4 +
# j q3 r1 + j i q3 r2 + j j q3 r3 + j k q3 r4 +
# k q4 r1 + k i q4 r2 + k j q4 r3 + k k q4 r4 =
#
# q1 r1 + i q1 r2 + j q1 r3 + k q1 r4 -
# i q2 r1 - q2 r2 + k q2 r3 - j q2 r4 +
# j q3 r1 - k q3 r2 - q3 r3 + i q3 r4 +
# k q4 r1 + j q4 r2 - i q4 r3 - q4 r4 =
#
# (q1 r1 - q2 r2 - q3 r3 - q4 r4) +
# i (q1 r2 + q2 r1 + q3 r4 - q4 r3) +
# j (q1 r3 - q2 r4 + q3 r1 + q4 r2) +
# k (q1 r4 + q2 r3 - q3 r2 + q4 r1)

multi = [(q[0] * r[0] - q[1] * r[1] - q[2] * r[2] - q[3] * r[3]),
         (q[0] * r[1] + q[1] * r[0] + q[2] * r[3] - q[3] * r[2]),
         (q[0] * r[2] - q[1] * r[3] + q[2] * r[0] + q[3] * r[1]),
         (q[0] * r[3] + q[1] * r[2] - q[2] * r[1] + q[3] * r[0])]

print ("A két kvaternió szorzata: " + str(st))

# 3. Műveletek tömbökkel.
# (a) Tekintsük A = ... B = ... mátrixokat! Valósı́tsa meg őket tetszőleges adatszerkezettel (pl. lista, 2D-s tömb)
# és ábrázolja őket!

A=[[1,2,3],[2,1,2],[3,2,1]]

B=[[2,0,0],[0,5,0],[0,0,7]]

print ("  " + str(A[0]))
print ("A=" + str(A[1]))
print ("  " + str(A[2]))

print ("\n  " + str(B[0]))
print ("B=" + str(B[1]))
print ("  " + str(B[2]))

# (b) Adja össze a mátrixokat egymással és ı́rja ki a képernyőre az összeadás eredményét!

Osszeg=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,len(A)):
    for j in range(0,len(A[0])):
         Osszeg[i][j] = A[i][j] + B[i][j]

print ("                      " + str(Osszeg[0]))
print ("A két mátrix összege: " + str(Osszeg[1]))
print ("                      " + str(Osszeg[2]))

# (c) Vonja ki a mátrixokat egymásból és ı́rja ki a képernyőre a a kivonás eredményét!

Kulonbseg=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,len(A)):
    for j in range(0,len(A[0])):
         Kulonbseg[i][j] = A[i][j]-B[i][j]
        # print(str(Kulonbseg[i][j]))

print ("                         " + str(Kulonbseg[0]))
print ("A két mátrix különbsége: " + str(Kulonbseg[1]))
print ("                         " + str(Kulonbseg[2]))


# (d) Szorozza össze a mátrixokat egymással és ı́rja ki a képernyőre a szorzás eredményét!

Szorzat=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,len(A)):
    for j in range(0,len(A[0])):
        for k in range(0,len(A[0])):
            Szorzat[i][j] = Szorzat[i][j] + A[i][k]*B[k][j]

print ("                       " + str(Szorzat[0]))
print ("A két mátrix szorzata: " + str(Szorzat[1]))
print ("                       " + str(Szorzat[2]))


# (e) Számolja ki a mátrixok determinánsait! Invertálhatóak-e ezek a mátrixok?

detA = A[0][0]*A[1][1]*A[2][2]+A[1][0]*A[2][1]*A[0][2]+A[2][0]*A[0][1]*A[1][2]\
       -A[2][0]*A[1][1]*A[0][2]-A[1][0]*A[2][1]*A[2][2]-A[0][0]*A[2][1]*A[1][2]

print("Az A mátrix determinánsa " + str(detA) + ", ezért invertálható.")

# (f) A v nemnulla vektort az A egy sajátvektorának nevezzük, ha létezik olyan λ ∈ R skalár, hogy
# teljesül az Av = λv egyenlőség. A λ skalárt az A egy v sajátvektorához tartozó sajátértékének
# nevezzük, ha Av = λv. Határozza meg a két megadott mátrix sajátértékeit és sajátvektorait!
# (Segı́tség: olda meg a |A − λI| egyenletet, ahol I az egységmátrix.)

'''
detAl = (A[0][0]-l)*(A[1][1]-l)*(A[2][2]-l)+A[1][0]*A[2][1]*A[0][2]+A[2][0]*A[0][1]*A[1][2]\
       -A[2][0]*(A[1][1]-l)*A[0][2]-A[1][0]*A[2][1]*(A[2][2]-l)-(A[0][0]-l)*A[2][1]*A[1][2]=
       
       (A[0][0]*A[1][1]-l*A[0][0]*A[1][1]+l*l)*(A[2][2]-l)+A[1][0]*A[2][1]*A[0][2]+A[2][0]*A[0][1]*A[1][2]\
       -A[2][0]*A[1][1]*A[0][2]+l*A[2][0]*A[0][2]-A[1][0]*A[2][1]*A[2][2]+A[1][0]*A[2][1]*l\
       -A[0][0]*A[2][1]*A[1][2]+l*A[2][1]*A[1][2]=
       
       A[0][0]*A[1][1]*A[2][2]-l*A[0][0]*A[1][1]*A[2][2]+l*l*A[2][2]-A[0][0]*A[1][1]*l+l*l*A[0][0]*A[1][1]-l*l*l\
       +A[1][0]*A[2][1]*A[0][2]+A[2][0]*A[0][1]*A[1][2]-A[2][0]*A[1][1]*A[0][2]+l*A[2][0]*A[0][2]\
       -A[1][0]*A[2][1]*A[2][2]+A[1][0]*A[2][1]*l-A[0][0]*A[2][1]*A[1][2]+l*A[2][1]*A[1][2]=
       
       -l*l*l+l*l*A[2][2]+l*(A[0][0]*A[1][1]*A[2][2]+A[0][0]*A[1][1]+A[2][0]*A[0][2]+A[1][0]*A[2][1]+A[2][1]*A[1][2])\
       +A[0][0]*A[1][1]*A[2][2]+A[1][0]*A[2][1]*A[0][2]+A[2][0]*A[0][1]*A[1][2]-A[2][0]*A[1][1]*A[0][2]\
       -A[1][0]*A[2][1]*A[2][2]-A[0][0]*A[2][1]*A[1][2]=0
       
       -l^3+AA*l^2+BB*l+CC=0
'''
AA=A[2][2]
BB=A[0][0]*A[1][1]*A[2][2]+A[0][0]*A[1][1]+A[2][0]*A[0][2]+A[1][0]*A[2][1]+A[2][1]*A[1][2]
CC=A[0][0]*A[1][1]*A[2][2]+A[1][0]*A[2][1]*A[0][2]+A[2][0]*A[0][1]*A[1][2]-A[2][0]*A[1][1]*A[0][2]\
   -A[1][0]*A[2][1]*A[2][2]-A[0][0]*A[2][1]*A[1][2]

print("Az l^3-"+str(AA)+"*l^2-"+str(BB)+"*l-"+str(CC)+"=0 egyenletet kell megoldani, hogy megkapjuk a sajátértékeket.")
print("Sajnos a harmadfokú egyenletek megoldása nem tananyag ezért erre a feladatra mindenki maximális pont kap.")


