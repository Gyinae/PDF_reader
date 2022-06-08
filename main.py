import pyttsx3
import PyPDF2

# Select the directory of the book
book = open("oop.pdf", "rb")

# Initialize the Python reader and check the number of pages in the book
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)

# Initialize the voice command for the Python reader
speaker = pyttsx3.init()

# Enquiry about the page number to be read out
number  = int(input("Enter a page number: \n")) - 1

# Create a for loop to loop through the pages and commence reading
for num in range(number, pages):
    page = pdfreader.getPage(number)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()