from hash_table import ChainingHashTable
from utility import load_data
from package import Package


class Packages:
    def __init__(self):
        self.hash_table = ChainingHashTable(40)
        self.init_packages_hash_table()

    def init_packages_hash_table(self):
        distance_df, package_df = load_data()
        data = (
            package_df.values.tolist()
        )  

        for i in data:
            print(i)
            address = " " + i[1]
            package = Package(address, i[2], i[3], i[4], i[5],i[6], i[7])
            self.hash_table.insert(int(i[0]), package)
            
            
# test = Packages()
# a =test.hash_table.search(1)
# print(a.print_all())


