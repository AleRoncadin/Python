from functions import build_person
from functions import greet_users as gu
import exercises_8 as ex
from functions import *     # importa tutte le funzioni

#person = build_person('jimi', 'hendrix', age=27)
#print(person)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

ex.make_shirt('xl', 'ciao')

# per non eseguire tutto il codice dal modulo importato inserire questo codice
# nel modulo:

# def main():
    # dentro il main inserisci tutte le chiamate e le istanze delle classi

# chiami il main:
# if __name__ == "__main__":
#   main() 