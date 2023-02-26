from pathlib import Path
import os

print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))


myFiles = ['chiudi_porte.txt', 'bitcoin_darkweb.txt', 'psw_vm_server.txt']
for fileName in myFiles:
    print(Path(r'D:\user_fronc', fileName))

# METODO 1 (EFFICIENTE): unire più percorsi con /
percorso = Path('D:\\Coding\\Python') / Path('Automate_Boring_Stuff\\9_FILES')
print(percorso)

# METODO 2 (SCONSIGLIATO): usare + "\\" +          
pythonFolder = r'D:\Coding\Python'
filesFolder = r'Automate_Boring_Stuff\9_FILES'
percorso = pythonFolder + "\\" + filesFolder
print(percorso)

# METODO 3 (SCONSIGLIATO): usare .join()           
percorso = '\\'.join([pythonFolder, filesFolder])
print(percorso)


# sapere qual è la current working directory (cwd)
print(Path.cwd())