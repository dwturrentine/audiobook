import PyPDF2
import pyttsx3

language = 'en'  # Set language to English
book = open('', 'rb')  # Set PDF path with file name 'file.pdf'
pdfReader = PyPDF2.PdfFileReader(book)

speaker = pyttsx3.init()  # Creates object
for num in range(pdfReader.numPages):  # Loop to extract pages in pdf
    text = pdfReader.getPage(num).extractText()
    print(text)  # Print extracted text
    speaker.say(text)

speaker.runAndWait()
speaker.stop()
speaker.save_to_file('', '.mp3')  # Save voice to file
print("Done.")
