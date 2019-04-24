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
        VEHICLE_MULE = 0
        if isinstance (self.vehicle, Car):
            I = 1.07
        elif isinstance (self.vehicle, Motorcycle):
            I = 1.03
        elif isinstance (self.vehicle, Truck):
            I = 1.11
        tv = self.vehicle.sale_price() + (I * self.monthly_payments * self.vehicle.sale_price() / 100)
        if isinstance (self.customer, Employee):
            return tv - (tv * .1)
        return tv
        
        
    def monthly_value(self):
        return self.total_value() / self.monthly_payments
        


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def total_value(self):
        lease_multiplier = 0
        if isinstance(self.vehicle, Car):
            lease_multiplier = self.vehicle.sale_price() * 1.2/self.length_in_months
        elif isinstance(self.vehicle, Motorcycle):
            lease_multiplier = self.vehicle.sale_price() * 1/self.length_in_months
        elif isinstance(self.vehicle, Truck):
            lease_multiplier = self.vehicle.sale_price() * 1.7/self.length_in_months
        tv = self.vehicle.sale_price() + lease_multiplier
        if isinstance (self.customer, Employee):
            return tv - (tv * .1)
        return tv

    def monthly_value(self):
        return self.total_value() / self.length_in_months 


