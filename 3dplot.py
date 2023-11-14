# 3D ábrázolás példaprogram
#
# Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
#
# -----------------------------------------------
#

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

# sin(x) / x
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))/np.sqrt(x ** 2 + y ** 2)

x = np.linspace(-15, 15, 30)
y = np.linspace(-15, 15, 30)
X, Y = np.meshgrid(x, y)
Z = f(X,Y)
# Előkészítés

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

# Ábra kirajzolása
plt.show()
