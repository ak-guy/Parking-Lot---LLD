from enum import Enum
from parkingticket import ParkingTicket
from payment import PaymentInfo


class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3

class Vehicle:
    def __init__(self, license_number: str,
                 vehicletype: VehicleType,
                 parkingticket: ParkingTicket,
                 paymentinfo: PaymentInfo):
        self.license_number = license_number
        self.vehicletype = vehicletype
        self.parkingticket = parkingticket
        self.paymentinfo = paymentinfo