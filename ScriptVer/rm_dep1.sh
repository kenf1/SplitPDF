#!bin/bash

echo "Script to remove dependencies for pyinstaller"
python3 -m pip uninstall altgraph pyinstaller-hooks-contrib macholib pyinstaller
echo "Completed"