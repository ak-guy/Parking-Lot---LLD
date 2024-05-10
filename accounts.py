from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from address import Address
    from parkinglot import ParkingLot
    from parkingfloor import ParkingFloor
    from parkingspace import ParkingSpace
    from parkingdisplayboard import ParkingDisplayBoard
    from payment import PaymentType, Payment
    from vehicle import Vehicle
    from parkingticket import ParkingTicket

class Accounts:
    def __init__(self, name: str,
                 email: str,
                 password: str,
                 employeeId: int,
                 address: Address):
        self.name = name
        self.email = email
        self.password = password
        self.employeeId = employeeId
        self.address = address

class Admin(Accounts):
    def addParkingFloor(self, parkinglot: ParkingLot, parkingfloor: ParkingFloor) -> None:
        parkinglot._parkingfloors.append(parkingfloor)

    def addParkingSpace(self, parkingfloor: ParkingFloor, parkingspace: ParkingSpace) -> None:
        parkingfloor.parkingspaces.append(parkingspace)

    def addDisplayBoard(self, parkingfloor: ParkingFloor, parkingdisplayboard: ParkingDisplayBoard) -> None:
        parkingfloor.parkingdisplayboard = parkingdisplayboard

class ParkingAttendant(Accounts):
    def __init__(self, name: str,
                 email: str,
                 password: str,
                 employeeId: int,
                 address: Address):
        super().__init__(name, email, password, employeeId, address)
        
    def createTicket(self, vehicle: Vehicle) -> ParkingTicket:
        pass

    def processPayment(self, parkingticket: ParkingTicket, paymenttype: PaymentType):
        '''
        from here we will make call to Payment.makepayment(parkingticket, paymenttype)
        '''
        pass