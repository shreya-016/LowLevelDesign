class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        self.guests = []
        self.staffs = []
        self.services = []
        self.bookings = []

    def add_room    (self, room):
        self.rooms.append(room)

    def find_room_by_number(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def check_room_availability(self, room_number):
        room = self.find_room_by_number(room_number)
        if room and room.room_status == Room_status.AVAILABLE:
            return True
        return False

    def add_staff(self, staff):
        self.staffs.append(staff)

    def get_staff_details(self, staff_id):
        for staff in self.staffs:
            if staff.staff_id == staff_id:
                return staff
        return None

    def update_staff_details(self, user_type=None, name=None, staff_id):
        staff = self.get_staff_details(staff_id)
        if staff:
            if name:
                staff.name = name
            if user_type:
                staff.user_type = User_type
            return True
        return False

    def add_guest(self, guest):
        self.guests.append(guest)

    def get_guest_details(self, guest_id):
        for guest in self.guests:
            if guest.guest_id == guest_id:
                return guest
        return None

    def add_service(self, service):
        self.services.append(service)
