from utility import load_data
import package  # Make sure this is the correct name of the module where your Package class is defined.
import  pandas
from track import Track
from packages import Packages
# Call the load_data function to get the dataframes
distance_df, package_df = load_data()

packages = []   
for index, row in package_df.iterrows():
    # Create a Package object with the data from the row
    pkg = package.Package(
        id=row['ID'],
        address=row['Address'],
        city=row['City'],
        state=row['State'],
        zip=row['Zip'],
        deadline=row['Deadline'],
        weight=row['Weight KILO']
    )
    # Add the package object to the list
    packages.append(pkg)

packages[0].print_all()

packages_hash_table = Packages().hash_table
track1 = Track()
track2 = Track()
track3 = Track()

track1_package_ids = [1,2,7,13,14,15,16,19,20,21,27,29,30,34,40]
track2_package_ids = [3,6,18,25,26,28,31,32,36,37,38]
track3_package_ids = [4,5,8,9,10,11,12,17,22,23,24,33,35,39]
# print(f"num is  + {len(track1_package_ids)}")
# print(len(track1_package_ids) + len(track2_package_ids) + len(track3_package_ids))

track1.assign_package(track1_package_ids)
track1.packages.print()


