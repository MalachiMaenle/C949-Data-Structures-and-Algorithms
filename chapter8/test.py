from chapter8.Set import Set

print('\033[1;32m' + '-----Chapter 8-----' + '\033[0m')

print('\033[31m' + 'Set: ' + '\033[0m')
# region Set test
def show_set(set1, set_name):
    print(set_name + ": ", end="")
    for element in set1:
        print(element, end=" ")
    print("")

def even_predicate(element):
    return (element % 2) == 0

def over50_predicate(element):
    return element > 50

def map_times_10(element):
    return element * 10

def map_mod_10(element):
    return element % 10

setA = Set()
setA.add(95)
setA.add(64)
setA.add(19)
setA.add(67)
setA.add(-24)
setA.add(90)
setB = Set()
setB.add(67)
setB.add(90)
setB.add(67)
setB.add(42)
setB.add(-84)

# Display the 2 sets
show_set(setA, "Set A")
show_set(setB, "Set B")

# Perform union, intersection, and difference of 2 sets
show_set(setA.union(setB), "A union B")
show_set(setA.intersection(setB), "A intersect B")
show_set(setA.difference(setB), "A - B")
show_set(setB.difference(setA), "B - A")

# Perform various filter operations
show_set(setA.filter(even_predicate), "Set A filtered for evens")
show_set(setB.filter(even_predicate), "Set B filtered for evens")
show_set(setA.filter(over50_predicate), "Set A filtered for elements > 50")
show_set(setB.filter(over50_predicate), "Set B filtered for elements > 50")

# Perform various map operations
show_set(setA.map(map_times_10), "Set A mapped * 10")
show_set(setB.map(map_times_10), "Set B mapped * 10")
show_set(setA.map(map_mod_10), "Set A mapped % 10")
show_set(setB.map(map_mod_10), "Set B mapped % 10")
# endregion
# region Set notes
# set - ADT representing a collection of distinct elements
# add - adds an element to the set if not exists already
# remove - removes an item from the set if exists
# length - number of elements in the set
# two sets containing the same elements are "equal"
# subset - at least all items in the subset are in the set
# {19, 22, 26} is a subset of {26, 42, 59, 19, 57, 22}
# union - combines two sets
# intersection - only the elements shared between sets are returned
# difference - only the unique elements are returned from given set
# filter - produces a subset containing elements of a certain condition
# map - makes a new set using a function of an old set
# endregion

print('\033[31m' + 'Python Default set(): ' + '\033[0m')
# region set() test
items_to_add = {"Bread", "Butter", "Jam", "Milk", "Cereal"}

grocery_items = set()
for item in items_to_add:
    grocery_items.add(item)
    print(f"Added \"{item}\"")
print(f"Set with {len(grocery_items)} items: {grocery_items}")

item_name = "Butter"

print(f"Set contains \"{item_name}\"? ", end="")
if item_name in grocery_items:
    print(f"Yes\nNow removing \"{item_name}\"")
    grocery_items.remove(item_name)
else:
    print("No")

print(f"Set with {len(grocery_items)} items: {grocery_items}")
# endregion