# version 0.1

import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger


def Upload_Action():
    Upload_Action.filepath = filedialog.askopenfilename(filetypes=[('PDF Documents', '*pdf')])
    print('Selected:', Upload_Action.filepath)


def Upload_Action2():
    Upload_Action2.filepath2 = filedialog.askopenfilename(filetypes=[('PDF Documents', '*pdf')])
    print('Selected:', Upload_Action2.filepath2)


def mergefile():
    merger = PdfFileMerger()
    f1 = open(Upload_Action.filepath, "rb")
    merger.append(f1)
    f2 = open(Upload_Action2.filepath2, "rb")
    merger.append(f2)
    mergefile.counter += 1  # counter for multiple files
    print(mergefile.counter)
    merger.write("mergedPdf %d.pdf" % (mergefile.counter))  # name of the output file
    print("Mergedpdf.pdf file created.")


mergefile.counter = 0

window = tk.Tk()
window.title('Merge PDF Files')
window.geometry('300x200')

button = tk.Button(window, text='Choose File 1', command=Upload_Action)
button.grid(row=0, column=0, padx=110, pady=20)

button2 = tk.Button(window, text='Choose File 2', command=Upload_Action2)
button2.grid(row=1, column=0, padx=110, pady=20)

button3 = tk.Button(window, text='Merge Files', command=mergefile)
button3.grid(row=2, column=0, padx=110, pady=20)

window.mainloop()
