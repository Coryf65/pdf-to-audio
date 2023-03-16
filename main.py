import pyttsx3, PyPDF2

# Creating a PDF to TTS converter
pdf_filename = 'sample.pdf'
clean_text = ''

# open the pdf
pdf_reader = PyPDF2.PdfReader(open(pdf_filename, 'rb'))

speaker = pyttsx3.init()

for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()