class EntranceGate:
    def __init__(self, gate_id:int, parking_lot:ParkingLot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot

    def allowEntry(self, vehicle:Vehicle):
        return self.parking_lot.park_vehicle(vehicle)
        
