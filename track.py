from datetime import time, timedelta, datetime
from hash_table import ChainingHashTable
from packages import Packages
from greedy_algolithm import GreedyAlgolithm


class Track:
    def __init__(self):
        # This contains (Adress, ID)
        self.packages_id_hash_table = ChainingHashTable(16)
        self.packages_array = []
        self.miles = 0
        self.time = time(0, 0)
        self.time_spent = timedelta()
        self.current_address = " HUB"

    def count_miles(self, miles):
        self.miles += miles
    
    def set_time(self, h, m):
        self.time =time(h,m)    
    
    def update_time(self, hours, minutes):
        self.time = time(hours, minutes)

    def calculate_time(self, miles):
        hours_spent = miles / 16

        additional_time = timedelta(hours=hours_spent)
        self.time_spent += additional_time  # Add to the existing time

    def get_time(self):
        placeholder_date = datetime(2000, 1, 1)
        current_datetime = datetime.combine(placeholder_date, self.time)
        new_datetime = current_datetime + self.time_spent
        # Return the time part
        return new_datetime.time()

    # def add_package(self, package):
    #     self.add_package.append(package)

    def assign_package(self, package_ids):
        packages_hash_table = Packages().hash_table
        for i in package_ids:
            address = packages_hash_table.search(i)
            self.packages_id_hash_table.insert(address, i)
            self.packages_array.append(address)
        print(self.packages_array)

    def deliver(self):
        greedy_algolithm_instance = GreedyAlgolithm()
        while self.packages_array:
            next_address, miles = greedy_algolithm_instance.greedy_algolithm(
                current_location=self.current_address,
                packages_array=self.packages_array,
            )
            if next_address is None:
                break
            self.count_miles(miles)
            self.calculate_time(miles)
            print(f"Dropped of at {next_address}: Time {self.get_time()}")
            print(f"Traveled {miles} miles")
            if self.current_address != " HUB":
                self.packages_array.remove(self.current_address)
            self.current_address = next_address

        print(f"Traveled {self.miles} miles \n")

    def back_to_hub(self):
        greedy_algolithm_instance = GreedyAlgolithm()
        hub, miles = greedy_algolithm_instance.greedy_algolithm(
            self.current_address, [" HUB"]
        )
        self.count_miles(miles)
        print(f"Back to Hub: Traveled {miles}miles")
