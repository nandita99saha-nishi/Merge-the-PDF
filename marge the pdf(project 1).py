from PyPDF2 import PdfMerger

ALLPDF = ["pdf 1.pdf", "pdf 2.pdf"]


OurMerger = PdfMerger()


for NewPDF in ALLPDF:
    OurMerger.append(NewPDF)

OurMerger.write("creature.pdf")
OurMerger.close()































