# Read File
my_file = open('601_data.txt','r')
file_content = my_file.read()
my_file.close()
print(file_content)

# Write file
user_name = input('Enter your name: ')
my_file_writing = open('601_data.txt','w') # Overwrites data
my_file_writing.write(user_name+'\n')
my_file_writing.close()

# Append to file 
user_name = input('Enter your name: ')
my_file_writing = open('601_data.txt','a')
my_file_writing.write(user_name)
my_file_writing.close()




