# Contour ábrázolás példaprogram
#
# Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# -----------------------------------------------
#

import numpy as np
import matplotlib.pyplot as plt


# Adatgenerálás
x, y = np.meshgrid(np.arange(7), np.arange(3,10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)

# Ábrázolás
cs = plt.contourf(x, y, z)
plt.contour(cs, colors='k')
plt.title("Contour plot")

# Háló
plt.grid(c='k', ls='-.', alpha=0.3)

plt.show()
