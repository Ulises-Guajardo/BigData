# Import statements
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# load datasets
google = pd.read_csv('1.2pt2.py/GOOGL_data.csv')
facebook = pd.read_csv('1.2pt2.py/FB_data.csv')
apple = pd.read_csv('1.2pt2.py/AAPL_data.csv')
amazon = pd.read_csv('1.2pt2.py/AMZN_data.csv')
microsoft = pd.read_csv('1.2pt2.py/MSFT_data.csv')

# Create figure
plt.figure(figsize=(16, 8), dpi=300)
# Plot data
plt.plot('date', 'close', data=google, label='Google')
plt.plot('date', 'close', data=facebook, label='Facebook')
plt.plot('date', 'close', data=apple, label='Apple')
plt.plot('date', 'close', data=amazon, label='Amazon')
plt.plot('date', 'close', data=microsoft, label='Microsoft')
# Specify ticks for x- and y-axis
plt.xticks(np.arange(0, 1260, 40), rotation=70)
plt.yticks(np.arange(0, 1450, 100))
# Add title and label for y-axis
plt.title('Stock trend', fontsize=16)
plt.ylabel('Closing price in $', fontsize=14)
# Add grid
plt.grid()
# Add legend
plt.legend()
# Show plot
plt.show()