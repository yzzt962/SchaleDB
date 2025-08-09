block_cipher = None

a = Analysis(
    ['app2.py'],  # 替换为你的主程序入口文件
    pathex=[],
    binaries=[],
    datas=[
        ('shared_manager.py', '.'),  # 包含共享模块
        ('config.ini', '.')         # 包含配置文件
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='changename',  # 生成的exe名称
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 设为True可显示控制台窗口
    onefile=True
)