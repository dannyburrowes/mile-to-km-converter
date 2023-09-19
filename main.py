from tkinter import *

def calculate_km():
    miles = float(input.get())
    km = round(miles * 1.609344, 5)
    output_label.config(text=km)

#Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=280, height=150)
window.config(padx=20, pady=20)

#Labels
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to", font=("Arial", 12))
equal_to_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

output_label = Label(text="0", font=("Arial", 12))
output_label.grid(column=1, row=1)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

#Calculate Button
calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)

window.mainloop()