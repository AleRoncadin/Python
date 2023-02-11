# 7.5
while True:
    age = input("\nEnter your age (or 'quit'): ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Ticket is free")
    elif age <= 12:
        print("Ticket is $10")
    else:
        print("Ticket is $15")