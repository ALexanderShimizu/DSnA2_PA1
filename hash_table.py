class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                self.table[hash_index][i] = (key, value)
                return
        self.table[hash_index].append((key, value))

    def remove(self, key):
        hash_index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                del self.table[hash_index][i]
                return True
        return False

    def search(self, key):
        hash_index = self.hash_function(key)
        for k, v in self.table[hash_index]:
            if key == k:
                return v
        return None
      
    def print(self):
      print(self.table)


# Example usage:
ht = ChainingHashTable(10)  # Create a hash table with 10 slots
ht.insert("key1", "value1")
ht.insert("key2", "value2")
ht.insert("key1", "value3")  # This will update the value for "key1"
ht.print()
print(ht.search("key1"))  # Output: value3
print(ht.search("key2"))  # Output: value2
print(ht.search("key3"))  # Output: None

ht.remove("key1")
print(ht.search("key1"))  # Output: None
