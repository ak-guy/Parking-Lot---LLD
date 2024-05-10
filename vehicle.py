from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING
from exceptions import NotValidVehicleException

if TYPE_CHECKING:
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
        self.validateVehicle()

    def validateVehicle(self):
        valid = True
        if not valid:
            raise NotValidVehicleException