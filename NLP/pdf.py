import PyPDF2

with open('sample.pdf',mode='rb') as myfile:
    pdf_reader = PyPDF2.PdfFileReader(myfile)
    print(pdf_reader.numPages)
    p = pdf_reader.getPage(0)
    text = p.extractText()
    print(text)
    
with open('sample.pdf', mode='rb') as myfile:
    pdf_reader = PyPDF2.PdfFileReader(myfile)
    p = pdf_reader.getPage(0)
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(p)
    with open('new_sample.pdf','wb') as output:
        pdf_writer.write(output)
        
with open('new_sample.pdf','rb') as new:
    read = PyPDF2.PdfFileReader(new)
    print(read.numPages)