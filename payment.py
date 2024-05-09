from enum import Enum

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
    pass

class Payment:
    pass