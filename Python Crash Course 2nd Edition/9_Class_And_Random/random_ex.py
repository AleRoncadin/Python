from random import randint, choice

print(randint(1, 6))        # stampa un numero tra 1 e 6

# choice() ritorna un elemento casuale da una lista o tupla
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up.title())

# ES. 9.13
class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        rand = randint(1, self.sides)
        print(rand)

count = 0

die = Die(20)
while count <= 10:
    die.roll_die()
    count +=1


# ES. 9.14 E 9.15 MODIFICATI A MIO PIACIMENTO (PIù COMPLESSI)

lista = ['1', '2', '3', '9', '0', '19', '78', '48', '34', '50', 'A', 'O', 'I', 'R', 'E']

def lotteria(lista): 
    """
    Genera un ticket random di lunghezza 4 formato da numeri e/o lettere 
    separate da un '-'
    """
    
    count = 0
    ticket = ""
    while count <= 3:
        if count == 3:           
            str = choice(lista)
        else:
            str = choice(lista) + "-"

        ticket += str
        count += 1

    return ticket
    
ticket = lotteria(lista)
print(f"Il ticket corretto è: {ticket}")

my_ticket = "1-A-R-19"

while True:
    ticket = lotteria(lista)
    if my_ticket == ticket:
        print(f"Ticket corretto!!!   -->   {my_ticket} = {ticket}")
        break
    else:
        print(f"Ticket non corretto, il ticket è: {ticket}")