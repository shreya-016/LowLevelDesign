from enum import Enum, auto

class Room_type(Enum):
    AVAILABLE = auto()
    BOOKED = auto()

class User_type(Enum):
    ADMIN = auto()
    MANAGER = auto()
    RECEPTIONIST = auto()
    HOUSEKEEPING = auto()
    STAFF = auto()
    GUEST = auto()

class Booking_status(Enum):
    PENDING = auto()
    COMPLETED = auto()

class Payment_status(Enum):
    PENDING = auto()
    COMPLETED = auto()

class Payment_method(Enum):
    CREDIT_CARD = auto()
    DEBIT_CARD = auto()
    CASH = auto()

class Account_status(Enum):
    ACTIVE = auto()
    INACTIVE = auto()

class Room_status(Enum):
    AVAILABLE = auto()
    BOOKED = auto()
