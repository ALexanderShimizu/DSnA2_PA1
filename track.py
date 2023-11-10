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
        
    def update_time(self, hours, minutes):
        self.time = time(hours, minutes)

    def calculate_time(self, average_speed):
        hours_spent = self.miles / average_speed
        self.time_spent = timedelta(hours=hours_spent)

    def get_time(self):
        return self.time + self.time_spent
    
    # def add_package(self, package):
    #     self.add_package.append(package)

    def assign_package(self, package_ids):
        packages_hash_table = Packages().hash_table
        for i in package_ids:
            address = packages_hash_table.search(i)
            self.packages_id_hash_table.insert(address, i)
            self.packages_array.append(address)
            
    def deliver(self):
        greedy_algolithm = GreedyAlgolithm
        while self.packages_array:
            next_address , miles = greedy_algolithm.greedy_algolithm(self.current_address, self.packages_array)
            self.count_miles(miles)
            if self.current_address != " HUB":
                self.packages_array.remove(self.current_address)
            self.current_address = next_address
            
        
        
