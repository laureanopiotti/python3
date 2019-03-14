from collections import defaultdict

# my_company = 'Teclado'

# coworkers = ['Jen','Li','Charlie','Rhys']

# other_coworkers = [('Rolf','Apple Inc.'),('Anna','Google')]

# coworkers_companies = defaultdict(lambda: my_company)

# for person, company in other_coworkers:
#     coworkers_companies[person] = company

# for person in coworkers:
#     coworkers_companies[person]

# print(coworkers_companies)


my_company = 'Teclado'

coworkers = ['Jen','Li','Charlie','Rhys']

other_coworkers = [('Rolf','Apple Inc.'),('Anna','Google')]

coworkers_companies = {}

for person, company in other_coworkers:
    coworkers_companies[person] = company

for person in coworkers:
    coworkers_companies[person] = coworkers_companies.get(person,my_company)

print(coworkers_companies)