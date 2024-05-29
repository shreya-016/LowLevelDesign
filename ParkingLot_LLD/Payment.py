class Payment:
    def __init__(self, ticket_id, amount:float):
        self.ticket_id = ticket_id
        self.amount = amount
        self.paid_at = datetime.now()

    def process(self):
        print(f"Processing payment of {self.amount} for ticket ID {self.ticket_id}")
        return True