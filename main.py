from utility import load_data
import package  # Make sure this is the correct name of the module where your Package class is defined.
import pandas
from track import Track
from packages import Packages
from greedy_algolithm import GreedyAlgolithm

# Call the load_data function to get the dataframes
distance_df, package_df = load_data()

packages = []
for index, row in package_df.iterrows():
    # Create a Package object with the data from the row
    pkg = package.Package(
        id=row["ID"],
        address=row["Address"],
        city=row["City"],
        state=row["State"],
        zip=row["Zip"],
        deadline=row["Deadline"],
        weight=row["Weight KILO"],
    )
    # Add the package object to the list
    packages.append(pkg)

packages[0].print_all()

packages_hash_table = Packages().hash_table
track1 = Track()
track2 = Track()
track3 = Track()

track1_package_ids = [1, 4, 7, 13, 14, 15, 16,  20, 21,  29, 30,  34, 37, 39, 40]
track2_package_ids = [3, 5, 6, 18, 25, 26, 31, 32, 36, 38]
track3_package_ids = [ 2,8, 9, 10, 11, 12, 17, 19, 22, 23, 24, 27, 28, 33, 35]  
# print(f"num is  + {len(track1_package_ids)}")
# print(len(track1_package_ids) + len(track2_package_ids) + len(track3_package_ids))

track1.assign_package(track1_package_ids)
track2.assign_package(track2_package_ids)
track3.assign_package(track3_package_ids)

track1.set_time(8,0)
track1.deliver()
track1.back_to_hub()
track2.set_time(9,5)
track2.deliver()

# track2.deliver()
track3.set_time(10,20)
track3.deliver()

print(track1.miles + track2.miles + track3.miles)