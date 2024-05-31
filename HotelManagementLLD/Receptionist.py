class Receptionist(staff):
    def check_in_guest(self, guest, hotel, room_number):
        return hotel.check_in_guest(guest, room_number)
    
    def check_out_guest(self, guest, hotel, room_number):
        return hotel.check_out_guest(guest, room_number)
        
