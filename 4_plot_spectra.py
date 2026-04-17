import numpy as np
import matplotlib.pyplot as plt

# Load the singular values
try:
    S = np.load('singular_values.npy')
except FileNotFoundError:
    print("Error: singular_values.npy not found. Run Step 2 first.")
    exit()

# 1. Calculate Individual Energy (%)
energy = (S**2) / np.sum(S**2) * 100

# 2. Calculate Cumulative Energy (%)
cumulative_energy = np.cumsum(energy)

# 3. Create the Plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Primary Axis: Individual Energy
color = 'tab:blue'
ax1.set_xlabel('Mode Number')
ax1.set_ylabel('Individual Energy (%)', color=color)
ax1.semilogy(range(1, len(energy) + 1), energy, 'o-', color=color, markersize=4, label='Mode Energy')
ax1.tick_params(axis='y', labelcolor=color) # Fixed the 'y' here!
ax1.grid(True, which="both", ls="-", alpha=0.3)

# Secondary Axis: Cumulative Energy
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Cumulative Energy (%)', color=color)
ax2.plot(range(1, len(cumulative_energy) + 1), cumulative_energy, 's--', color=color, alpha=0.5, label='Cumulative')
ax2.tick_params(axis='y', labelcolor=color) # Fixed the 'y' here!
ax2.set_ylim(0, 105)

# Add a horizontal line at 90% energy (standard threshold)
ax2.axhline(y=90, color='gray', linestyle=':', alpha=0.7)
ax2.text(1, 91, '90% Threshold', color='gray', fontsize=9)

# Formatting
plt.title('POD Energy Spectrum (Scree Plot)')
plt.xlim(0, min(50, len(energy))) # Focus on top 50 modes
fig.tight_layout()

plt.savefig('pod_spectra.png', dpi=300)
print("Spectra plot saved as 'pod_spectra.png'")
