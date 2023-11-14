# Statisztikai példaprogram
#
# Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# -----------------------------------------------
#

import lorem as li
import matplotlib.pyplot as plt

# Mondat, bekezdés, illetve szöveg generálása
#s = li.sentence()  # 'Eius dolorem dolorem labore neque.'
#p = li.paragraph()
t = li.text()

# Kiírás ellenőrzésképpen
#print (t)

# Az ABC betűi
abc = "abcdefghijklmnoprtsuvwxyz" #ABCDEFGHIJKLMNORSTUVWXYZ"

# Megszámolja, hogy melyik betű hányszor szerepel a szövegben
bDist = []
for b in abc:
    bDist.append(t.count(b))

# Létrehoz egy ábrát a barcharthoz.
fig, ax = plt.subplots()

# Ez a barchar ábrázolás + az abc stringből egy listát készít a címkékhez
ax.bar(list(abc), bDist, label=list(abc))#, color=bar_colors)
# Cím
ax.set_title("A latin ABC betűinek eloszlása véletlen szövegben")
# Y tengely címkéew
ax.set_ylabel('A betűk száma')
# Beállítja az x tengely ábrázolási tartományát
#plt.xlim(['a','z'])
# Beállítja az y tengely ábrázolási tartományát. Kis helyet hagy a tetején.
plt.ylim([0,(round(max(bDist)/20)+1)*20])

# Kirajzolja az ábrát
plt.show()