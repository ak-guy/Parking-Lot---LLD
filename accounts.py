from address import Address
from parkinglot import ParkingLot
from parkingfloor import ParkingFloor
from parkingspace import ParkingSpace
from parkingdisplayboard import ParkingDisplayBoard
from payment import PaymentType
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
        pass

    def addParkingSpace(self, parkingfloor: ParkingFloor, parkingspace: ParkingSpace) -> None:
        pass

    def addDisplayBoard(self, parkingfloor: ParkingFloor, parkingdisplayboard: ParkingDisplayBoard) -> None:
        pass

class ParkingAttendant(Accounts):
    def createTicket(self, vehicle: Vehicle) -> ParkingTicket:
        pass

    def processPayment(self, parkingticket: ParkingTicket, paymenttype: PaymentType):
        pass