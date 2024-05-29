class ExitGate:
    def __init__(self, gate_id:int, parking_lot:ParkingLot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot

    def allowExit(self, ticket_id:int):
        if ticket_id in self.parking_lot.tickets:
            ticket = self.parking_lot.tickets[ticket_id]:
            if ticket.paid:
                return self.parking_lot.remove_vehicle(ticket_id)
        return False
