1) convert -ui file into python file. Open CMD and write the next command:
pyuic5 -x ADECUA.ui -o ADECUABis.py
pyuic5 -x ClientNew.ui -o ClientNewBis.py
pyuic5 -x ClientManage.ui -o ClientManageBis.py
pyuic5 -x ClientView.ui -o ClientViewBis.py
2) Make a .exe
  - to generate .exe, execute: .\QRCode\pyinstaller --onefile -w main.py
  - Make a .zip file of the folder "dist"
  - To generate a windows installer. download NSIS software https://sourceforge.net/projects/nsis/ and click on the 	options:" Installer based on .ZIP file". Leave all the options by default.

