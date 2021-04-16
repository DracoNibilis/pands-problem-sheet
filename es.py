# Program that counts amount of letter 'e' in Moby Dick
# Author: Magdalena Malik

countOfE = 0
#fileToRead = input("enter a file name: ")
fileToRead = "mobydick.txt"  
with open(fileToRead, "rt") as f: #open file to read
    text = f.read()
    list_of_text = text.split() # split text to a list 
    count = 0
    for element in list_of_text:
        element = element.lower() # making all words in lower case to count all "e"
        count = element.count("e") # counting letter "e"
        countOfE = countOfE + count # cumulated count of letter "e"
    print("number of letter 'e' in text is: ", countOfE) # printing the result
