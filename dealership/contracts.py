from .customers import Customer, Employee
from .vehicles import Car, Truck, Motorcycle


class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
    
    def total_value(self):

        VEHICLE_MULTIPLIERS = {
            Car: 1.07,
            Motorcycle: 1.03,
            Truck: 1.11
        }
        multiplier = VEHICLE_MULTIPLIERS[self.vehicle.__class__]

        price = self.vehicle.sale_price() + (multiplier * self.monthly_payments * self.vehicle.sale_price() / 100)
        if isinstance (self.customer, Employee):
            return price - (price * .1)
        return price
        
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
        


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def total_value(self):
        VEHICLE_MULTIPLIERS = {
            Car: 1.2,
            Motorcycle: 1,
            Truck: 1.7
        }
        multiplier = VEHICLE_MULTIPLIERS[self.vehicle.__class__]

        lease_multiplier = self.vehicle.sale_price() * multiplier/self.length_in_months
        price = self.vehicle.sale_price() + lease_multiplier

        if isinstance (self.customer, Employee):
            return price - (price * .1)
        return price

    def monthly_value(self):
        return self.total_value() / self.length_in_months 


