import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a dataset: data dictionary
data = {
  "Centrality": ["0-5", "5-10", "10-20", "20-30", "30-40"],
  "mean_pT": [0.72, 0.70, 0.67, 0.63, 0.59]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid", context="talk")
sns.pointplot(data=df, x="Centrality", y="mean_pT")

plt.ylabel(r'$\langle p_T \rangle$ [GeV]')
plt.xlabel('Centrality (%)')

plt.tight_layout()
plt.show()
