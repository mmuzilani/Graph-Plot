# ==========================================
# 1️⃣ Import required libraries
# ==========================================
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 2️⃣ Define your data
# ==========================================
energy = np.array([0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01,0.012,0.014,
                   0.016,0.018,0.02,0.022,0.024,0.026,0.0281,0.03,0.0326,0.0349,
                   0.037,0.0399,0.0424,0.0451,0.0472,0.0477,0.05,0.0551,0.0597,
                   0.0603,0.065,0.0702,0.0751,0.0806,0.0856,0.09,0.0947,0.0999,
                   0.1099,0.1197,0.1309,0.1392,0.1509,0.1613,0.1698,0.179,0.1961,
                   0.1998,0.2036,0.2075,0.2116,0.2157,0.22,0.2244,0.229,0.2337,
                   0.2385,0.2435])          # paste your energy list here
experimental = np.array([589.843,512.904,460.009,419.924,387.831,361.227,338.645,319.151,
                         286.995,261.445,240.586,223.207,208.496,195.884,184.951,175.389,
                         166.565,159.506,150.973,144.355,138.955,132.349,127.326,122.491,
                         119.095,118.329,114.997,108.589,103.752,103.176,99.0463,95.1465,
                         91.991,88.9332,86.5164,84.6271,82.816,81.0244,78.083,75.7025,
                         73.4378,72.0038,70.2608,68.9335,67.975,67.0486,65.5943,65.3174,
                         65.046,64.7806,64.5152,64.2632,64.0127,63.7702,63.531,63.3012,
                         63.0809,62.8663])    # paste experimental data
observational = np.array([1173.57,983.18,863.389,779.499,716.441,666.613,625.777,591.398,
                          498.728,450.068,411.224,379.207,352.249,329.152,309.113,291.555,
                          275.32,262.247,246.487,234.199,224.113,211.687,202.158,192.896,
                          186.335,184.851,178.351,165.683,155.952,154.784,146.391,138.322,
                          131.675,125.118,119.847,115.669,111.614,107.552,100.78,95.2522,
                          89.9148,86.4898,82.2737,79.0165,76.6394,74.3073,70.5306,69.7956,
                          69.0663,68.3441,67.6122,66.916,66.215,65.5251,64.8321,64.1518,
                          63.4858,62.8189])   # paste observational data


plt.rcParams.update({
    'font.size': 14,              # overall font size
    'font.family': 'serif',       # looks professional (Times style)
    'axes.labelsize': 14,         # axis label font
    'axes.titlesize': 16,         # title font
    'legend.fontsize': 12,        # legend text size
    'lines.linewidth': 3          # default line thickness
})


plt.figure(figsize=(8, 5))   # 8 wide × 5 high (good ratio)
plt.plot(energy, experimental, 'o-', color='navy', label='Experimental')
plt.plot(energy, observational, 's--', color='darkred', label='Observational')

#  Add error bars (if you have uncertainties)

# plt.errorbar(energy, experimental, yerr=error_values, fmt='o', capsize=3)

 #Add a fitted curve (e.g., polynomial)

# coeffs = np.polyfit(energy, experimental, 3)
# fit = np.polyval(coeffs, energy)
# plt.plot(energy, fit, 'k-', label='3rd-order Fit')


#Label axes, title, legend, and grid

plt.xlabel('Energy (MeV)')
plt.ylabel('Cross-section (arb. units)')
plt.title('Comparison of Experimental and Observational Data')
plt.legend(frameon=True, loc='best')          # “frameon” = boxed legend
plt.grid(True, linestyle=':', alpha=0.4)      # dotted light grid

plt.xscale('log')
plt.yscale('log')

plt.tight_layout()
plt.savefig('energy_comparison.pdf', dpi=600, bbox_inches='tight')
plt.show()
