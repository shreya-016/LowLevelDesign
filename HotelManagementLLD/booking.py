class Booking:
    def __init__(self, guest, hotel, room, check_in_date, check_out_date):
        self.guest = guest
        self.hotel = hotel
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_status = Booking_status.PENDING