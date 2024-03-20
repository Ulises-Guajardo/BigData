import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as snsplt

x = np.random.normal(0, 1, size=100)
y = np.random.normal(0, 1, size=100)
z = np.random.normal(0, 1, size=100)
c = np.random.normal(0, 1, size=100)
plt.figure()
plt.scatter(x, y, s=z*500, c=c, alpha=0.5)
plt.colorbar()
plt.show()