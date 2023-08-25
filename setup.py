from setuptools import setup

APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "icon.icns",
    "plist": {
        "CFBundleShortVersionString": "0.2.0",
        "LSUIElement": True,
        "CFBundleIconFile": "icon.icns"
    },
    "packages": ["rumps", "selenium", "webdriver_manager"],
}

setup(
    app=APP,
    name='Leave Me Alone Okta',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)
