import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

"""
2. como conseguir que tenga el color correcto
"""


matriz = np.array([
    [255,0, 255, 255, 255],
    [255, 0, 0, 255, 255],
    [255,255, 0,0, 255],
    [255, 255, 255, 0,255],
    [255, 255, 0, 0, 255],
    [255, 255, 255, 0, 255]
])

x, y = matriz.shape
x, y = np.meshgrid(range(x), range(y))


colores = []

scatter = plt.scatter(x, -y, c=colores, s=500, cmap='gray', edgecolors='black') 
plt.axis('off') 
plt.show()
