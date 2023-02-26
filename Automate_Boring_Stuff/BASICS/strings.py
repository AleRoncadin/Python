message = 'Say Hi to Bob\' mum.'

# \'
# \"
# \t
# \n
# \\

# stampare i backslash: usare r nel print
print(r"This is Carol\'s cat")

# stringhe multilinea: usare ''' ''' oppure """ """
print("""Ciao Marco,
Ti volevo fare gli auguri!

Saluti,
Alessandro""")


# fare commenti multilinea: usare """"""
"""Questo programma spiega le stringhe
Ma non gli interi"""


hello = "Hello, world!"
print(hello[0])             # H
print(hello[-1])            # !
print(hello[0:5])           # Hello
print(hello[:5])            # Hello
print(hello[7:])            # world!

# vedere se una sottostringa o carattere è nella stringa
print('Hello' in 'Hello, world!')
print('HELLO' in 'Hello, world!')
print('mondo' not in 'Hello, world!')

# controlli della stringa
print(hello.islower())
print(hello.isupper())
print(hello.istitle())
print(hello.isalpha())          # True if is only letters, no spaces
print(hello.isalnum())          # True if is only letters and numbers, no spaces
print(hello.isdecimal())        # True if is only numbers, no spaces
print(hello.isspace())          # True if is only spaces

print(hello.startswith('hello'))    # falso perché inizia con Hello
print(hello.endswith('world!'))


# trasformare stringa in lista
lista = 'My name is Simon'.split(' ')
print(lista)

# trasformare lista in stringa
stringa = ' '.join(['My', 'name', 'is', 'Simon'])
print(stringa)

# riempire il testo rjust(), ljust(), and center() Methods
print('Hello'.rjust(20))        # stampa Hello con degli spazi prima
print('Hello'.ljust(10))        # stampa Hello con degli spazi dopo
print('Hello'.center(10))       # stampa Hello in mezzo a degli spazi
print('Hello'.rjust(10, '*'))   # stampa Hello con degli * prima
print('Hello'.rjust(20, '-'))   # stampa Hello con degi - dopo
print('Hello'.center(10, '*'))  # stampa Hello in mezzo a degli *

# ord e char
# per capire il valore numerico Unicode dei caratteri
print(ord('A'))
print(chr(98))
print(chr(ord('A') + 1))