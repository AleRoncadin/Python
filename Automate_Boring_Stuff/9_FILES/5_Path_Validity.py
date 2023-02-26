import os
from pathlib import Path

# p.exists() --> True se il percorso esiste
# p.is_file() --> True se esiste e se è un file
# p.is_dir() --> True se esiste ed è una directory

# METODO 1 (Path): creare nuove directory (vedo prima se esiste)
newDir = Path('D:\\user_fronc\\Documents\\Prova')
if not newDir.is_dir():
    os.makedirs(newDir)

# METODO 1 (os): creare nuove directory (vedo prima se esiste)
newDir = Path(r'D:\\user_fronc\\Documents\\Prova1')
if not newDir.is_dir():
    newDir.mkdir()

# vedo se il file esiste
fileName = Path('1_path.py')
print(fileName.is_file())

# vedo se il percorso esiste
percorso = Path('E:\\Ciaooooooooo')
print(percorso.exists())