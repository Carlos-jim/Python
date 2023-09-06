# Importamos las librerias necesarias
from pytube import YouTube
from tkinter import *
from tkinter import messagebox as Messagebox
from tkinter import ttk

# Funcion para descargar el video
def ytdownload(resolution):
    value = resolution.get()
    enlace = videos.get()
    video = YouTube(enlace, on_progress_callback=progress_function)
    descargar = video.streams.filter(res=value+"p").first()
    descargar.download()

# Funcion de la barra de progreso    
def progress_function(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (float(abs(bytes_remaining-size)/size))*float(100)
    bar['value'] = progress
    root.update_idletasks()

def popup():
    Messagebox.showinfo("Sobre mi", "Github: ")

root = Tk()
root.config(bd=15, bg='light blue')
root.title("Youtube Download")

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Informacion", menu=helpmenu)
helpmenu.add_command(label="Autor", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

label_title = Label(root, text="Youtube Download\n", font=("Helvetica", 16), bg='light blue')
label_title.grid(row=0, column=1, pady=10)

videos = Entry(root)
videos.grid(row=1, column=1)

btn_360p= StringVar(value="360")
btn_480p= StringVar(value="480")
btn_720p= StringVar(value="720")
btn_1080p= StringVar(value="1080")

button1 = Button(root, text="Download 360p", bg='green', fg='white',  command=lambda: ytdownload(btn_360p) )
button2 = Button(root, text="Download 480p", bg='green', fg='white', command=lambda:ytdownload(btn_480p))
button3 = Button(root, text="Download 720p",  bg='green', fg='white', command=lambda:ytdownload(btn_720p))
button4 = Button(root, text="Download 1080p",  bg='green', fg='white', command=lambda:ytdownload(btn_1080p))

button1.grid(row=3, column=1) #Btn 360p
button2.grid(row=3, column=2) #Btn 480p
button3.grid(row=3, column=3) #Btn 720p
button4.grid(row=3, column=4) #Btn 1080p

bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
bar.grid(row=4, columnspan=4)

root.grid_columnconfigure(0, minsize=10)
root.grid_columnconfigure(5, minsize=10)

root.mainloop()

