from datetime import datetime
from uuid import uuid4
from enum import Enum

customer_db = {}

def generate_uuid():
    return str(uuid4())

class Customer:
    def __init__(self, name, email):
        self.id = generate_uuid()
        self.name = name
        self.email = email
        self.created_at = datetime.utcnow()

    def register(self):
        if self.email in customer_db:
            raise ValueError("Customer already exists")
        customer_db[self.id] = self
        return ("Customer registered successfully")

    def update_details(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            if email in [customer.email for user in customer_db.values()]:
                raise ValueError("Email already in use.")
            self.email = email


    def get_details(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at
        }
