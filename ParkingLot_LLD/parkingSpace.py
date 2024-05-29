class ParkingSpace:
    def __init__(self, space_id:int, is_reserved = False):
        self.space_id = space_id
        self.is_reserved = is_reserved
        self.is_occupied = False
        self.vehicle = None

    def park_vehicle(self, vehicle: Vehicle):
        if not self.is_occupied:
            self.vehicle = vehicle
            self.is_occupied = True
            return True
        return False

    def remove_vehicle(self):
        if self.is_occupied:
            self.vehicle = None
            self.is_occupied = False
            return True
        return False

