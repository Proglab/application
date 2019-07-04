# -*- mode: python -*-

block_cipher = None

added_files = [
         ( './assets/icons/*.*', 'assets/icons' ),
         ( './assets/images/*.*', 'assets/images' )
         ]

a = Analysis(['C:\\wamp64\\www\\application\\app.py'],
             pathex=['C:\\wamp64\\www\\application', 'C:\\wamp64\\www\\application'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=['c:\\wamp64\\www\\python\\application\\lib\\site-packages\\pyupdater\\hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='win',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='win')