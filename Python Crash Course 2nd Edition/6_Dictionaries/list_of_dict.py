alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] # abbiamo creato 3 alieni

# ne vogliamo creare 30:

aliens = [] # inizializzo una lista vuota

for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    aliens.append(new_alien)

for alien in aliens[:5]:        # stampa i primi 5 alieni
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

# cambiamo le caratteristiche degli alieni:
for alien in aliens[:3]:                    # cambia i primi 3
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

for alien in aliens[:8]:                    # cambia i primi 8
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15