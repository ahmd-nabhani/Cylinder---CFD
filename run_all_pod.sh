#!/bin/bash

# Ensure venv exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
    ./venv/bin/pip install meshio numpy tqdm
fi

PYTHON_BIN="./venv/bin/python3"

echo "--------------------------------------"
echo "Running Universal POD Pipeline"
echo "--------------------------------------"

# Check for OpenFOAM data if no VTK exists
if [ $(find . -name "*.vtk" -o -name "*.vtu" | wc -l) -eq 0 ]; then
    echo "No VTK/VTU files. Trying foamToVTK..."
    foamToVTK && echo "Conversion done."
fi

$PYTHON_BIN 1_build_snapshots.py
$PYTHON_BIN 2_run_pod.py
$PYTHON_BIN 3_export_vtk.py
echo "Step 4: Generating Spectra Plot..."
$PYTHON_BIN 4_plot_spectra.py

echo "Process Complete."
