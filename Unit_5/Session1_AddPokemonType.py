'''
Problem 6: Add Pokemon Type
Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

It should add new_type to the Pokemon's list of types.

class Pokemon():
	...
	
	def add_type(self, new_type):
		pass
Example Usage:

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
Example Output:

{
    "name": "Jigglypuff",
    "types": ["Normal"]
    "is_caught": False
}

{
    "name": "Jigglypuff",
    "types": ["Normal", "Fairy"]
    "is_caught": False
}

'''

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if not self.is_caught:
            print(f"{self.name} is wild! Catch them if you can!")
        else:
            print(f"{self.name} I choose you!")

    def add_type(self, new_type):
        self.types.append(new_type)

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()