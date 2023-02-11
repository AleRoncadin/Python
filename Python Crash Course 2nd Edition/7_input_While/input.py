name = input("""Hi, my name is Aleesandro.
What is your name? """)

print(f"Hello {name}")

# puoi anche scriverlo usando += per andare a capo
message = "My name is Pippy."
message += "\nWhat is your surname? "
surname = input(message)
print(f"Hello {surname}")

# numeri
age = int(input("How old are you? "))

if age < 18:
    print("You are a kid")
else:
    print("You are an adult")