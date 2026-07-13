def get_full_name(first_name, last_name):
	full_name = first_name.title() + " " + last_name.title()
	return full_name

print(get_full_name("fahad", "monshi"))

# Outputs:
"""
Fahad Monshi
"""


"""
It takes the first_name and last_name, converts the first letter of each one to upper case with title(). Concatenates them with a space in the middle.
"""


# Re-write with types
def get_full_name(first_name: str, last_name: str):
	full_name = first_name.title + " " + last_name.title()
	return full_name

print(get_full_name("fahad", "monshi"))

