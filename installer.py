import PyInstaller.__main__
import os

print('Ruta' ,os.path)
PyInstaller.__main__.run([
    '--name=%s' % 'height-converter',
    '--onefile',
    '--windowed',
    '--clean',
    '--icon=%s' % os.path.join('', '', 'icon.ico'),
    os.path.join('', 'main.py'),
])