drivers_db = {}

class Driver:
    def __init__(self, name, email, location, cab_id, dob):
        self.id = generate_uuid()
        self.name = name
        self.email = email
        self.cab_id = cab_id
        self.location = location
        self.dob = dob

    def register(self):
        if self.email in drivers_db:
            raise ValueError("Driver email already exist")
        drivers_db[self.id] = self
        return ("Driver registered successfully")

    def update_location(self, new_location):
        self.location = new_location
        drivers_db[self.location] = self
        return ("Driver location updated successfully")

    def get_details(self):
        return = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'dob': self.dob,
            'cab_id': self.cab_id,
            'location': self.location
        }
    
    def update_details(self, name=None, email=None, location=None):
        if name:
            self.name = name
        if email:
            if email in [driver.email for driver in drivers_db.values()]:
                raise ValueError("Email already in use.")
            self.email = email
        if location:
            self.location = location
        return ("Driver details updated successfully")

    def set_availability(self, available):
        self.available = available

    def is_available(self):
        return self.available
