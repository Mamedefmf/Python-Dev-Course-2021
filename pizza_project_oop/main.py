# Creates the pizza class with the following parameters: name, price, ingredients, vegetarian(t or f)

class Pizza:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def display(self):
        print(f"{self.name} : R${self.price}")
        print(", ".join(self.ingredients))


# Creates object: pizza1
pizza1 = Pizza("portuguesa", 24.99, ("muzzarela cheese", "ham", "egg", "onion", "tomato"))
pizza1.display()

# a list with pizza flavors from the last project
# pizza_container = ["portuguesa", "paulista", "baiana", "frango e catupity", "atum"]
