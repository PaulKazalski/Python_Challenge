# Store the file path associated with the file (note the backslash may be OS specific)

file1 = "C:/Users/paulk/Documents/python-challenge/pyParagraph/raw_data/paragraph_1.txt"
paragraph = " "
letters = []
words = []
sentences = []

file_var = input("What paragraph do you want? 1 or 2?")

if file_var == "1":
    file1 = "C:/Users/paulk/Documents/python-challenge/pyParagraph/raw_data/paragraph_1.txt"
elif file_var == "2":
    file1 = "C:/Users/paulk/Documents/python-challenge/pyParagraph/raw_data/paragraph_2.txt"
else:
    print("Sorry! We don't have that!")
    exit()

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file1, 'r') as text:

    # This stores a reference to a file stream
    print(text)

    # Store all of the text inside a variable called "lines"
    paragraph = text.read()
    print("---")
    # Print the contents of the text file
    print(paragraph)
    print("---")

    for letter in paragraph:
        letters.append(letter)
    print(letters[0])
    print(letters[1])
    print(len(letters))

    words = paragraph.split()
    print(words[0])
    print(words[1])
    print(len(words))
    print("---------------------")

    sentences = paragraph.split(sep = ".")
    print(sentences[0] + ".")
    print(len(sentences))
    print("---------------------")
    # Comments on execution
    # 1. there's some funkiness going on in front of the word "promoter", near the end of Paragraph 1.
