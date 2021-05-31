import tkinter as tk
from compressmodule import compress,decompress

def compression(i,o):
    compress(i,o)

def decompression(i,o):
    decompress(i,o)

window = tk.Tk()

window.title("Compression Engine")
window.geometry("600x400")

title = tk.Label(window,text="Compress Files")
title.grid(row=0,column=1)

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window,text="File To Be Compressed")
input_label.grid(row=1,column=0)
input_entry.grid(row=1,column=1)

output_label = tk.Label(window,text="Name of Compressed File")
output_label.grid(row=2,column=0)
output_entry.grid(row=2,column=1)

compression_bttn = tk.Button(window,text="Compress",command=lambda:compression(input_entry.get(),output_entry.get()))
compression_bttn.grid(row=3,column=1)

label = tk.Label(window,text="")
label.grid(row=4)

title = tk.Label(window,text="Decompress Files")
title.grid(row=5,column=1)

input_entryd = tk.Entry(window)
output_entryd = tk.Entry(window)

input_labeld = tk.Label(window,text="File To Be Deompressed")
input_labeld.grid(row=6,column=0)
input_entryd.grid(row=6,column=1)

output_labeld = tk.Label(window,text="Name of Decompressed File")
output_labeld.grid(row=7,column=0)
output_entryd.grid(row=7,column=1)

decompression_bttn = tk.Button(window,text="Decompress",command=lambda:decompression(input_entryd.get(),output_entryd.get()))
decompression_bttn.grid(row=8,column=1)

window.mainloop()

