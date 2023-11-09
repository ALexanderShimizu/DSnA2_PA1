from datetime import time, timedelta, datetime
from hash_table import ChainingHashTable
from packages import Packages

class Track:
    def __init__(self):
        self.packages = ChainingHashTable(16)
        self.miles = 0
        self.time = time(0, 0)
        self.time_spent = timedelta()

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
            self.packages.insert(i, address)
            
        
