from hash_table import ChainingHashTable
from utility import load_data


class Packages:
    def __init__(self):
        self.hash_table = ChainingHashTable(40)
        self.init_packages_hash_table()

    def init_packages_hash_table(self):
        distance_df, package_df = load_data()
        data = (
            package_df.values.tolist()
        )  # This converts the DataFrame rows to a list of lists

        for i in data:
            address = " " + i[1]
            self.hash_table.insert(i[0], address)
            
            
      

