import meshio
import numpy as np
import os
import glob

# Find a template from the original data
templates = glob.glob("**/*.vtk", recursive=True) + glob.glob("**/*.vtu", recursive=True)
templates = [f for f in templates if "POD_Results" not in f]
mesh = meshio.read(templates[0])

modes = np.load('modes.npy')
mean_flow = np.load('mean_flow.npy')

if not os.path.exists('POD_Results'): os.makedirs('POD_Results')

# Save Mean Flow
mesh.point_data = {'Mean_U': mean_flow.reshape(-1, 3)}
mesh.write('POD_Results/Mean_Flow.vtu')

# Save Top 5 Modes
for i in range(5):
    m = meshio.Mesh(points=mesh.points, cells=mesh.cells)
    m.point_data = {f'Mode_{i+1}': modes[:, i].reshape(-1, 3)}
    m.write(f'POD_Results/Mode_{i+1}.vtu')

print("Modes exported to 'POD_Results'.")
