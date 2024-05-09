from vehicle import Vehicle

class ParkingSpaceType:
    TWOWHEELER = 1
    FOURWHEELER = 2
    SIXWHEELER = 3

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
