import tkinter as tk
from tkinter import ttk

def sortowanie_babelkowe(liczby, n):
    for i in range(n):
        for j in range(1, n - i):
            if liczby[j - 1] > liczby[j]:
                liczby[j - 1], liczby[j] = liczby[j], liczby[j - 1]

def sortuj_button_click():
    try:
        liczby = [int(x) for x in liczby_entry.get().split()]
        n = len(liczby)
        sortowanie_babelkowe(liczby, n)
        wynik_label.config(text="Posortowane liczby: " + ", ".join(map(str, liczby)))
    except ValueError:
        wynik_label.config(text="Liczby mają być oddzielone spacją.")

okno = tk.Tk()
okno.title("Sortowanie Bąbelkowe")
okno.geometry("400x200")  

background_color = "#34ebb4"
button_color = "#4CAF50"
label_color = "#333333"

okno.configure(background=background_color)

style = ttk.Style()
style.configure("TButton", font=("Arial", 14), background=button_color)
style.configure("TLabel", font=("Arial", 14), background=background_color, foreground=label_color)

liczby_label = ttk.Label(okno, text="Wprowadź liczby oddzielone spacją:")
liczby_entry = ttk.Entry(okno)
sortuj_button = ttk.Button(okno, text="Sortuj", command=sortuj_button_click)
wynik_label = ttk.Label(okno, text="")

liczby_label.pack(pady=10)
liczby_entry.pack(pady=5)
sortuj_button.pack(pady=10)
wynik_label.pack()

okno.mainloop()
