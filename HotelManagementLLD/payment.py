class Payment:
    def __init__(self, booking, amount, payment_method):
        self.booking = booking
        self.amount = amount
        self.payment_method = Payment_method
        self.payment_status = Payment_status.PENDING

    def process_payment(self):
        print(f"Processing payment of {self.amount} via {self.payment_method.name}")
        self.payment_status = Payment_status.COMPLETED
