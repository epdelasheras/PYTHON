1) convert -ui file into python file. Open CMD and write the next command:
pyuic5 -x QT.ui -o main_bis.py
2) Make a .exe
  - to generate .exe, execute on the file .py path: pyinstaller --onefile -w main.py
  - Make a .zip file of the folder "dist"
  - To generate a windows installer. download NSIS software https://sourceforge.net/projects/nsis/ and click on the 	options:" Installer based on .ZIP file". Leave all the options by default.

