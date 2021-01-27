def display(collection):
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("ERROR: Pizza list is empty")
        return

    print("---PIZZAS(" + str(nb_pizzas) + ")---")
    for i in collection:
        print(i)
    print()
    print(f"The first pizza in the list is: {collection[0]}")
    print(f"The last pizza is: {collection[-1]}")


pizzas = ("Portuguesa", "Paulista", "Baiana", "Frango e Catupity", "Atum")
empty = ()

display()
