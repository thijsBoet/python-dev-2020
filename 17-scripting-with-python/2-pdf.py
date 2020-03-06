import PyPDF4
import sys

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF4.PdfFileReader(file)
    print(reader.numPages)

    page = reader.getPage(0)
    page.rotateClockwise(180)
    writer = PyPDF4.PdfFileWriter()
    writer.addPage(page)
    with open('tilted_dummy.pdf', 'wb') as new_file:
        writer.write(new_file)

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF4.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('combined.pdf')

pdf_combiner(inputs)

def watermark_pdf():
    template = PyPDF4.PdfFileReader(open('dummy.pdf', 'rb'))
    watermark = PyPDF4.PdfFileReader(open('wtr.pdf', 'rb'))
    output = PyPDF4.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)

watermark_pdf()