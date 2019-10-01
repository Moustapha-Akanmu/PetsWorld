from pet_class import *
class Appointment():
    def __init__(self, disease, date, price, pet = ' ', vet = ' '):
        self.disease = disease
        self.date = date
        self.price = price
        self.pet = pet
        self.vet = vet
        self.appointment_list = []

    def assign_vet(self):
        return self.vet

    def assign_pet(self):
        return self.pet

    def assign_appointment(self, *pet):
        if self.appointment_list.append(self):
            return True
        else:
            return False

    def pet_details(self):
        view_pet_details = {
            'name': self.pet.name,
            'id': self.pet.vet_id,
            'disease': self.disease,
            'appointment Date': self.date,
            'breed': self.pet.breed,
            'owner_name': self.pet.owner
        }
        return view_pet_details()

