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

"""
Now code editor knows the types and i can suggest related methods and also provides error checks.
"""



# For some additional use cases, you might need to import some things from the standard library typing module, for example when you want to declare that something has "any type", you can use Any from typing:
from typing import Any

def some_function(data: Any):
	print(data)



# Generic types
"""
Some types can take "type parameters" in square brackets, to define their internal types, for example a "list of strings" would be declared list[str].

These types that can take type parameters are called Generic types or Generics.

You can use the same builtin types as generics (with square brackets and types inside):

- list
- tuple
- set
- dict
"""
def process_items(items: list[str]):
	for item in items:
		print(item)
"""
That means: "the variable items is a list, and each of the items in this list is a str".
By doing that, your editor can provide support even while processing items from the list
"""
