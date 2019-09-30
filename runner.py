from human_class import *
from pet_class import *
from client_class import *
from vet_class import *
from appointment_class import *


#as a user i can creata a pet
    #manually do pet1 = pet(.....)
pet1 = Pet('D001', 'Deano', 'German Sheperd', 'Bryant Smith')
pet2 = Pet('D002', 'Leyla', 'Bulldog', 'Bryant Smith')
pet3 = Pet('D003', 'Ricardo', 'Boston Terrier', 'Bryant Smith')
pet4 = Pet('D004', 'Pat', 'BullDog', 'Tyron Josh')
pet5 = Pet('D005', 'Millie', 'German Sheperd', 'Sallie Ashley')
pet6 = Pet('D006', 'Sacha', 'Dashund', 'Ashley Tasneen')


# As a user I can add a pet to appointment
        #before assiging a dog to an appointment, one must select a vet
        # pet1.assignedAppointment1
        # pet2.assignedAppointment2
vet1 = Vet('Romans', 'Taylor', '07845125486', 'taylor@gmail.com', 'Microbiology')
vet2 = Vet('Sandra', 'Rhena', '07748462548', 'rhena@gmail.com', 'Toxicology')
vet3 = Vet('Peat', 'Alex', '07844152864', 'alex@gmail.com', 'Nutrition')


app1 = Appointment('Kennel Cough', 12/05/2019, '£30.00', pet2, vet1 )
app2 = Appointment('Canine Coronavirus', 18/08/2019, '£45.00', pet1, vet3)
app3 = Appointment('Leptospirosis', 15/07/2019, '£25.00', pet4, vet1 )
app4 = Appointment('Rabies', 19/06/2019, '£30.00', pet6, vet2)
app5 = Appointment('Canine Coronavirus', 19/06/2019, '£30.00', pet3, vet3)









#As a user i can list appointments (Need To see what pets are there)
# keep list of generated dog appointment ( details include, vet and owner app1 = mia, vet1, client1)
    #have an empty list to star with then append each appointment
    # then append to list. Should look like something`
           "appointment_list.append(appointment1)

         # for appointmen in appointment_list:
                #print appointment.getdetils





def add_passenger_to_expo(self, passenger):
    # get the list and add the pass
    if self.__passenger_list.append(passenger):

        return True
    else:
        return False

#As a user i can get pet details and owner details FOR one pet
#maybe use of dictionnary
#pet1.showDetails
pet_Description = {}
pet name
pet bread
ower
own phone number
owner email
owner name
}

return pet description

for pet in pet list
    print the above