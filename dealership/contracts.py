from .customers import Customer, Employee
from .vehicles import Car, Truck, Motorcycle


class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    def total_value(self):
        price = self._total_value()
        if self.customer.is_employee():
            return price * 0.9
        return price

    def monthly_value(self):
        return self.total_value() / self._monthly_attribute()



class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
    
    def _total_value(self):
        VEHICLE_MULTIPLIERS = {
            Car: 1.07,
            Motorcycle: 1.03,
            Truck: 1.11
        }
        multiplier = VEHICLE_MULTIPLIERS[self.vehicle.__class__]

        sale_price =  self.vehicle.sale_price()
        return sale_price + (multiplier * self.monthly_payments * sale_price / 100)

    def _monthly_attribute(self):
        return self.monthly_payments



class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def _total_value(self):
        VEHICLE_MULTIPLIERS = {
            Car: 1.2,
            Motorcycle: 1,
            Truck: 1.7
        }
        multiplier = VEHICLE_MULTIPLIERS[self.vehicle.__class__]

        sale_price = self.vehicle.sale_price()
        return sale_price + (sale_price * multiplier / self.length_in_months)

    def _monthly_attribute(self):
        return self.length_in_months
