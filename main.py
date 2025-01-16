from pdf2docx import Converter

pdf_file = 'sample.pdf'
out_file = 'sample.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(out_file)      # all pages by default
cv.close()