# Importamos la libreria pytube
from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox
from tkinter import ttk

def ytdownload():
    # Obtenemos el enlace del video y lo asignamos a una variable
    enlace = videos.get()
    video = YouTube(enlace, on_progress_callback=progress_function)
    
    # Guardamos el video en la variable descarga en maxima resolucion
    descargar = video.streams.filter(res="720p").first()
    
    # Se descarga el video
    descargar.download()
    
def progress_function(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (float(abs(bytes_remaining-size)/size))*float(100)
    bar['value'] = progress
    root.update_idletasks()

def popup():
    # Mensaje del menu de Sobre mi
    Messagebox.showinfo("Sobre mi", "Github: ")

root = Tk()
root.config(bd=15, bg='light blue')

# Titulo del programa
root.title("Youtube Download")

# Creamos un menu
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

# Menu de informacion en cascada
menubar.add_cascade(label="Informacion", menu=helpmenu)

# Submenu donde llamamos a la funcion popup
helpmenu.add_command(label="Autor", command=popup)

# Menu para salir
menubar.add_command(label="Salir", command=root.destroy)

# Crear una etiqueta con el título del programa
label_title = Label(root, text="Youtube Download\n", font=("Helvetica", 16), bg='light blue')
label_title.grid(row=0, column=1, pady=10)

# Donde recibimos el enlace del video
videos = Entry(root)
videos.grid(row=1, column=1)

# Boton a descargar que llama a la funcion ytdownload
btn = Button(root, text="Download", command=ytdownload, bg='green', fg='white')
btn.grid(row=2, column=1)

bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
bar.grid(row=3, column=1)

root.mainloop()
