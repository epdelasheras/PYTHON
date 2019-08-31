1)to generate .exe, execute:
.\Files\pyinstaller main.py
2)When it finishes open .\Files\main.spec and edit the next lines:
a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('zynqAdcLog.txt','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
3)Save the file and execute .\Files\pyintaller main.spec and say "yes" to the question in between.



