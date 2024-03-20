
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as snsplt

plt.figure()
labels = ['A', 'B', 'C']
x = np.arange(len(labels))
bars1 = [10, 20, 30]
bars2 = [15, 10, 20]
bars3 = [20, 10, 10]
plt.bar(x, bars1)
plt.bar(x, bars2, bottom=bars1)
plt.bar(x, bars3, bottom=np.add(bars1, bars2))
plt.xticks(x, labels)
plt.show()