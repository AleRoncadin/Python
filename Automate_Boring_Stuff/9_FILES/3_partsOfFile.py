from pathlib import Path
import os

p = Path('C:/Users/fronc/file.txt')
print(p.anchor)                                 # C:\
print(p.parent)                                 # C:\Users\fronc
print(p.name)                                   # file.txt
print(p.stem)                                   # file
print(p.suffix)                                 # .txt
print(p.drive)                                  # C:

# parents[] è diverso dal metodo parent:

cwd = Path.cwd()                   # D:\Coding\Python\Automate_Boring_Stuff\9_FILES
p0 = Path.cwd().parents[0]         # D:\Coding\Python\Automate_Boring_Stuff           
p1 = Path.cwd().parents[1]         # D:\Coding\Python
p2 = Path.cwd().parents[2]         # D:\Coding 
p3 = Path.cwd().parents[3]         # D:\

print(cwd)
print(p0)
print(p1)
print(p2)
print(p3)


# si può fare anche con os.path
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
basename = os.path.basename(calcFilePath)           # calc.exe
dirname = os.path.dirname(calcFilePath)             # C:\Windows\System32

# oppure con split
basename, dirname = os.path.split(calcFilePath)
print(f"Basename: {basename} \t\t Dirname: {dirname}")

print(calcFilePath.split(os.sep))