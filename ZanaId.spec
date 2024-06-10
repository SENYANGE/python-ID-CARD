# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['ZanaId.py'],
             pathex=['/home/programmer/python projects/desktop apps/IdentityCard'],
             binaries=[],
             datas=[('zms_badge.png', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
#Add the file like the below example
a.datas += [('zms_badge.png', '/home/programmer/python projects/desktop apps/IdentityCard/zms_badge.png', 'DATA'),('profile_pic.png', '/home/programmer/python projects/desktop apps/IdentityCard/profile_pic.png', 'DATA')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='ZanaId',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
