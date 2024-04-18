from buss import Buss
from car import Car
from driver import Driver
from transport import Transport
from truck import Truck

trans = Transport()
car = Car()
buss = Buss()
truck = Truck()
driver = Driver()

print(buss.busses_need(35))
print(buss.cost_per_trip(100, 1.80))
print((buss.buss_trip_cost(35, 100, 1.80)))
print(car.cost_per_trip(100, 0.20))
print(buss.validate_date_insurance())
print(trans.validate_date_inspection())
print(truck.calculate_trucks_needed(37000))
print(truck.driver_on(driver))
print(buss.driver_on(driver))
print(truck.driver_license(driver))
print(buss.driver_license(driver))
print(car.driver_license(driver))
