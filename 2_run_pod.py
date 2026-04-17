import numpy as np

X = np.load('X_raw.npy')

# Mean Removal (Fluctuating part calculation)
print("Removing temporal mean...")
mean_flow = np.mean(X, axis=1).reshape(-1, 1)
X_prime = X - mean_flow

# SVD - The core of Algorithm 2
print("Computing SVD...")
U, S, Vh = np.linalg.svd(X_prime, full_matrices=False)

np.save('modes.npy', U)
np.save('mean_flow.npy', mean_flow)
np.save('singular_values.npy', S)

# Energy spectrum (Equation 13)
energy = (S**2) / np.sum(S**2) * 100
print(f"Dominant Mode Energy: {energy[0]:.2f}%")
