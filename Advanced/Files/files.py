"""
    file = open("Advanced/Files/file.txt", "r") # open in read mode 
    print(file.read())
    file.close()
"""

# read a file - with statements provides cleanup operations (open/close)
with open("Advanced/Files/file.txt", "r") as file:
    line1 = file.readlines()[0] # gives us each line in file, access first line
    print([line1.strip()]) # removes whitespace left or right of text
    
# write to a new file
with open("Advanced/Files/file2.txt", "w") as file:
    file.write("Hello world this is a new file created here \n")
    file.write("added line")
    
# append to an existing file - cursor at end of the file
with open("Advanced/Files/file2.txt", "a") as file:
    file.write("\nappended content \n")

# reading and writing - puts cursor at beginning of file
with open("Advanced/Files/file3.txt", "r+") as file:
    score = file.read()
    print(score)
    new_score = int(score) + 1 
    file.seek(0) # bring us back to beginning of file (over ride what's there w/ read operation) | 1 is reference point and 0 is end of file
    file.write(str(new_score)) # convert back to string to write

#iterate over a file and read specific lines
with open("Advanced/Files/file4.txt", "r+") as file:
   
    for i, line in enumerate(file):
        print(line, end="")
        if i == 2:
            break
        
    
# Excercise one         
text = ""

with open("Advanced/Files/file4.txt", "r") as file:
    text = file.read()

escape_characters_removed = text.replace("\n", "")
punctuation_removed = escape_characters_removed.replace(",", "").replace("-", "").replace(".","")

words = punctuation_removed.split(" ")
empty_strings = words.count("")
number_of_words = len(words) - empty_strings

print(number_of_words)

# Excercise Two - write to a file the squares of numbers from 0 to 50

with open("Advanced/Files/file6.txt", "w") as file:
    for i in range (1, 51):
        square = i ** 2
        file.write(str(square) + "\n")