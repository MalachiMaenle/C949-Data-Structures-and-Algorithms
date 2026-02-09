class MapADT:
    # Returns True if the specific key exists in the map, False otherwise.
    def contains(self, key):
        pass

    # Searches for the item with the specified key. Returns the item's value if
    # found, None if not found.
    def get(self, key):
        pass

    # Returns the number of items in the map.
    def get_length(self):
        pass

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def insert(self, key, value):
        pass

    # Prints all items in the map.
    def print(self, key_value_separator=":", item_separator=", ",
              prefix="", suffix=""):
        pass

    # Searches for the specified key. If found, the key/value pair is removed
    # from the map and True is returned. If not found, False is returned.
    def remove(self, key):
        pass