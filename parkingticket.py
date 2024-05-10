from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Dict
)

if TYPE_CHECKING:
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
        self.parkingspacetype = parkingspacetype
        self.total_cost: float = 0.0
        self.parkingticketstatus = parkingticketstatus
    
    def updateExitTime(self) -> None:
        self.vehicleexittime = datetime.now()
    
    def updateTotalCost(self) -> None:
        mapping: Dict[int, float] = {
            1: 1.99,
            2: 4.99,
            3: 7.99
        }
        cost_per_hour = mapping[self.parkingspacetype]
        total_hours = (datetime.now() - self.vehicleentrytime).hours

        self.total_cost = cost_per_hour * total_hours
        self.updateExitTime()