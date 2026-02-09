from chapter4.ChainingHashTable import ChainingHashTable

print('\n\033[1;32m' + '-----Chapter 4-----' + '\033[0m')

# region MapADT notes
# associates keys with values
# each key in a map is distinct
# if the key does not exist, it creates a new key-value pair
# if the key exists, it updates the value of the key
# get returns the value of the given key
# insert, remove, get, contains, get_length
# endregion

print('\n\033[31m' + 'Hash Table: ' + '\033[0m')
# region Hash Table test

keys = [
    "LAX", "IAH", "IAD", "ORD", "SFO",
    "DAL", "NRT", "JFK", "YVR", "LHR"
]
values = [
    "Los Angeles", "Houston", "Washington", "Chicago", "San Francisco",
    "Dallas", "Tokyo", "New York", "Vancouver", "London"
]

# Create a ChainingHashTable and add all items
chaining = ChainingHashTable()
for i in range(len(keys)):
    chaining.insert(keys[i], values[i])

# Print the table's items
print("Items: ")
chaining.print(": ", "\n", "", "\n")

# Print the table's buckets
print("\nBuckets:")
chaining.print_table()

# Remove some items
print()
keys_to_remove = [ "LAX", "ORD" ]
for key_to_remove in keys_to_remove:
    print(f"Removing \"{key_to_remove}\"")
    chaining.remove(key_to_remove)

# Print again
print("\nBuckets after removals:")
chaining.print_table()
# endregion
# region Hash Table notes
# all keys are integers in the range [0,9] and uses a map ADT
# noninteger key types are not supported
# an array large enough to support all possible integers cannot be allocated
# hash table - data structure that stores unordered items by mapping each item to a location in an array
# bucket - a hash table array element
# hash map - implementation of a map ADT using a hash table
# insert, get, and remove each have a key parameter. The key is converted into a bucket index with the following logic:
# hash_code = Call hash code function for key
# bucket_index = hash_code % array_allocation_size
# endregion