#create a new file
new_file = open('newfile.txt', 'x')
new_file.close()

#check if a file exists
import os
print("Checking if my_file exists or not.....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")
    
#create a new if it doesn't
my_file = open("my_file.txt", 'w')
my_file.write("Hi! I am Royce and i am 14 yr old.")
my_file.close()

#delete file names codingal
os.remove('Codingal.txt')

#delete the folder
os.rmdir('Folder')