class Room:
    def __init__(self, room_number, room_type, price, room_staus=Room_status.AVAILABLE):
        self.room_number = room_number
        self.room_type = Room_type
        self.price = price
        self.room_staus = Room_staus.AVAILABLE

    def book_room(self, guest_id):
        self.status = Room_status.BOOKED

    def vacate_room(self):
        self.status = Room_staus.AVAILABLE


