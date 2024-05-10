from __future__ import annotations
from enum import Enum
from parkingticket import ParkingTicket

from typing import (
    TYPE_CHECKING
)

if TYPE_CHECKING:
    from datetime import datetime

class PaymentType(Enum):
    CREDIT = 1
    DEBIT = 2
    UPI = 3
    CASH = 4

class PaymentStatus(Enum):
    UNPAID = 1
    PENDING = 2
    COMPLETED = 3
    DECLINED = 4
    CANCELLED= 5
    REFUNDED = 6

class PaymentInfo:
    def __init__(self, amount: float,
                 paymentdate: datetime,
                 transaction_id: int,
                 parkingticket: ParkingTicket,
                 paymentstatus: PaymentStatus):
        self.amount = amount
        self.paymentdate = paymentdate
        self.transaction_id = transaction_id
        self.parkingticket = parkingticket
        self.paymentstatus = paymentstatus

class Payment:
    '''
    main api for making payment, here it will take parking ticket, calculate total amount that has to be paid
    '''
    @staticmethod
    def makePayment(parkingticket: ParkingTicket, paymenttype: PaymentType) -> PaymentInfo:
        parkingticket.updateTotalCost()
        total_amount = parkingticket.total_cost

        # remaining logic needs to be implemented