from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from accounts import ParkingAttendant
    from parkingticket import ParkingTicket
    from payment import PaymentType
    from vehicle import Vehicle


class Gate:
    def __init__(self):
        self.gateId = 0
        self.parkingattendant: ParkingAttendant = None

class EntranceGate(Gate):
    def getParkingTicket(self, vehicle: Vehicle = Vehicle.CAR) -> ParkingTicket:
        pass

class ExitGate(Gate):
    def payParkingTicket(self, parkingticket: ParkingTicket, paymenttype: PaymentType = PaymentType.CASH) -> bool:
        pass