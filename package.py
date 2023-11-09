class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip
        self.deadline = deadline
        self.weight = weight

    def print_all(self):
        print(f"ID: {self.id}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Zip Code: {self.zip_code}")
        print(f"Deadline: {self.deadline}")
        print(f"Weight: {self.weight}")