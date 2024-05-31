class Guest:
    def __init__(self, name, guest_id, user_type=User_type.REGULAR):
        self.name = name
        self.guest_id = guest_id
        self.user_type = User_type
        self.booking_status = None
        self.account_status = Account_status.ACTIVE

    def make_reservation(self, hotel, room_number):
        return hotel.check_in_guest(self, room_number)

    def cancel_reservation(self):
        if self.booking_status:
            self.booking_status.cancel()
            self.booking_status = None
