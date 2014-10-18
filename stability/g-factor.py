"""
Stability of a Fabry-Perot cavity based on the radii of curvature of the end mirrors.

Sean Leavey
https://github.com/SeanDS/
"""

import pylab
import numpy as np

# radii of curvature of mirrors
m_roc_ITM = 5.7
m_roc_ETM = 5.7

# laser wavelength
lambda0 = 1064e-9

# cavity length vector
x = np.linspace(10, 11.5, 100)
g1 = 1 - np.divide(x, m_roc_ITM)
g2 = 1 - np.divide(x, m_roc_ETM)

# g-factor
y1 = g1 * g2

# spot size on mirrors (from Christian Graef's thesis, p49)
y2 = np.sqrt((lambda0 * x / np.pi) * (np.sqrt(g2 / (g1 * (1 - y1)))))

fig, ax = pylab.subplots(2, 1, sharex=True, figsize=(7.5, 10))

ax[0].plot(x, y1)
ax[0].grid(True)
ax[0].set_title('Cavity Stability')
ax[0].set_ylabel('g-factor')
#ax[0].set_ylim([0, 1])

ax[1].fill_between(x, y2, facecolor='blue')
ax[1].set_xlabel('Cavity Length [m]')
ax[1].grid(True)
ax[1].set_ylabel('Spot Size [m]')

#pylab.savefig('g-factor.pdf', format='PDF')
pylab.show()
