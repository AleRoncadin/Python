import random, sys
print("ROCK, PAPER, SCISSORS")

wins, losses, ties = 0, 0, 0

# rock = 0
# paper = 1
# scissors = 2


while True:
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ")
    enemy = random.randint(0, 2)

    if move == 'q':
        print("Bye!")
        break

    elif move == 'r':
        print('ROCK VERSUS ...')
        if enemy == 0:
            print('ROCK')
            print('It is a tie!')
            ties += 1
        elif enemy == 1:
            print('PAPER')
            print('You lose!')
            losses += 1
        else:
            print('SCISSOR')
            print('You win!')
            wins += 1

    elif move == 'p':
        print('PAPER VERSUS ...')
        if enemy == 0:
            print('ROCK')
            print('You win!')
            wins += 1
        elif enemy == 1:
            print('PAPER')
            print('It is a tie!')
            ties += 1
        else:
            print('SCISSOR')
            print('You lose!')
            losses += 1   

    elif move == 's':
        print('SCISSORS VERSUS ...')
        if enemy == 0:
            print('ROCK')
            print('You lose!')
            losses += 1
        elif enemy == 1:
            print('PAPER')
            print('You win!')
            wins += 1
        else:
            print('SCISSOR')
            print('It is a tie!')
            ties += 1  
    
    else:
        print("Wrong command!")
