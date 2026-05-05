from PyPDF2 import PdfReader

reader = PdfReader("pdfs/339741.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)


import re
matches = re.findall(r'\bH.{3}\b', text)
print(matches)