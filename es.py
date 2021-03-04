# Program that counts amount of letter 'e' in Moby Dick
# Author: Magdalena Malik

countOfE = 0
fileToRead = input("enter a file name: ")
with open(fileToRead, "rt") as f:
    text = f.read()
    list_of_text = text.split()
    count = 0
    for element in list_of_text:
        element = element.lower() # making all words in lower case to count all "e"
        count = element.count("e")
        countOfE = countOfE + count
    print("number of letter 'e' in text is: ", countOfE)
