from hash_table import ChainingHashTable
from utility import load_data
from package import Package


class Packages:
    def __init__(self):
        # Constructor for the Packages class. Initializes a hash table for storing packages.
        self.hash_table = ChainingHashTable(40)  # Hash table with 40 slots.
        self.init_packages_hash_table()  # Initialize the hash table with package data.

    def init_packages_hash_table(self):
        # Method to initialize the hash table with package data.
        distance_df, package_df = load_data()  # Load package data.
        data = package_df  # Assign package data to 'data' variable.

        for i in data:
            # Iterate through each package in the data.
            address = " " + i[1]  # Prepend a space to the address for formatting.
            # Create a Package object with the package details.
            package = Package(address, i[2], i[3], i[4], i[5], i[6], i[7])
            # Insert the package into the hash table with its ID as the key.
            self.hash_table.insert(str(i[0]), package)

    def search(self, key):
        # Method to search for a package in the hash table using its key.
        return self.hash_table.search(key)

    def print_header(self):
        # Print Header
        header = (
            "PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, Special Notes, "
            "Status, Delivered Time, Distance from Last Location, Name of the Track"
        )
        print(header)

    def print_status_all(self):
        # Method to print the status of all packages.
        self.print_header()
        for i in range(1, 41):
            # Iterate through package IDs.
            package = self.search(str(i))  # Search for the package by its ID.
            print(f"ID: {i},", end="") # Print package info
            package.print_all()

    def print_a_package(self, id):
        self.print_header
        print(f"ID: {id},", end="")
        self.search(id).print_all()
