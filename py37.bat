@echo off
REM py -3.7-64 -m pip install pandas
REM py -3.7-64 -m pip install Pillow
REM py -3.7-64 -m pip install -U matplotlib
py -3.7-64 -m PyInstaller --onefile resize_image.py
REM git remote add backup "C:\Users\treve\Dropbox\projects\gen_desc"
REM git config --local --bool core.bare false
REM py -3.7-64 plot/trial.py 

REM compile code
REM py -3.7-64 -m PyInstaller main.spec
REM py -3.7-64 -m PyInstaller main.py
REM iscc "setup/design_auto.iss"
REM "setup/setups/ssc_design_setup-1.0.7"

REM "dist/main/trsc"
REM py -3.7-64 -m pip freeze rem show all packages installed
REM git rm --cached *.exe 
