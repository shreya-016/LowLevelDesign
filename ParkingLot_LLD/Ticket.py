Copy code
class Ticket:
    def __init__(self, ticket_id: int, space_id: int, vehicle: Vehicle):
        self.ticket_id = ticket_id
        self.space_id = space_id
        self.vehicle = vehicle
        self.paid = False