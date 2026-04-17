import os
import glob
import meshio
import numpy as np
import re
from tqdm import tqdm

def extract_number(filepath):
    match = re.search(r'(\d+)\.(vtk|vtu)$', filepath)
    return int(match.group(1)) if match else 0

# 1. Focus ONLY on the internal volume files
# We exclude folders like 'walldown', 'wallup', 'front', 'back'
vtk_files = glob.glob("**/*.vtk", recursive=True) + glob.glob("**/*.vtu", recursive=True)

# FILTER: Keep only files that are NOT in a subfolder, 
# or are in folders typically containing the internal field.
# Adjusting to exclude the specific folders that caused your error:
excluded_folders = ['walldown', 'wallup', 'front', 'back', 'in', 'out', 'trl-edge', 'POD_Results']
vtk_files = [f for f in vtk_files if not any(ex in f for ex in excluded_folders)]

vtk_files.sort(key=extract_number)

if not vtk_files:
    print("No internal mesh files found! Please check your VTK directory.")
    exit()

sample = meshio.read(vtk_files[0])
n_points = sample.points.shape[0]
X = np.zeros((n_points * 3, len(vtk_files)))

print(f"Building matrix from {len(vtk_files)} internal snapshots...")
for i, f in enumerate(tqdm(vtk_files)):
    try:
        data = meshio.read(f)
        X[:, i] = data.point_data['U'].ravel()
    except Exception as e:
        print(f"\nSkipping {f} due to error: {e}")
        continue

np.save('X_raw.npy', X)
print("X_raw.npy saved.")
