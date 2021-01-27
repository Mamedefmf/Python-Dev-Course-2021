# --- TEST PROGRAM - ERROR MANAGEMENT NOT IMPLEMENTED ---

# this function append a new pizza to the pizza_container
def append(collection):
    p = input("Insert the new pizza name: ")
    if p.lower() in collection:
        print("Error: Pizza already in the list")
    else:
        collection.append(p)


"""this function sort the names by number of characters
is just a test, not going to use it"""
def custom_sort(e):
    return len(e)


"""this function displays the items in pizza_container, it has
a optional parameter to limit what is printed.
"""
def display(collection, limit=None):
    # collection.sort(key=custom_sort)
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("ERROR: Pizza list is empty")
    else:
        print("---PIZZAS(" + str(nb_pizzas) + ")---")
        for i in collection[:limit:]:
            print(i)
        print()
        print(f"The first pizza in the list is: {collection[0]}")
        print(f"The last pizza is: {collection[-1]}")


# a list with pizza flavors
pizza_container = ["portuguesa", "paulista", "baiana", "frango e catupity", "atum"]

# this call the append function, to add a new pizza to the pizza_container
append(pizza_container)

# call the display function
display(pizza_container)
