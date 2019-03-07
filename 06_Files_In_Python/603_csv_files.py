csv_data = open('603_csv_data.txt','r')
lines = csv_data.readlines()
csv_data.close()

# Skip header
lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].capitalize()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].title()

    print(f'{name} is {age}, studying {degree} at {university}')