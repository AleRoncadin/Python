from pathlib import Path

p = Path('spam.txt')
if not p.is_file:
    p.write_text('Ciao, mondo!')
    txt = p.read_text()
    print(txt)

# open function accepts only Path() elements
spamFile = open(Path.cwd() / 'spam.txt', 'r')       # read mode è di default
spamContent = spamFile.read()
spamContentList = spamFile.readlines()              # fa una lista delle righe
print(spamContent)


# write mode cancella tutto
spamFile = open(Path.cwd() / 'spam.txt', 'w')
spamFile.write('Buongiorno a te')
spamFile.close()

# append mode scrive alla fine
spamFile = open(Path.cwd() / 'spam.txt', 'a')
spamFile.write('\nCiao')
spamFile.close()

spamFile = open(Path.cwd() / 'spam.txt', 'r')
spamFile.read()
spamFile.close()