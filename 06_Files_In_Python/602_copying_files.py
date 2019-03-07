# Ask the user for a list of 3 friends
# For each friend, tell the user whether they are nearby
# For each nearby friend, we'll save their name to `602_nearby_friends.txt`

# hint: readlines()

# My code - works! 
# friends = input('Enter three friends: ')
# friends = friends.split(' ')

# people_file = open('602_people.txt','r')
# people_list = people_file.readlines()
# people_file.close()
# for friend in friends:
#     for person in people_list:
#         if friend == person.strip():
#             nearby_friends_file = open('602_nearby_friends.txt','a')
#             nearby_friends_file.write(friend+'\n')
#             nearby_friends_file.close()

# Solution
friends = input('Enter three friend names, separated by commas: ').split(',') # ['Rolf','Jose','Charlie']

people = open('602_people.txt','r')
people_nearby = [line.strip() for line in people.readlines()] # [line1,line2,line3,line4]
people.close()

friends_set = set(friends)
people_nearby_set =  set(people_nearby)
friends_nearby_set = friends_set & people_nearby_set

nearby_friends_file = open('602_nearby_friends.txt','w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby ! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()

