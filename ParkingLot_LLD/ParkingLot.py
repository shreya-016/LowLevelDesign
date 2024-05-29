from datetime import datetime

class ParkingLot:
    def __init__(self, total_spots: int):
        self.total_spots = total_spots
        self.spots = {space_id: ParkingSpace(space_id) for space_id in range(1, total_spots+1)}
        self.tickets = {}
        self.next_ticket_id = 1

    def find_available_space(self):
        for space in self.spots.values():
            if not space.is_occupied:
                return space
        return None

    def park_vehicle(self, vehicle:Vehicle):
        available_space = self.find_available_space()
        if available_space:
            ticket = Ticket(self.next_ticket_id, available_space.space_id, vehicle)
            self.tickets[self.next_ticket_id] = ticket
            available_space.park_vehicle(vehicle)
            self.next_ticket_id += 1
            return ticket
        return None

    def remove_vehicle(self, ticket_id: int) -> bool:
        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]
            spot_id = ticket.space_id
            if self.spots[spot_id].remove_vehicle():
                del self.tickets[ticket_id]
                return True
        return False
