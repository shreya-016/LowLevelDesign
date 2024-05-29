class ParkingAttendant:
    def __init__(self, name:str, parking_lot:ParkingLot):
        self.name = name
        self.parking_lot = parking_lot

    def issue_ticket(self, vehicle:Vehicle):
        return self.parking_lot.park_vehicle(vehicle)

    def process_payment(self, ticket_id:int, amount:float):
        if ticket_id in self.parking_lot.tickets:
            ticket = self.parking_lot.tickets[ticket_id]
            if not ticket.paid:
                ticket.paid = True
                print(f"Payment of {amount} received for ticket ID {ticket_id}")
                return True
        return False

    def remove_vehicle(self, ticket_id):
        return self.parking_lot.remove_vehicle(ticket_id)