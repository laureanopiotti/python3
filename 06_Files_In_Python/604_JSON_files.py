import json


# JSON LOAD AND DUMP (FP)

json_file = open('604_friends_json.txt','r')
file_contents = json.load(json_file) # Reads file and turns it to dictionary
json_file.close()

print(file_contents)



for friend in file_contents:
    print(f'{friend}')

cars = [
    {'make':'Ford','model':'Fiesta'},
    {'make':'Ford','model':'Focus'}
]

json_file = open('604_cars_json.txt','a')
json.dump(cars,json_file) # Takes dic and writes to fp (file pointer)



# JSON LOADS AND DUMPS
my_json_string = '[{"name":"Alfa Romeo","released":1950}]'

incorrect_car = json.loads(my_json_string)

print(incorrect_car[0]['name'])



