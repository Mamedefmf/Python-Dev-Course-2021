# Creates the pizza class with the following parameters: name, price, ingredients, vegetarian(t or f)

class Pizza:
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian

    def display(self):
        if self.vegetarian == True:
            print(f"{self.name} : R${self.price} - VEGETARIAN")
            print(", ".join(self.ingredients) + "\n")
        else:
            print(f"{self.name} : R${self.price}")
            print(", ".join(self.ingredients) + "\n")


# Creates a child class for a custom pizza, where the user can choose the ingredients and the price will be attached
# class CustomPizza(Pizza):

#
pizzas = [
    Pizza("portuguesa", 8.99, ("muzzarela cheese", "ham", "egg", "onion", "tomato")),
    Pizza("paulista", 10.99, ("muzzarela cheese", "bacon", "tomato")),
    Pizza("baiana", 11, ("muzzarela cheese", "pepperoni sausage", "pepper sauce", "tomato")),
    Pizza("chicken & cheese", 10, ("chicken", "catupiry cheese")),
    Pizza("tuna", 12.99, ("muzzarela cheese", "tuna", "tomato")),
    Pizza("broccoli", 10, ("broccoli", "catupiry cheese", "tomato"), True),
    Pizza("special broccoli", 16.99, ("brocolli", "muzzarela cheese", "catupiry cheese", "tomato"), True)
]


# Function to sort the pizza list by the number of ingredients
def pizza_sort(e):
    return len(e.ingredients)


# Call the pizza_sort function to organize the pizzas list
pizzas.sort(key=pizza_sort)


for i in pizzas:
    i.display()
