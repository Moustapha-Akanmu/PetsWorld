
from pet_class import *
from client_class import *
from vet_class import *
from appointment_class import *

#init__(self, f_name, l_name, phone, email, payment_type ):

client1 = Client('Bryant', 'Smith', '07845124965', 'dubois@yahoo.fr', 'cash')
client2 = Client('Tyron', 'Josh','07845124965', 'travis@yahoo.fr', 'card')
client3 = Client('Sallie', 'Ashley','07845124965', 'bees@yahoo.fr', 'cash')
client4 = Client('Angela', 'Maya','07845124965', 'angela@yahoo.fr', 'card')



vet1 = Vet('Romans', 'Taylor', '07845125486', 'taylor@gmail.com', 'Microbiology')
vet2 = Vet('Sandra', 'Rhena', '07748462548', 'rhena@gmail.com', 'Toxicology')
vet3 = Vet('Peat', 'Alex', '07844152864', 'alex@gmail.com', 'Nutrition')

vet_list =[vet1, vet2, vet3]

#as a user i can creata a pet
    #manually do pet1 = pet(.....)
pet1 = Pet('D001', 'Deano', 'German Sheperd', 'Bryant Smith')
pet2 = Pet('D002', 'Leyla', 'Bulldog', 'Bryant Smith')
pet3 = Pet('D003', 'Ricardo', 'Boston Terrier', 'Bryant Smith')
pet4 = Pet('D004', 'Pat', 'BullDog', 'Tyron Josh')
pet5 = Pet('D005', 'Millie', 'German Sheperd', 'Sallie Ashley')
pet6 = Pet('D006', 'Sacha', 'Dashund', 'Ashley Tasneen')

pet_list =[pet1,pet2,pet3,pet4,pet5,pet5,pet6]



# As a user I can add a pet to appointment
        #before assiging a dog to an appointment, one must select a vet


appointment1 = Appointment('Kennel Cough', '12/05/2019', '£30.00', pet2, vet1)
appointment2 = Appointment('Canine Coronavirus', '18/08/2019', '£25.00', pet1, vet3)
appointment3 = Appointment('Leptospirosis', '15/07/2019', '£25.00', pet4, vet1)
appointment4 = Appointment('Rabies', '19/06/2019', '£30.00', pet6, vet2)
appointment5 = Appointment('Canine Coronavirus', '19/06/2019', '£30.00', pet3, vet3)


appointment_list = []
appointment_list.append(appointment1)
appointment_list.append(appointment2)
appointment_list.append(appointment3)
appointment_list.append(appointment4)
appointment_list.append(appointment5)

print(type(appointment_list))

#As a user i can list appointments (Need To see what pets are there)

for appoint in appointment_list:
    print('Disease: ' + '' + appoint.disease, appoint.date + '    ' + appoint.price,'  Pet Name: ' + '' + appoint.pet.name, '     Owner: ' + '' + appoint.vet.f_name + ' ' + appoint.vet.l_name)
    print('             ')
    # As a user i can get pet details and owner details FOR one pet
    # maybe use of dictionnary
    # pet1.showDetails

# for appoint in appointement_list:
      #  for vet in pet_list
       # print()

#for appoint in appointment_list:
 #   for pet in appointment_list.pet_details()(["pet_list"]):
  #      print(pet.name, pet.breed, pet.owner_name(), pet.vet_id, pet.)





    # appoint.vet, appoint.pet)
    #print('Disease: ' + '  ' + appoint.pet_details()["date"])

           #, appointment.date, appointment.price,'Which Pet: ' + ' ' + appointment.)
    #'Book with: ' + ' ' + appointment.assign_vet() )

    #'Disease:' + ' ' + appointment.disease,' Date:' + ' ' + appointment.date,' Price:' + ' ' + appointment.price, ' Pet:' + ' ' +appointment.pet)



#for appoint in appointment_list
   # for  pets in pet detain [pet details]

# keep list of generated dog appointment ( details include, vet and owner app1 = mia, vet1, client1)
    #have an empty list to star with then append each appointment
    # then append to list. Should look like something`

         # for appointmen in appointment_list:
                #print appointment.getdetils






#As a user i can get pet details and owner details FOR one pet
#maybe use of dictionnary
#pet1.showDetails



# pet_Description = {}
# pet name
# pet bread
# ower
# own phone number
# owner email
# owner name
# }
#
# return pet description
#
# for pet in pet list
#     print the above