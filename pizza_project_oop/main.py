# Creates the pizza class with the following parameters: name, price, ingredients, vegetarian(t or f)

class Pizza:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def display(self):
        print(f"{self.name} : R${self.price}")
        print(", ".join(self.ingredients))


# Objective: 1.create a pizzas tuple 2.create the pizzas from the pizza_container 3.display all pizzas

# Creates objects: pizza1,pizza2,3....
pizza1 = Pizza("portuguesa", 24.99, ("muzzarela cheese", "ham", "egg", "onion", "tomato"))
pizza2 = Pizza("paulista", 34.99, ("muzzarela cheese", "bacon", "tomato"))
pizza3 = Pizza("baiana", 26.99, ("muzzarela cheese", "pepperoni sausage", "pepper sauce", "tomato"))
pizza4 = Pizza("chicken & cheese", 24.99, ("chicken", "catupiry cheese"))
pizza5 = Pizza("tuna", 24.99, ("muzzarela cheese", "tuna", "tomato"))

pizzas = (pizza1, pizza2, pizza3, pizza4, pizza5)

for i in pizzas:
    print("")
    i.display()
