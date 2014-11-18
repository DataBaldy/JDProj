__author__ = 'Jon'
import matplotlib as mpl

mpl.use('Agg')  # Must be used before pyplot import to use Agg

import matplotlib.pyplot as plt
import numpy as np

# define x

x = np.arange(1, 10, 0.01)

#plot points with legend labels

plt.plot(x, [xi**2 for xi in x], label='Power 2')
plt.plot(x, [xi**3 for xi in x], label='Power 3')
plt.plot(x, [xi**3.2 for xi in x], label='Power 3.2')

#grid

plt.grid(True)

#labels

plt.xlabel('Samples')
plt.ylabel('Values')
plt.title('Simple Plot')
plt.legend(loc='best')

# save chart

#plt.savefig('plot1.png',dpi=200, transparent=True)

# show chart

plt.show()
