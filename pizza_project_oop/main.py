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
class CustomPizza(Pizza):
    BASE_PRICE = 20.0
    PRICE_PER_INGREDIENT = 3.2
    last_number = 0

    def __init__(self):
        CustomPizza.last_number += 1
        self.number = CustomPizza.last_number
        super().__init__("custom " + str(self.number), .0, [])
        self.ask_user_for_ingredients()
        self.compute_price()

    def ask_user_for_ingredients(self):
        print(f"\nIngredients for {self.number}")
        while True:
            ingredient = input("Add an Ingredient (or press ENTER to finish) ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"You have added {len(self.ingredients)} ingredient(s) : {', '.join(self.ingredients)}")

    def compute_price(self):
        self.price = float(len(self.ingredients)) * self.PRICE_PER_INGREDIENT + self.BASE_PRICE

#
pizzas = [
    Pizza("portuguesa", 29.99, ("muzzarela cheese", "ham", "egg", "onion", "tomato")),
    Pizza("paulista", 29.99, ("muzzarela cheese", "bacon", "tomato")),
    Pizza("baiana", 26.99, ("muzzarela cheese", "pepperoni sausage", "pepper sauce", "tomato")),
    Pizza("chicken & cheese", 24.99, ("chicken", "catupiry cheese")),
    Pizza("tuna", 24.99, ("muzzarela cheese", "tuna", "tomato")),
    Pizza("broccoli", 24.99, ("broccoli", "catupiry cheese", "tomato"), True),
    Pizza("special broccoli", 29.99, ("brocolli", "muzzarela cheese", "catupiry cheese", "tomato"), True),
    CustomPizza(),
    CustomPizza()
]

# Function to sort the pizza list by the number of ingredients
# def pizza_sort(e):
#    return len(e.ingredients)


# Call the pizza_sort function to organize the pizzas list
# pizzas.sort(key=pizza_sort)


for i in pizzas:
    i.display()
