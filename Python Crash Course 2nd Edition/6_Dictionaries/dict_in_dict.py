users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location'].title()

    print(f"- Name: {full_name}")
    print(f"- Location: {location}")