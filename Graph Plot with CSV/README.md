# Energy Data Analysis Project

This Python project reads an energy dataset and visualizes experimental and observational values using Matplotlib. 
---

## Dataset (CSV)

- **File:** `data/energy_data.csv`  
- **Description:** Contains energy measurements with two corresponding columns:
  - `Experimental` → Experimental values
  - `Observational` → Observed values
  - `Energy` → Energy levels (MeV)

**Important:** Make sure the CSV file is located in the `data/` folder.  
df = pd.read_csv('../data/energy_data.csv')

If your CSV is elsewhere, update the path accordingly.\

## Set up virtual environment (recommended):

python3 -m venv .venv
source .venv/bin/activate

# Install dependencies:
pip install pandas matplotlib

# Run the Python script:
python scripts/plot_energy.py


## Output:

Prints first few rows of the dataset (df.head())\
Prints dataset shape (df.shape)\
Shows a plot comparing Experimental vs Observational data\
Optional: Save plot as PNG by adding in script:\
plt.savefig('plots/energy_plot.png')\

# Example Plot

X-axis: Energy (MeV)\
Y-axis: Values

Experimental data → solid circles (o-)

Observational data → dashed squares (s--)
