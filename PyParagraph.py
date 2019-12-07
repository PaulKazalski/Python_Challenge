# import the os and csv reader
# Set the directory path relative to the currrent file

import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Declare variables
paragraph = " "
letters = []
words = []
sentences = []
word_per_sent = 0
lett_per_word = 0
# Find out what paragraph to open
file_var = input("What paragraph do you want? 1 or 2?")
# opens paragraph 1 or 2 depending on input
if file_var == "1":
    txtpath = os.path.join("." , "raw_data", "paragraph_1.txt")
elif file_var == "2":
    txtpath = os.path.join("." , "raw_data", "paragraph_2.txt")
else:
    print("Sorry! We don't have that!")
    exit()

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(txtpath, 'r') as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    paragraph = text.read()
    print("Here is the paragraph")
    print("---")
    # Print the contents of the text file
    print(paragraph)
    print("--------------------------------")

# Splits the paragraph based on spaces and calls them words.    
    words = paragraph.split()
    print("There are " + str(len(words)) + " words in this paragraph.")
    print("The first word is " + words[0])
    print("---------------------")

# Takes every character and declares them as a letter.
# But it counts a space as a word, so we subtract the number
# of words, then add one, since there one less space than word.
    for letter in paragraph:
        letters.append(letter)
    print("There are " + str(len(letters)-len(words)+1) + " letters in this paragraph.")
    print("The first letter is " + letters[0])
    print("---------------------------------")

# Separates the paragraph by periods.  The program will index the null set behind the last period, 
# so the number of sentences is subtracted by one.
    sentences = paragraph.split(sep = ".")
    print("There are " + str(len(sentences) - 1) + " sentences in this paragraph.")
    print("The first sentence is:  " + sentences[0] + ".")
    print("---------------------")
    
    word_per_sent = len(words)/(len(sentences)-1)
    print("The average words per sentence is: " + str(word_per_sent))
    lett_per_word = (len(letters)-len(words)+1)/len(words)
    print("The average letters per word is: " + str(lett_per_word))