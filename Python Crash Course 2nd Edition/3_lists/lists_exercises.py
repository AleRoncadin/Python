# 3.4
people = ['Alberto', 'Daniele', 'Francesco']
print(f"Hei {people[0]}, you're invited to dinner")
print(f"Hei {people[1]}, you're invited to dinner")
print(f"Hei {people[2]}, you're invited to dinner")

# 3.5
print("------------------------------------------------------")
print(f"{people[1]} can't make the dinner")

people[1] = 'Roberto'
print(f"Hei {people[0]}, you're invited to dinner")
print(f"Hei {people[1]}, you're invited to dinner")
print(f"Hei {people[2]}, you're invited to dinner")

# 3.6
print("------------------------------------------------------")
people.insert(0, 'Marco')
people.insert(2, 'Stefano')
people.append('Matteo')

print(f"Hei {people[0]}, you're invited to dinner")
print(f"Hei {people[1]}, you're invited to dinner")
print(f"Hei {people[2]}, you're invited to dinner")
print(f"Hei {people[3]}, you're invited to dinner")
print(f"Hei {people[4]}, you're invited to dinner")
print(f"Hei {people[5]}, you're invited to dinner")

# 3.7
print("------------------------------------------------------")
popped_person = people.pop()
print(f"Sorry {popped_person} but I can't invite you to dinner")
popped_person = people.pop()
print(f"Sorry {popped_person} but I can't invite you to dinner")
popped_person = people.pop()
print(f"Sorry {popped_person} but I can't invite you to dinner")
popped_person = people.pop()
print(f"Sorry {popped_person} but I can't invite you to dinner")
print(f"Hei {people[0]}, {people[1]}, you're still invited")
del people[0]
del people[0]
print(f"Empty list: {people}")