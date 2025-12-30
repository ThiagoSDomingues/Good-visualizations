import numpy as np
import matplotlib.pyplot as plt

# Toy model for heavy-ion pT spectra
pT = np.linspace(.2, 5, 30)
spectra = np.exp(-pT/.6)

plt.figure(figsize=(6,4))
plt.semilogy(pT, spectra, 'o-', label=r'$\pi^+$, 0-5%')

plt.xlabel(r'$p_T$ [GeV]')
plt.ylabel(r'$\frac{1}{2\pi p_T}\frac{d^2N}}{dp_T dy}$')
plt.legend()
plt.grid(alpha=.3)

plt.tight_layout()
plt.show()
