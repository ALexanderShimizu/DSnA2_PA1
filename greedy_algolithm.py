from hash_table import ChainingHashTable
from utility import load_data


class GreedyAlgolithm:
    def __init__(self):
        self.distance_table = ChainingHashTable(40)
        self.address_index_table = ChainingHashTable(20)
        self.init_tables()
        self.distance_array = []

    def init_tables(self):
        distance_df, package_df = load_data()
        addresses = distance_df.iloc[:, 0].to_list()
        data = (
            distance_df.values.tolist()
        ) 
        for i in range(len(addresses)):
            self.distance_table.insert(addresses[i], data[i][1:])
            self.address_index_table.insert(addresses[i], i)

    def greedy_algolithm(self, current_location, packages_array):
        cureent_location_index = self.address_index_table.search(current_location)
        next_location = None
        next_location_distance = float("inf")
        for i in packages_array:
            if i == current_location and packages_array.count(i) == 1:
                continue  
            package_address_index = self.address_index_table.search(i)
            if cureent_location_index <= package_address_index:
                compared_distance = float(
                    self.distance_table.search(i)[cureent_location_index]
                )
                if compared_distance < next_location_distance:
                    next_location = i
                    next_location_distance = compared_distance

            elif cureent_location_index >= package_address_index:
                compared_distance = float(
                    self.distance_table.search(current_location)[package_address_index]
                )
                if compared_distance < next_location_distance:
                    next_location = i
                    next_location_distance = compared_distance

        return next_location, next_location_distance

