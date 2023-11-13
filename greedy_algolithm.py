from hash_table import ChainingHashTable
from utility import load_data


class GreedyAlgorithm:
    def __init__(self):
        # Constructor for the GreedyAlgorithm class.
        # Initializes two hash tables: one for distances and one for address indices.
        self.distance_table = ChainingHashTable(40)  # Hash table for distances.
        self.address_index_table = ChainingHashTable(
            20
        )  # Hash table for address indices.
        self.init_tables()  # Initialize the tables with data.
        self.distance_array = []  # Array to store distances.

    def init_tables(self):
        # Method to initialize the distance and address index tables.
        distance_df, package_df = load_data()  # Load distance and package data.
        addresses = []
        for i in distance_df:
            # Extract addresses from the distance data.
            addresses.append(i[0])
        data = distance_df  # Assign distance data to 'data' variable.

        for i in range(len(addresses)):
            # Iterate through each address.
            # Insert distance data and address index into respective hash tables.
            self.distance_table.insert(addresses[i], data[i][1:])
            self.address_index_table.insert(addresses[i], i)

    def greedy_algorithm(self, current_location, packages_array):
        # Method implementing the greedy algorithm to find the next location.
        current_location_index = self.address_index_table.search(current_location)
        next_location = None
        next_location_distance = float("inf")

        for i in packages_array:
            # Iterate through each package in the array.
            if i == current_location and packages_array.count(i) == 1:
                # Skip if the package's location is the same as the current location.
                continue
            package_address_index = self.address_index_table.search(i)
            # Calculate the distance to the package's location.
            if current_location_index <= package_address_index:
                compared_distance = float(
                    self.distance_table.search(i)[current_location_index]
                )
            else:
                compared_distance = float(
                    self.distance_table.search(current_location)[package_address_index]
                )
            # Update the next location if a shorter distance is found.
            if compared_distance < next_location_distance:
                next_location = i
                next_location_distance = compared_distance

        return next_location, next_location_distance
