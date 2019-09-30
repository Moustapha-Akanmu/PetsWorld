from human_class import *
class Client(Human):

    def __init__(self, f_name, l_name, phone, email, payment_type ):
        super().__init__(f_name, l_name, phone, email)
        self.payment_type = payment_type


