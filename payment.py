from enum import Enum

class PaymentType(Enum):
    CREDIT = 1
    DEBIT = 2
    UPI = 3
    CASH = 4