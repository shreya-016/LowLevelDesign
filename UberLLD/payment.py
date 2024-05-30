class Payment:
    def __init__(self, ride_id, amount, payment_method):
        self.ride_id = ride_id
        self.amount = amount
        self.payment_method = payment_method
        self.status = "pending" 

    def make_payment(self):
        if self.status != "pending":
            return {'message': 'Payment already processed!', 'status': self.status}
            if self.payment_method == "credit_card":
            self.status = "completed"
            return {'message': 'Payment completed successfully!', 'status': self.status}
        elif self.payment_method == "wallet":
            self.status = "completed"
            return {'message': 'Payment completed successfully!', 'status': self.status}
        else:
            self.status = "failed"
            return {'message': 'Unsupported payment method!', 'status': self.status}

    def process_post_payment(self):
        if self.status != "completed":
            return {'message': 'Payment not completed!', 'status': self.status}
        self.status = "completed"
        return {'message': 'Post-payment processed successfully!', 'status': self.status}
