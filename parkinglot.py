from __future__ import annotations
from typing import (
    Dict,
    List,
    TYPE_CHECKING
)
from address import Address
from accounts import Admin, ParkingAttendant
from parkingfloor import ParkingFloor
from parkingdisplayboard import ParkingDisplayBoard

if TYPE_CHECKING:
    from gate import EntranceGate, ExitGate

class SingletonParkingLot(type):
    _instances: Dict[SingletonParkingLot, ParkingLot] = {}

    def __call__(self, *args, **kwargs):
        if self not in SingletonParkingLot._instances:
            parkinglot_instance = super().__call__(*args, **kwargs)
            SingletonParkingLot._instances[self] = parkinglot_instance
        
        return SingletonParkingLot._instances[self]

class ParkingLot(metaclass=SingletonParkingLot):
    
    def __init__(self, name: str, address: Address):
        self.name = name
        self.adress = address
        self._parkingfloors: List[ParkingFloor] = []
        self._entrance_gate: List[EntranceGate] = []
        self._exit_gate: List[ExitGate] = []
        self._admins: List[Admin] = []
        self._parking_attendants: List[ParkingAttendant] = []
    
    def addAdmin(self, admin: Admin):
        self._admins.append(admin)
    
    def addParkingAttendants(self, parkingattendant: ParkingAttendant):
        self._parking_attendants.append(parkingattendant)


if __name__ == '__main__':
    parking_address_obj = Address('bor','ad','erg','afe','tyj',123255)
    admin_address_obj = Address('sdbre', 'ag', 'reh', 'svdf', 'egr', 122018)
    parkingattendant_address_obj = Address('nboie', 'aerhg', 'revah', 'vesvdf', 'esejnugr', 12287658)
    parking_lot_obj = ParkingLot('xyz', parking_address_obj)
    admin_obj = Admin('Arpit', 'arp@g.com', 'aieo', 123, admin_address_obj)
    parkingattendant_obj = ParkingAttendant('someone', 's@gm.com', '2boib', 542, parkingattendant_address_obj)
    parking_lot_obj.addParkingAttendants(parkingattendant_obj)
    parking_lot_obj.addAdmin(admin_obj)
    parkingdisplayboard_obj = ParkingDisplayBoard()
    parking_floor_obj = ParkingFloor(1, parkingdisplayboard_obj)
    print(parking_lot_obj._admins[0].name)
    admin_obj.addParkingFloor(parking_lot_obj, parking_floor_obj)
    print(parking_lot_obj._parkingfloors[0].floor_id)