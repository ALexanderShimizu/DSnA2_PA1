class Package:
    def __init__(self, address, city, state, zip_code, deadline, weight, note):
        self.address = address
        self.city = city 
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.note = note 
        self.is_delivered = False
        self.delivered_time = None
        self.miles_from_last_location = None 
    
    def print_all(self):
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip Code: {self.zip_code}")
        print(f"Deadline: {self.deadline}")
        print(f"Weight: {self.weight}")
        print(f"Note: {self.note}")
        print(f"Is Delivered: {self.is_delivered}")
        print(f"Delivered Time: {self.delivered_time}")
        print(f"Miles from Last Location: {self.miles_from_last_location}")