from typing import (
    List
)
from parkingspace import ParkingSpace
from parkingdisplayboard import ParkingDisplayBoard

class ParkingFloor:
    def __init__(self, floor_id: int,
                 isFull: bool,
                 parkingspaces: List[ParkingSpace],
                 parkingdisplayboard: ParkingDisplayBoard):
        self.floor_id = floor_id
        self.isFull = isFull
        self.parkingspaces = parkingspaces
        self.parkingdisplayboard = parkingdisplayboard
    