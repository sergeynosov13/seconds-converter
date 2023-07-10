from termcolor import colored
from customtkinter import *

#Создание окна
window = CTk()
window.title("Seconds converter")
window.geometry("300x120")
set_default_color_theme("green")

#Функция конвертирования
def convert():
    secs = int(input_entry.get())
    converted = f"{secs//3600} hours {(secs % 3600) // 60} minutes {secs % 60} seconds"
    result_lbl.configure(text=converted)

#Объекты
input_entry = CTkEntry(window, placeholder_text="Введите кол-во сек.")
convert_btn = CTkButton(window, text="Convert!", command=convert)
result_lbl = CTkLabel(window, text="")

input_entry.pack()
convert_btn.pack(pady=10)
result_lbl.pack()

window.mainloop()