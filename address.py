from exceptions import NotValidAddressException
class Address:
    def __init__(self, address_1: str, 
                 address_2: str, 
                 city: str, 
                 state: str, 
                 country: str, 
                 pincode: int):
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.country = country
        self.pincode = pincode
        self.validateAddress()
    
    # dummy validation
    def validateAddress(self):
        if type(self.address_1) != str or type(self.address_2) != str:
            raise NotValidAddressException