from human55_class import *


class Vet(Human):
    def __init__(self, f_name, l_name, phone, email, specialization):
        super().__init__(f_name, l_name, phone, email)
        self.specialization = specialization


    def vet_name(self):
        self.f_name + '' + self.l_name