import numpy as np
import corner

# Fake data: posterior samples (5,000) from a 2D Gaussian distribution
samples = np.random.multivariate_normal(
    mean=[0.15, 0.30],
    cov=[[0.01,0.005],[0.005, 0.02]],
    size=5000
)

labels = [r'$\eta/s$', r'$T_{\mathrm{switch}}$']

figure = corner.corner(
    samples,
    labels=labels,
    show_titles=True,
    title_fmt=".3f"
)

plt.show()
