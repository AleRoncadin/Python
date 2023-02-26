from pathlib import Path
import os

# cambiare directory
os.chdir(r'D:\Coding\Python\Automate_Boring_Stuff\9_FILES')
print(Path.cwd())

# home directory
print(Path.home())

# abosulte path: comincia con la root folder (C:\)
# relative path: si intende il percorso dalla cwd

# guardare immagine p.207 (ovvero p.249)
# .\spam.txt e spam.txt si riferiscono entrambi al file nella cwd
# ..\file.txt si riferisce al file presente nella directory prima


# METODO 1 (Path): creare nuove directory
newDir = Path('D:\\user_fronc\\Documents\\Prova')
print(newDir)
if not newDir.is_dir():
    os.makedirs(newDir)

# METODO 1 (os): creare nuove directory
newDir = Path(r'D:\\user_fronc\\Documents\\Prova1')
print(newDir)
if not newDir.is_dir():
    newDir.mkdir()

"""os.makedirs() crea più sottodirectory, mentre Path().mkdir() no"""

# ottenere l'absolute path dal relative path
absPath = Path.cwd() / Path('1_path.py')
print(absPath)

absPath = os.path.abspath('1_path.py')
print(absPath)

relPath = os.path.relpath('1_path.py')
print(relPath)

# utili
print(os.path.abspath('.'))
print(os.path.abspath('..'))