from datetime import time, timedelta, datetime
from hash_table import ChainingHashTable
from packages import Packages
from greedy_algolithm import GreedyAlgolithm


class Track:
    def __init__(self):
        # Initialize truck attributes
        self.packages_array = []  # Stores addresses of packages assigned to the truck
        self.id_array = []  # Stores package IDs assigned to the truck
        self.packages_info = []  # Stores package information
        self.miles = 0  # Total miles traveled by the truck
        self.time = time(0, 0)  # Start time of the truck's delivery
        self.time_spent = timedelta()  # Total time spent on delivery
        self.current_address = " HUB"  # Current location of the truck, default is HUB

    def count_miles(self, miles):
        # Add traveled miles to the truck's total mileage
        self.miles += miles

    def set_time(self, h, m):
        # Set the start time for the truck
        self.time = time(h, m)

    def update_time(self, hours, minutes):
        # Update the truck's current time
        self.time = time(hours, minutes)

    def calculate_time(self, miles):
        # Calculate the time spent based on miles traveled
        hours_spent = miles / 16  # Assuming a fixed speed
        additional_time = timedelta(hours=hours_spent)
        self.time_spent += additional_time

    def get_time(self):
        # Calculate and return the current time of the truck
        placeholder_date = datetime(2000, 1, 1)
        current_datetime = datetime.combine(placeholder_date, self.time)
        new_datetime = current_datetime + self.time_spent
        return new_datetime.time()

    def assign_package(self, package_ids, packages_info, track_name):
        # Assign packages to the truck
        package_ids = [str(item) for item in package_ids]
        self.id_array = package_ids
        self.packages_info = packages_info
        for i in package_ids:
            # Update package information with the truck's name and address
            packages_info.search(str(i)).track = track_name
            address = self.packages_info.search(str(i)).address
            self.packages_array.append(address)

    def deliver(self, end):
        # Deliver packages until the specified end time
        end_hour, end_minute = end
        if self.get_time() >= time(end_hour, end_minute):
            return  # Stop delivery if current time exceeds end time

        # Mark all packages as 'en route' at the start of delivery
        for i in self.id_array:
            self.packages_info.search(i).delivery_status = "en route"

        greedy_algolithm_instance = GreedyAlgolithm()

        # Continue delivery until all packages are delivered or time runs out
        while self.packages_array:
            next_address, miles = greedy_algolithm_instance.greedy_algolithm(
                current_location=self.current_address,
                packages_array=self.packages_array,
            )
            if next_address is None:
                break  # Stop if there are no more addresses to deliver

            # Update truck's mileage and time after each delivery
            self.count_miles(miles)
            self.calculate_time(miles)
            if self.get_time() >= time(end_hour, end_minute):
                break  # Stop delivery if current time exceeds end time

            # Update package delivery status and time
            delivered_package_id = str(
                self.id_array[self.packages_array.index(next_address)]
            )
            self.packages_info.search(
                delivered_package_id
            ).delivered_time = self.get_time()
            self.packages_info.search(
                delivered_package_id
            ).miles_from_last_location = miles
            self.packages_info.search(
                delivered_package_id
            ).delivery_status = "Delivered"

            # Remove delivered package from truck's tracking arrays
            if self.current_address != " HUB":
                self.packages_array.remove(self.current_address)
                self.id_array.remove(delivered_package_id)
            self.current_address = next_address

    def back_to_hub(self):
        # Calculate and travel back to the hub after deliveries
        greedy_algolithm_instance = GreedyAlgolithm()
        hub, miles = greedy_algolithm_instance.greedy_algolithm(
            self.current_address, [" HUB"]
        )
        self.count_miles(miles)
        print(f"Track 1 Back to Hub: Traveled {miles}miles")

