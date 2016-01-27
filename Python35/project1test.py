Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
C:\Stuff
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
C:\Stuff
Traceback (most recent call last):
  File "C:/Python35/Project1.py", line 12, in <module>
    main()
  File "C:/Python35/Project1.py", line 7, in main
    os.path.exists(p)
NameError: name 'os' is not defined
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
C:\Stuff
Traceback (most recent call last):
  File "C:/Python35/Project1.py", line 13, in <module>
    main()
  File "C:/Python35/Project1.py", line 8, in main
    os.path.exists(p)
  File "C:\Python35\lib\genericpath.py", line 19, in exists
    os.stat(path)
TypeError: argument should be string, bytes or integer, not WindowsPath
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
C:\Stuff
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
C:\Stuff
False
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
>>> 
C:\Riot
False
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
C:\Data
True
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
yo
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
yo
yo
ERROR

====================== RESTART: C:/Python35/Project1.py ======================
yo
ERROR
C:\Data
>>> p = Path('.')
>>> [x for x in p.iterdir() if x.is_dir()]
[WindowsPath('DLLs'), WindowsPath('Doc'), WindowsPath('include'), WindowsPath('Lib'), WindowsPath('libs'), WindowsPath('Scripts'), WindowsPath('tcl'), WindowsPath('Tools')]
>>> p = Path('Riot games')
>>> [x for x in p.iterdir() if x.is_dir()]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    [x for x in p.iterdir() if x.is_dir()]
  File "<pyshell#4>", line 1, in <listcomp>
    [x for x in p.iterdir() if x.is_dir()]
  File "C:\Python35\lib\pathlib.py", line 1036, in iterdir
    for name in self._accessor.listdir(self):
  File "C:\Python35\lib\pathlib.py", line 371, in wrapped
    return strfunc(str(pathobj), *args)
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'Riot games'
>>> p = Path('Data')
>>> [x for x in p.iterdir() if x.is_dir()]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    [x for x in p.iterdir() if x.is_dir()]
  File "<pyshell#6>", line 1, in <listcomp>
    [x for x in p.iterdir() if x.is_dir()]
  File "C:\Python35\lib\pathlib.py", line 1036, in iterdir
    for name in self._accessor.listdir(self):
  File "C:\Python35\lib\pathlib.py", line 371, in wrapped
    return strfunc(str(pathobj), *args)
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'Data'
>>> p = Path('lib')
>>> [x for x in p.iterdir() if x.is_dir()]
[WindowsPath('lib/asyncio'), WindowsPath('lib/collections'), WindowsPath('lib/concurrent'), WindowsPath('lib/ctypes'), WindowsPath('lib/curses'), WindowsPath('lib/dbm'), WindowsPath('lib/distutils'), WindowsPath('lib/email'), WindowsPath('lib/encodings'), WindowsPath('lib/ensurepip'), WindowsPath('lib/html'), WindowsPath('lib/http'), WindowsPath('lib/idlelib'), WindowsPath('lib/importlib'), WindowsPath('lib/json'), WindowsPath('lib/lib2to3'), WindowsPath('lib/logging'), WindowsPath('lib/msilib'), WindowsPath('lib/multiprocessing'), WindowsPath('lib/plat-aix4'), WindowsPath('lib/plat-darwin'), WindowsPath('lib/plat-freebsd4'), WindowsPath('lib/plat-freebsd5'), WindowsPath('lib/plat-freebsd6'), WindowsPath('lib/plat-freebsd7'), WindowsPath('lib/plat-freebsd8'), WindowsPath('lib/plat-generic'), WindowsPath('lib/plat-linux'), WindowsPath('lib/plat-netbsd1'), WindowsPath('lib/plat-next3'), WindowsPath('lib/plat-sunos5'), WindowsPath('lib/plat-unixware7'), WindowsPath('lib/pydoc_data'), WindowsPath('lib/site-packages'), WindowsPath('lib/sqlite3'), WindowsPath('lib/test'), WindowsPath('lib/tkinter'), WindowsPath('lib/turtledemo'), WindowsPath('lib/unittest'), WindowsPath('lib/urllib'), WindowsPath('lib/venv'), WindowsPath('lib/wsgiref'), WindowsPath('lib/xml'), WindowsPath('lib/xmlrpc'), WindowsPath('lib/__pycache__')]
>>> p = Path('C:\Riot Games')
>>> [x for x in p.iterdir() if x.is_dir()]
[WindowsPath('C:/Riot Games/League of Legends')]
>>> PurePath([x for x in p.iterdir() if x.is_dir()][0])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    PurePath([x for x in p.iterdir() if x.is_dir()][0])
NameError: name 'PurePath' is not defined
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
>>> p = Path('C:\Riot Games')
>>> PurePath([x for x in p.iterdir() if x.is_dir()][0])
PureWindowsPath('C:/Riot Games/League of Legends')
>>> p = Path('.')
>>> [x for x in p.iterdir() if x.is_dir()==False]
[WindowsPath('LICENSE.txt'), WindowsPath('NEWS.txt'), WindowsPath('Project1.py'), WindowsPath('python.exe'), WindowsPath('python3.dll'), WindowsPath('python35.dll'), WindowsPath('pythonw.exe'), WindowsPath('README.txt'), WindowsPath('vcruntime140.dll')]
>>> [x for x in p.iterdir() if x.is_dir()]
[WindowsPath('DLLs'), WindowsPath('Doc'), WindowsPath('include'), WindowsPath('Lib'), WindowsPath('libs'), WindowsPath('Scripts'), WindowsPath('tcl'), WindowsPath('Tools')]
>>> p = [x for x in p.iterdir() if x.is_dir()][0]
>>> [x for x in p.iterdir() if x.is_dir()==False]
[WindowsPath('DLLs/py.ico'), WindowsPath('DLLs/pyc.ico'), WindowsPath('DLLs/pyexpat.pyd'), WindowsPath('DLLs/select.pyd'), WindowsPath('DLLs/sqlite3.dll'), WindowsPath('DLLs/tcl86t.dll'), WindowsPath('DLLs/tk86t.dll'), WindowsPath('DLLs/unicodedata.pyd'), WindowsPath('DLLs/winsound.pyd'), WindowsPath('DLLs/_bz2.pyd'), WindowsPath('DLLs/_ctypes.pyd'), WindowsPath('DLLs/_ctypes_test.pyd'), WindowsPath('DLLs/_decimal.pyd'), WindowsPath('DLLs/_elementtree.pyd'), WindowsPath('DLLs/_hashlib.pyd'), WindowsPath('DLLs/_lzma.pyd'), WindowsPath('DLLs/_msi.pyd'), WindowsPath('DLLs/_multiprocessing.pyd'), WindowsPath('DLLs/_overlapped.pyd'), WindowsPath('DLLs/_socket.pyd'), WindowsPath('DLLs/_sqlite3.pyd'), WindowsPath('DLLs/_ssl.pyd'), WindowsPath('DLLs/_testbuffer.pyd'), WindowsPath('DLLs/_testcapi.pyd'), WindowsPath('DLLs/_testimportmultiple.pyd'), WindowsPath('DLLs/_testmultiphase.pyd'), WindowsPath('DLLs/_tkinter.pyd')]
>>> ord('_')
95
>>> ord('Z')
90
>>> ord('z')
122
>>> len([x for x in p.iterdir() if x.is_dir()==False])
27
>>> [x for x in p.iterdir() if x.is_dir()==False]
[WindowsPath('DLLs/py.ico'), WindowsPath('DLLs/pyc.ico'), WindowsPath('DLLs/pyexpat.pyd'), WindowsPath('DLLs/select.pyd'), WindowsPath('DLLs/sqlite3.dll'), WindowsPath('DLLs/tcl86t.dll'), WindowsPath('DLLs/tk86t.dll'), WindowsPath('DLLs/unicodedata.pyd'), WindowsPath('DLLs/winsound.pyd'), WindowsPath('DLLs/YO.txt'), WindowsPath('DLLs/_bz2.pyd'), WindowsPath('DLLs/_ctypes.pyd'), WindowsPath('DLLs/_ctypes_test.pyd'), WindowsPath('DLLs/_decimal.pyd'), WindowsPath('DLLs/_elementtree.pyd'), WindowsPath('DLLs/_hashlib.pyd'), WindowsPath('DLLs/_lzma.pyd'), WindowsPath('DLLs/_msi.pyd'), WindowsPath('DLLs/_multiprocessing.pyd'), WindowsPath('DLLs/_overlapped.pyd'), WindowsPath('DLLs/_socket.pyd'), WindowsPath('DLLs/_sqlite3.pyd'), WindowsPath('DLLs/_ssl.pyd'), WindowsPath('DLLs/_testbuffer.pyd'), WindowsPath('DLLs/_testcapi.pyd'), WindowsPath('DLLs/_testimportmultiple.pyd'), WindowsPath('DLLs/_testmultiphase.pyd'), WindowsPath('DLLs/_tkinter.pyd')]
>>> [x for x in p.iterdir() if x.is_dir()==False]
[WindowsPath('DLLs/py.ico'), WindowsPath('DLLs/pyc.ico'), WindowsPath('DLLs/pyexpat.pyd'), WindowsPath('DLLs/select.pyd'), WindowsPath('DLLs/sqlite3.dll'), WindowsPath('DLLs/tcl86t.dll'), WindowsPath('DLLs/tk86t.dll'), WindowsPath('DLLs/U.txt'), WindowsPath('DLLs/unicodedata.pyd'), WindowsPath('DLLs/winsound.pyd'), WindowsPath('DLLs/_bz2.pyd'), WindowsPath('DLLs/_ctypes.pyd'), WindowsPath('DLLs/_ctypes_test.pyd'), WindowsPath('DLLs/_decimal.pyd'), WindowsPath('DLLs/_elementtree.pyd'), WindowsPath('DLLs/_hashlib.pyd'), WindowsPath('DLLs/_lzma.pyd'), WindowsPath('DLLs/_msi.pyd'), WindowsPath('DLLs/_multiprocessing.pyd'), WindowsPath('DLLs/_overlapped.pyd'), WindowsPath('DLLs/_socket.pyd'), WindowsPath('DLLs/_sqlite3.pyd'), WindowsPath('DLLs/_ssl.pyd'), WindowsPath('DLLs/_testbuffer.pyd'), WindowsPath('DLLs/_testcapi.pyd'), WindowsPath('DLLs/_testimportmultiple.pyd'), WindowsPath('DLLs/_testmultiphase.pyd'), WindowsPath('DLLs/_tkinter.pyd')]
>>> [x for x in p.iterdir() if x.is_dir()==False][0}
SyntaxError: invalid syntax
>>> [x for x in p.iterdir() if x.is_dir()==False][0]
WindowsPath('DLLs/py.ico')
>>> Path([x for x in p.iterdir() if x.is_dir()==False][0])
WindowsPath('DLLs/py.ico')
>>> [x for x in p.iterdir() if x.is_dir()==False][0].as_posix()
'DLLs/py.ico'
>>> 
====================== RESTART: C:/Python35/Project1.py ======================
>>> shutil.disk_usage(Path('C:\Riot Games'))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    shutil.disk_usage(Path('C:\Riot Games'))
  File "C:\Python35\lib\shutil.py", line 1002, in disk_usage
    total, free = nt._getdiskusage(path)
