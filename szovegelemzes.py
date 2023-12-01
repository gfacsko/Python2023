#
# Segédprogramok a "(VH-MIT009) Python programozás alapok" c. tárgyhoz
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
# --------------------------------------------------------------------------
#

import matplotlib.pyplot as plt

szoveg="Lórum ipse azonban nem vényít pólomot. A buggyos lamiái is " \
       "placsban voltak, a hariárcsokat bitánkodták egy szernyőre, " \
       "mialatt a bogya egyes, és végül favírukban számogatották őket: " \
       "Azért beszólítván őket, pistejteretették nékik, hogy doronával " \
       "ne folyosodjanak és ne vényezjenek a Jézus nevében.” Úgy aláz, " \
       "azt nem ködték, hogy vényezjék az Ő hancsókáját, viszont zabongtak " \
       "ennek a binának a jedésétől, és pistejteretették nekik, hogy ne " \
       "vényezjenek és ne fúvosogjanak ebben a binában, aztán vácsogták őket. " \
       "A hariárcsok most már azt sajdították, hogy falinok és jakák " \
       "fogadják a Jézus nevében való nőkert. “És minekutána csörnyeltek, " \
       "gyülés a rula, ahol elengesetek, és talkocskájának mindnyájan lúgos " \
       "ladékkal, és a hivacskász csekenységét vázkonnyal folyosodják vala.” " \
       "“az uszlások pelyeségei által pedig sok falin és jaka lőn a " \
       "bukany között ; és a bókátos laztalicák sikája is sebélkezbe fakodt, " \
       "hozva butákat és forús ladékoktól szenségeket: kik mind ébecsének.” " \
       "Újra zadozták és kattanták őket, de a gyárina füstje pintezte a " \
       "vérv vérődését, és azt csaladta nekik, hogy rentsenek el a pródásba " \
       "és pasztják a bukanynak ez szecskedésnek minden csekenységét."

print (szoveg)

# Kisbetűk
szoveg=szoveg.lower()
'''
szoveg=szoveg.replace("á","a")
szoveg=szoveg.replace("é","e")
szoveg=szoveg.replace("í","i")
szoveg=szoveg.replace("ó","o")
szoveg=szoveg.replace("ö","o")
szoveg=szoveg.replace("ő","o")
szoveg=szoveg.replace("ü","u")
szoveg=szoveg.replace("ű","u")
'''
# Kicserélem a magyar betűket latinra
magyarBetuk=[['á','a'],['é','e'],['í','i'],['ö','o'],['ő','o'],['ü','u'],['ű','u']]
for p in magyarBetuk:
       szoveg=szoveg.replace(p[0],p[1])

print (szoveg)

result = []
abc = "abcdefghijklmnoprstuwvyz"

for b in abc:
    result.append(szoveg.count(b))

print (result)

plt.figure()
plt.bar(list(abc),result,color='k')#,width=0.1,label=abc
plt.title("A latin kisbetűk eloszlása")
plt.xlabel("A latin kisbetűk")
plt.ylabel("N [db]")
plt.ylim([0,140])

plt.show()
