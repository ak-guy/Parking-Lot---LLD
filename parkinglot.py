from typing import (
    Dict,
    List
)
from gate import EntranceGate, ExitGate
from address import Address
from parkingfloor import ParkingFloor

class SingletonParkingLot(type):
    _instances: Dict['SingletonParkingLot', 'ParkingLot'] = {}

    def __call__(self, *args, **kwargs):
        if self not in SingletonParkingLot._instances:
            parkinglot_instance = super().__call__(*args, **kwargs)
            SingletonParkingLot._instances[self] = parkinglot_instance
        
        return SingletonParkingLot._instances[self]

class ParkingLot(metaclass=SingletonParkingLot):
    _parkingfloors: List[ParkingFloor] = []
    _entrance_gate: List[EntranceGate] = []
    _exit_gate: List[ExitGate] = []
    
    def __init__(self, name: str, address: Address):
        self.name = name
        self.adress = address
