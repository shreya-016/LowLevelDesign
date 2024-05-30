rides_db = {}

class Ride:
    def __init__(self, customer_id, driver_id, source, destination, status):
        self.id = generate_uuid()
        self.customer_id = customer_id
        self.driver_id = driver_id
        self.source = source
        self.destination = destination
        self.status = status


    def book_ride(customer_id, source, destination):
        driver_id = find_available_driver()
        new_ride = Ride(customer_id, driver_id, "pending", source, destination)
        rides_db[new_ride.id] = new_ride
        return {'message': 'Ride booked successfully!', 'ride_id': new_ride.id}

    def search_ride(customer_id):
        available_trips = [ride.get_details() for trip in rides_db.values() if trip.status == "pending"]
        return available_rides

    def find_available_driver():
        for driver in drivers_db.values():
            if driver.is_available():
                driver.set_availability(False)
                return driver.id
        return None
    
    def track_ride(customer_id, ride_id):
        if ride_id not in rides_db:
            raise ValueError("Ride does not exist.")
        ride = rides_db[ride_id]
        if ride.customer_id != customer_id:
            raise ValueError("You are not authorized to track this ride.")
        return ride.get_details()
    
    def update_ride(ride_id, new_status):
        if ride_id not in rides_db:
            raise ValueError("Ride does not exist.")
        ride = rides_db[ride_id]
        ride.status = new_status
        rides_db[ride_id] = ride
        return {'message': 'Ride status updated successfully!'}

    def get_details(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'driver_id': self.driver_id,
            'status': self.status,
            'source': self.source,
            'destination': self.destination
        }


