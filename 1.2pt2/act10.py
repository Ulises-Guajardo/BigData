import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as snsplt

x = np.random.normal(0, 1, size=100)
y = x + np.random.normal(0, 1, size=100)
plt.figure()
plt.scatter(x, y)
plt.show()