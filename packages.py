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

    def print_status_all(self):
        # Method to print the status of all packages.
        for i in range(1, 41):
            # Iterate through package IDs.
            package = self.search(str(i))  # Search for the package by its ID.
            # Check and print the delivery status of the package.
            if package.delivery_status == "Delivered":
                if package.note != "":
                    # Print details including special note if it exists.
                    print(
                        f"Package {i} delivered by {package.track} to {package.address} at {package.delivered_time} | Special Note: {package.note}"
                    )
                else:
                    # Print details without special note.
                    print(
                        f"Package {i} delivered by {package.track} to {package.address} at {package.delivered_time}"
                    )
            elif package.delivery_status == "en route":
                # Print details for packages that are en route.
                print(
                    f"Package {i} {package.delivery_status} to {package.address} by {package.track}"
                )
            elif package.delivery_status == "at HUB":
                # Print details for packages that are still at the HUB.
                print(f"Package {i} is at {package.delivery_status}")
