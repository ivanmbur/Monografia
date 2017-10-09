import numpy as np
import matplotlib.pyplot as plt

Lambda = np.linspace(0.001,0.999,1000)

fig, ax = plt.subplots()
ax.plot(Lambda, -(Lambda*np.log(Lambda) + (1-Lambda)*np.log(1-Lambda)), c = "k")
ax.set_xlabel("$\lambda$")
ax.set_ylabel("$S$")
fig.savefig("entropia_M2")
plt.show()
