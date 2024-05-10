from __future__ import annotations
from typing import (
    Dict,
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from parkingspace import ParkingSpaceType

class ParkingDisplayBoard:
    def __init__(self, freespotavailable: Dict[ParkingSpaceType, int] = {}):
        self.freespotavailable = freespotavailable
    
    def updateFreeSpotAvailable(self, parkingspottype: ParkingSpaceType, spaces: int):
        pass
