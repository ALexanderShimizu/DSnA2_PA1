class ChainingHashTable:
    def __init__(self, size):
        # Initialize the hash table with a specific size.
        self.size = size
        # Create a list of empty lists for each slot in the hash table.
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Hash function to determine the index for a given key.
        return hash(key) % self.size

    def insert(self, key, value):
        # Calculate the hash index for the given key.
        hash_index = self.hash_function(key)
        # Check if the key already exists in the hash table.
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                # If key exists, update the value.
                self.table[hash_index][i] = (key, value)
                return
        # If key does not exist, append the key-value pair to the hash table.
        self.table[hash_index].append((key, value))

    def remove(self, key):
        # Calculate the hash index for the given key.
        hash_index = self.hash_function(key)
        # Iterate through the list at the hash index to find the key.
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                # If key is found, delete the key-value pair.
                del self.table[hash_index][i]
                return True
        # Return False if key is not found.
        return False

    def search(self, key):
        # Calculate the hash index for the given key.
        hash_index = self.hash_function(key)
        # Iterate through the list at the hash index to find the key.
        for k, v in self.table[hash_index]:
            if key == k:
                # Return the value if key is found.
                return v
        # Return None if key is not found.
        return None

    def print(self):
        # Print the entire hash table.
        print(self.table)

    def get_key(self, value):
        # Iterate through the entire hash table to find a value.
        for index in range(self.size):
            for k, v in self.table[index]:
                if v == value:
                    # Return the key if value is found.
                    return k
        # Return None if value is not found.
        return None
