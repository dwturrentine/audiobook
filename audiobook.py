import pdfplumber
from gtts import gTTS

language = 'en' # Set language to English
pdf_path = "MaRainey.pdf"  # Set path of pdf to convert

pdf = pdfplumber.open(pdf_path)
page = pdf.pages[0]
text = page.extract_text()
for i in range(len(pdf.pages)):
    new_text = pdf.pages[i].extract_text()
    print(new_text)
    pdf.close()



gTTS_transformer = gTTS(text=new_text, lang=language)
gTTS_transformer.save("test1.mp3")  # Set name with mp3 extension
print("Done.")
