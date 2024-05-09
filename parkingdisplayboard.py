from typing import Dict
from parkingspace import ParkingSpaceType

class ParkingDisplayBoard:
    def __init__(self, freespotavailable: Dict[ParkingSpaceType, int]):
        self.freespotavailable = freespotavailable
    
    def updateFreeSpotAvailable(self, parkingspottype: ParkingSpaceType, spaces: int):
        pass
