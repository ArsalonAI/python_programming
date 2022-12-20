"""
    file = open("Advanced/file.txt", "r") # open in read mode 
    print(file.read())
    file.close()
"""

#with statements provides cleanup operations (open/close)

with open("Advanced/file.txt", "r") as file:
    line1 = file.readlines()[0] # gives us each line in file, access first line
    print([line1.strip()]) # removes any /n from our text
    



