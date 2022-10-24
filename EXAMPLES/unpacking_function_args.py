#

people = [ # list of 4-element tuples
    ('Joe', 'Schmoe', 'Burbank', 'CA'),
    ('Mary', 'Brown', 'Madison', 'WI'),
    ('Jose', 'Ramirez', 'Ames', 'IA'),
]

def display_person(first_name, last_name, city, state): # function that takes 4 parameters
    print("{} {} lives in {}, {}".format(first_name, last_name, city, state))

joe = people[0]
display_person(joe[0], joe[1], joe[2], joe[3])
display_person(*joe)
print()

for person in people:  # person is a tuple (one element of people list)
    display_person(*person)  # {splat}person unpacks the tuple into four individual parameters
