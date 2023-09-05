# Importar los módulos necesarios
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from docx2pdf import convert
from pdf2docx import Converter

# Definir una función para convertir de Word a PDF
def word_to_pdf():
    # Mostrar un diálogo para elegir un archivo de Word
    source = fd.askopenfilename(
        title="Selecciona un archivo de Word",
        filetypes=[("Archivos de Word", "*.docx")]
    )
    # Si se ha seleccionado un archivo
    if source:
        # Mostrar un diálogo para elegir el nombre y la ruta del archivo de destino
        destination = fd.asksaveasfilename(
            title="Guarda el archivo PDF",
            filetypes=[("Archivos PDF", "*.pdf")],
            defaultextension=".pdf"
        )
        # Si se ha introducido un nombre y una ruta válidos
        if destination:
            # Intentar hacer la conversión usando la librería docx2pdf
            try:
                convert(source, destination)
                # Mostrar un mensaje de éxito
                label_message.config(text="Conversión exitosa de Word a PDF")
            # Si ocurre algún error, mostrar un mensaje de error
            except Exception as e:
                label_message.config(text="Error al convertir de Word a PDF")
                messagebox.showerror("Error", str(e))

# Definir una función para convertir de PDF a Word
def pdf_to_word():
    # Mostrar un diálogo para elegir un archivo PDF
    source = fd.askopenfilename(
        title="Selecciona un archivo PDF",
        filetypes=[("Archivos PDF", "*.pdf")]
    )
    # Si se ha seleccionado un archivo
    if source:
        # Mostrar un diálogo para elegir el nombre y la ruta del archivo de destino
        destination = fd.asksaveasfilename(
            title="Guarda el archivo Word",
            filetypes=[("Archivos de Word", "*.docx")],
            defaultextension=".docx"
        )
        # Si se ha introducido un nombre y una ruta válidos
        if destination:
            # Intentar hacer la conversión usando la librería pdf2docx
            try:
                cv = Converter(source)
                cv.convert(destination)
                cv.close()
                # Mostrar un mensaje de éxito
                label_message.config(text="Conversión exitosa de PDF a Word")
            # Si ocurre algún error, mostrar un mensaje de error
            except Exception as e:
                label_message.config(text="Error al convertir de PDF a Word")
                messagebox.showerror("Error", str(e))

# Crear una instancia de la clase Tk, que representa la ventana principal
root = tk.Tk()

# Crear una etiqueta con el título del programa
label_title = tk.Label(root, text="Convertidor de documentos", font=("Arial", 20))
label_title.pack(pady=10)

# Crear un botón para la opción de convertir de Word a PDF y asignarle la función correspondiente
button_word_to_pdf = tk.Button(root, text="Convertir de Word a PDF", command=word_to_pdf)
button_word_to_pdf.pack(pady=10)

# Crear un botón para la opción de convertir de PDF a Word y asignarle la función correspondiente
button_pdf_to_word = tk.Button(root, text="Convertir de PDF a Word", command=pdf_to_word)
button_pdf_to_word.pack(pady=10)

# Crear una etiqueta para mostrar el mensaje del estado de la conversión o posibles errores
label_message = tk.Label(root, text="")
label_message.pack(pady=10)

# Iniciar el bucle principal de la ventana, que espera los eventos del usuario
root.mainloop()
