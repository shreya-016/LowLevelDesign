class ParkingDisplayBoard:
    def __init__(self, parking_lot: ParkingLot):
        self.parking_lot = parking_lot

    def display(self):
        available_spots = [space.space_id for space in self.parking_lot.spots.values() if not space.is_occupied]
        print(f"Available spots: {available_spots}")