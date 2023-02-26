import sys, random, time

print(23 / 7)       # divisione float
print(23 // 7)      # divisione intera

# replicare le stringhe
print('Alice' * 6)      # stampa Alice 6 volte  -->  AliceAliceAlice...

# end keyword in print() function
print("Hello", end='')
print(" World")             # stampa Hello World nella stessa linea

print("Top", end='G ')
print("is me")

count = 0

while count <= 5:
    print(random.randint(0, 3))
    count += 1
    time.sleep(0.1)

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    else:
        break

