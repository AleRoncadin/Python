#flessibilità apostrofi per le stringhe
print('I told my friend, "Python is my favorite language!"')
print("The language 'Python' is named after Monty Python, not the snake.")
print("One of Python's strengths is its diverse and supportive community.")

first_name = "ada"
last_name = "grotti"

#f-strings
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello world, I'm {full_name.title()}")

#tab
print("\tTab space")

#remove extra whitespace on right and left of the strings:
#   rstrip() for right side
#   lstrip() for left side
#   strip() for both sides
favorite_language = '   python   '
print(favorite_language)
print(favorite_language.strip())

famous_person = "Albert Einstein"
quote = '"A person who never made a mistake never tried anything new."'
message = f"{famous_person} once said, {quote}"
print(message)