from chapter4.MapADT import MapADT


# Abstract class for map ADT implementation that uses a hash table.
class HashTable(MapADT):
    # Returns a non-negative hash code for the specified key.
    def hash(self, key):
        return abs(hash(key))

    # Prints the hash table's data, including empty buckets.
    def print_table(self):
        pass