import json


# json_file = open('604_friends_json.txt','r')
# file_contents = json.load(json_file) # Reads file and turns it to dictionary
# json_file.close()

with open('604_friends_json.txt','r') as file:
    file_contents = json.load(file) # Reads file and turns it to dictionary

print(file_contents)



for friend in file_contents:
    print(f'{friend}')

cars = [
    {'make':'Ford','model':'Fiesta'},
    {'make':'Ford','model':'Focus'}
]

with open('604_cars_json.txt','a') as json_file:
    json.dump(cars,json_file) # Takes dic and writes to fp (file pointer)



# JSON LOADS AND DUMPS
my_json_string = '[{"name":"Alfa Romeo","released":1950}]'

incorrect_car = json.loads(my_json_string)

print(incorrect_car[0]['name'])



