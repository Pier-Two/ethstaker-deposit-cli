from PyInstaller.utils.hooks import copy_metadata

# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['ethstaker_deposit/__main__.py'],
    pathex=[],
    binaries=[],
   datas = copy_metadata('ssz') + copy_metadata('py_ecc') + \
       [('ethstaker_deposit/intl/en/cli/*.json', 'ethstaker_deposit/intl/en/cli')] + \
       [('ethstaker_deposit/key_handling/key_derivation/word_lists/*.txt', 'ethstaker_deposit/key_handling/key_derivation/word_lists')] + \
       [('ethstaker_deposit/intl/en/credentials.json', 'ethstaker_deposit/intl/en')],
    hiddenimports=['py_ecc', 'importlib_metadata', 'ssz'],
    hookspath=['hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='deposit',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)