#!bin/bash

#activate venv
cd VENV
source VENV/bin/activate

#create exe
pyinstaller --onefile --hidden-import=pdf2image --name "SplitPDF" "SplitPDF/ScriptVer/SplitPDF-script.py"

#clean project folder
    #copy exe to desktop
    #rm build dist .spec
cp -r /dist ~/Desktop
rm -rf build dist
rm *.spec
