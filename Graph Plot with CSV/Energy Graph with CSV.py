import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/zilani/Downloads/energy_data.csv')
print(df.head())               # quick check: first rows
print(df.shape)                # check row/column counts

energy = df['Energy']
exp = df['Experimental']
obs = df['Observational']

plt.figure(figsize=(8,5))
plt.plot(energy, exp, 'o-', label='Experimental')
plt.plot(energy, obs, 's--', label='Observational')
plt.xlabel('Energy (MeV)')
plt.ylabel('Value')
plt.legend()
plt.grid(True, alpha=0.4)
plt.tight_layout()
plt.show()
        