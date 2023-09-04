#Importamos la libreria de word a pdf
from docx2pdf import convert

#Importamos la libreria de pdf a word
from pdf2docx import Converter


select = int(input("1. Convertor de word a pdf | 2.Convertor de pdf a word "))

#Opcion de convertir word a pdf
if select == 1:
    
    nombre = input("Ingrese el nombre del documento")
    
    #Direccion del documento
    convert("PLANTILLA.docx", nombre +".pdf")


#Opcion de convertir pdf a word
elif select == 2:

    #Direccion del archivo
    pdf_file = 'PLANTILLAs.pdf'
    
    nombre = input("Ingrese el nombre del archivo ")

    #Salida del archivo
    docx_file = nombre + '.docx'

    # Convertor de pdf a word
    cv = Converter(pdf_file)
    cv.convert(docx_file)      # all pages by default
    cv.close()

else:
    print("Error...")