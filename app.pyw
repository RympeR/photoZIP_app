from tkinter import ttk
from tkinter import Tk, simpledialog, filedialog, Frame, Button, Label, messagebox, StringVar
from photoManager import PhotoManager

PATH = ''
ZIP_FILE_PATH = ''

def ShowDialogs():
    global ZIP_FILE_PATH
    ret = filedialog.askopenfilename()
    text.set(ret)
    ZIP_FILE_PATH = ret

def get_path():
    global PATH
    path = filedialog.askdirectory()
    PATH = path
    path_.set(path)

def run():
    if PATH != '' and ZIP_FILE_PATH != '':
        PHOTO_MANAGER = PhotoManager(ZIP_FILE_PATH, PATH)
        PHOTO_MANAGER.run()
    else:
        ret = messagebox.showerror("Пустой путь или файл", "Не выбрали файл\nили не заполнили путь")

window=Tk()
window.title('Photo Manager')
main_frame = Frame(window)
main_frame.pack(fill="both", expand=True)
text = StringVar()
text.set("")
label = Label(main_frame, textvariable=text)
label.grid(row=0,padx=10, column=0)
path_ = StringVar()
path_.set("")
label = Label(main_frame, textvariable=path_)
label.grid(row=0,padx=10, column=1)
button_choose=Button(main_frame,text="Выбрать архив",padx=10,pady=10,bg="#C0392B",fg="white",command=ShowDialogs)
button_choose.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)
button_path_input=Button(main_frame,text="Ввести путь",padx=10,pady=10,bg="#C0392B",fg="white",command=get_path)
button_path_input.grid(row=1,column=1,sticky="nsew",padx=10,pady=10)
button_start=Button(main_frame,text="Запуск",padx=10,pady=10,bg="#C0392B",fg="white",command=run)
button_start.grid(row=2,column=0,sticky="nsew",padx=10,pady=10)

window.mainloop()
