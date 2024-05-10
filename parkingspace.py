from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vehicle import Vehicle

class ParkingSpaceType(Enum):
    BIKE_PARKING = 1
    CAR_PARKING = 2
    TRUCK_PARKING = 3

class ParkingSpace:
    def __init__(self, spaceId: int,
                 isFree: bool,
                 costPerHour: float,
                 vehicle: Vehicle,
                 parkingspacetype: ParkingSpaceType):
        self.spaceId = spaceId
        self.isFree = isFree
        self.costPerHour = costPerHour
        self.vehicle = vehicle
        self.parkingspacetype = parkingspacetype