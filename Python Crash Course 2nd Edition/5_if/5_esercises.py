# 5.3 - 5.4 - 5.5
alien_color = 'yellow'

if alien_color.lower() == 'green':
    print("You earned 5 points")
elif alien_color.lower() == 'yellow':
    print("You earned 10 points")
else:
    print("You earned 15 points")

# 5.6
age = 24

if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder")

# 5.10
current_users = ['alfa', 'Beta', 'DOOM', 'xi', 'Sigma']
current_users_lower = ['alfa', 'beta', 'doom', 'xi', 'sigma']
new_users = ['orso', 'BETA', 'doom', 'fi', 'sigma']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username {new_user} has already been used, you have to enter another username!")
    else:
        print(f"The username {new_user} is available")

# 5.11
ordinal_numbers = list(range(1,10))

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print("1st")
    elif ordinal_number == 2:
        print("2nd")
    elif ordinal_number == 3:
        print("3rd")
    else:
        print(f"{ordinal_number}th")
    
