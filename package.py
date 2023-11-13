class Package:
    def __init__(self, address, city, state, zip_code, deadline, weight, note):
        # Constructor for the Package class. Initializes package details.
        self.address = address  # Address where the package needs to be delivered.
        self.city = city  # City of the delivery address.
        self.state = state  # State of the delivery address.
        self.zip_code = zip_code  # Zip code of the delivery address.
        self.deadline = deadline  # Delivery deadline for the package.
        self.weight = weight  # Weight of the package.
        self.note = note  # Any special notes related to the package.
        self.delivery_status = "at HUB"  # Initial delivery status of the package.
        self.delivered_time = (
            None  # Time when the package was delivered. None initially.
        )
        self.miles_from_last_location = None  # Miles traveled from the last location.
        self.track = ""  # The track assigned to deliver the package.

    def print_all(self):
        # Method to print all details of the package.
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip Code: {self.zip_code}")
        print(f"Deadline: {self.deadline}")
        print(f"Weight: {self.weight}")
        print(f"Note: {self.note}")
        print(f"Is Delivered: {self.delivery_status}")
        print(f"Delivered Time: {self.delivered_time}")
        print(f"Miles from Last Location: {self.miles_from_last_location}")
        print(f"Delivered by {self.track}")
