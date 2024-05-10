class NotValidAddressException(Exception):
    def __init__(self, message: str = 'Address is not valid'):
        self.message = message
        super().__init__(self.message)

class NotValidVehicleException(Exception):
    def __init__(self, message: str = 'Vehicle is not valid'):
        self.message = message
        super().__init__(self.message)