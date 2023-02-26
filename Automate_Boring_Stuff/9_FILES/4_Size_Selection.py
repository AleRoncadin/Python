from pathlib import Path
import os

# file size
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
calcSize = os.path.getsize(calcFilePath)
print(str(calcSize) + " B")

# vedere i file nella directory e la loro dimensione
documentsPath = Path('D:\\user_fronc\\Documents')
files = os.listdir(documentsPath)
totalSize = 0

print(f"File in Documents directory are: ")
for file in files:
    size = os.path.getsize(documentsPath / file)
    totalSize = totalSize + size
    print(f"- {file}: {size} B")

print(f"Size of Documents is: {totalSize} B")


# usare glob() per selezionare alcuni file:
#   con glob('*') seleziono tutti, è come os.listdir(path)
#   con glob('*.txt') seleziono solo i .txt
#   con glob('progetto?.txt') mostra tutti i file che hanno un carattere 
#       dopo progetto e prima di .txt. Va bene progetto1.txt, ma non progetto10.txt

txtDocuments = documentsPath.glob('*.txt')
for txtDocument in list(txtDocuments):          # bisogna metterlo come lista
    print(txtDocument.name)                     # con .name tolgo il percorso

randomDocuments = documentsPath.glob('*.???')
for randomDocument in list(randomDocuments):
    print(randomDocument.name)
