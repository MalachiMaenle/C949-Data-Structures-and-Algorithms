from chapter4.HashTable import HashTable


class ChainingHashTableItem:
    def __init__(self, item_key, item_value):
        self.key = item_key
        self.value = item_value
        self.next = None


class ChainingHashTable(HashTable):
    def __init__(self, initial_capacity=11):
        self.table = [None] * initial_capacity

    # Returns True if the specific key exists in the map, False otherwise.
    def contains(self, key):
        # Hash the key and compute the bucket index
        bucket_index = self.hash(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        while item != None:
            if key == item.key:
                return True
            item = item.next

        return False  # key not found

    # Searches for the item with the specified key. Returns the item's value if
    # found, None if not found.
    def get(self, key):
        # Hash the key and compute the bucket index
        bucket_index = self.hash(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        while item != None:
            if key == item.key:
                return item.value
            item = item.next

        return None  # key not found

    def get_length(self):
        length = 0
        # Loop through buckets
        for bucket in self.table:
            item = bucket
            # Loop through the bucket's linked list
            while item != None:
                # Increment the length
                length += 1

                # Advance to next item in the bucket's linked list
                item = item.next
        return length

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def insert(self, key, value):
        # Hash the key to get the bucket index
        bucket_index = self.hash(key) % len(self.table)

        # Traverse the linked list, searching for the key. If the key exists in
        # an item, the value is replaced. Otherwise a new item is appended.
        current_item = self.table[bucket_index]
        previous_item = None
        while current_item != None:
            if key == current_item.key:
                current_item.value = value
                return True
            previous_item = current_item
            current_item = current_item.next

        # Append to the linked list
        if self.table[bucket_index] == None:
            self.table[bucket_index] = ChainingHashTableItem(key, value)
        else:
            previous_item.next = ChainingHashTableItem(key, value)
        return True

    # Searches for the specified key. If found, the key/value pair is removed
    # from the hash table and True is returned. If not found, False is returned.
    def remove(self, key):
        # Hash the key and compute bucket index
        bucket_index = self.hash(key) % len(self.table)

        # Search the bucket's linked list for the key
        current_item = self.table[bucket_index]
        previous_item = None
        while current_item != None:
            if key == current_item.key:
                if previous_item == None:
                    # Remove linked list's first item
                    self.table[bucket_index] = current_item.next
                else:
                    previous_item.next = current_item.next
                return True
            previous_item = current_item
            current_item = current_item.next

        return False  # key not found

    # Prints all items in the table.
    def print(self, key_value_separator=": ", item_separator=", ",
              prefix="", suffix=""):
        # Print the prefix first
        print(prefix, end="")

        # First item print will be a special case
        printed_first_item = False

        # Loop through buckets
        for bucket in self.table:
            item = bucket

            # Loop through the bucket's linked list
            while item != None:
                if printed_first_item:
                    # All items but first are preceded by the separator
                    print(item_separator, end="")
                else:
                    printed_first_item = True

                # Print the item's key and value with the separator between
                print(f"{item.key}{key_value_separator}{item.value}", end="")

                # Advance to next item in the bucket's linked list
                item = item.next

        # Print the suffix last
        print(suffix, end="")

    # Prints the hash table's data, including empty buckets.
    def print_table(self):
        for i in range(len(self.table)):
            print(f"{i}: ", end="")

            if self.table[i] == None:
                print("(empty)")
            else:
                item = self.table[i]

                # Print first item and move to next
                print(f"{item.key}: {item.value}", end="")
                item = item.next

                # Print remaining items, each preceded by "-->"
                while item != None:
                    print(f" --> {item.key}: {item.value}", end="")
                    item = item.next
                print()