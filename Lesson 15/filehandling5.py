#write in file with() function
with open('CODINGAL.txt', 'w')as file:
    file.write("Hi! I am penguin and I am 1 yr old")
    file.close()
    
    #split file into words
    with open('CODINGAL.txt', 'r')as file:
        data = file.readlines()
        print("Words in this file are......")
        for line in data:
            word = line.split()
            print(word)
file.close()