from __future__ import annotations
from typing import (
    List,
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from parkingspace import ParkingSpace
    from parkingdisplayboard import ParkingDisplayBoard

class ParkingFloor:
    def __init__(self, floor_id: int,
                 parkingdisplayboard: ParkingDisplayBoard,
                 parkingspaces: List[ParkingSpace] = [],
                 isFull: bool = False):
        self.floor_id = floor_id
        self.isFull = isFull
        self._parkingspaces = parkingspaces
        self._parkingdisplayboard = parkingdisplayboard
    
    def addParkingSpaces(self, parkingspaces: ParkingSpace):
        self._parkingspaces.append(parkingspaces)
    