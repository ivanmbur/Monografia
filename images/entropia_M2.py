import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc("text", usetex = True)

Lambda = np.linspace(0.001,0.999,1000)

fig, ax = plt.subplots(figsize = (7,5))
ax.plot(Lambda, -(Lambda*np.log(Lambda) + (1-Lambda)*np.log(1-Lambda)), c = "k")
ax.set_xlabel("$\lambda$", fontsize = 15)
ax.set_ylabel("$S$", fontsize = 15)
fig.savefig("entropia_M2")
plt.show()