TypeError: _getdiskusage() argument 1 must be str, not WindowsPath
>>> shutil.disk_usage('C:\Riot Games')
usage(total=512002879488, used=364018561024, free=147984318464)
>>> shutil.disk_usage('C:\Riot Games').used/(1024**3)
339.0187644958496
>>> shutil.disk_usage('C:\Riot Games\League of Legends\lol.launcher').used/(1024**1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    shutil.disk_usage('C:\Riot Games\League of Legends\lol.launcher').used/(1024**1)
  File "C:\Python35\lib\shutil.py", line 1002, in disk_usage
    total, free = nt._getdiskusage(path)
FileNotFoundError: [WinError 3] The system cannot find the path specified
>>> 
>>> 
>>> os.path.getsize('C:\Riot Games')
0
>>> os.path.getsize('C:\Riot Games\League of Legends\lol.launcher')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    os.path.getsize('C:\Riot Games\League of Legends\lol.launcher')
  File "C:\Python35\lib\genericpath.py", line 50, in getsize
    return os.stat(filename).st_size
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Riot Games\\League of Legends\\lol.launcher'
>>> os.path.getsize('C:\Riot Games\League of Legends\Config\game')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    os.path.getsize('C:\Riot Games\League of Legends\Config\game')
  File "C:\Python35\lib\genericpath.py", line 50, in getsize
    return os.stat(filename).st_size
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Riot Games\\League of Legends\\Config\\game'
>>> os.path.getsize('C:\Riot Games\League of Legends\Config')
4096
>>> os.path.getsize('C:\Riot Games\League of Legends\Config')
4096
>>> os.stat('C:\Riot Games\League of Legends\Config').st_size
4096
>>> os.stat('C:\Riot Games').st_size
0
>>> 
