from datetime import datetime
from enum import Enum
from parkingspace import ParkingSpaceType

class ParkingTicketStatus(Enum):
    PAID = 1
    ACTIVE = 2

class ParkingTicket:
    def __init__(self, ticketId: int,
                 levelId: int, 
                 spaceId: int,
                 parkingspacetype: ParkingSpaceType,
                 parkingticketstatus: ParkingTicketStatus):
        self.ticketId = ticketId
        self.levelId = levelId
        self.spaceId = spaceId
        self.vehicleentrytime = datetime.now()
        self.vehicleexittime: datetime = None
        self.parkingspacetype: float = parkingspacetype
        self.total_cost = 0.0
        self.parkingticketstatus = parkingticketstatus
    
    def updateExitTime(self) -> None:
        self.vehicleexittime = datetime.now()
    
    def updateTotalCost(self, total_cost: float) -> None:
        pass