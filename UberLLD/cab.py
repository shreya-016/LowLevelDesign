class Cab:
    def __init__(self, cab_type, driver_id, reg_no):
        self.id = generate_uuid()
        self.type = cab_type
        self.driver_id = driver_id
        self.reg_no = reg_no

    def register(self):
        if self.reg_no in [cab.reg_no for cab in cabs_db.values()]:
            raise ValueError("Car with this registration number already exists")
        cabs_db[self.id] = self
        return ("Car registration successful")

    def get_details(self):
        return = {
            'id': self.id,
            'type': self.cab_type,
            'driver_id': self.driver_id,
            'reg_no': self.reg_no
        }
    
    def update_details(self, cab_type=None, reg_no=None):
        if type:
            self.type = cab_type
        if reg_no:
            if reg_no in [cab.reg_no for cab in cabs_db.values()]:
                raise ValueError("Cab with this registration number already exists.")
            self.reg_no = reg_no
        cabs_db[self.id] = self
        return {'message': 'Cab details updated successfully!'}
