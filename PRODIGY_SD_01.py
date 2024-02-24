import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        original_unit = combo_original_unit.get()

        if original_unit == "Celsius":
            fahrenheit = (temperature * 9/5) + 32
            kelvin = temperature + 273.16
            result_text = f"Fahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K"
        elif original_unit == "Fahrenheit":
            celsius = (temperature - 32) * 5/9
            kelvin = (temperature - 32) * 5/9 + 273.16
            result_text = f"Celsius: {celsius:.2f} °C\nKelvin: {kelvin:.2f} K"
        elif original_unit == "Kelvin":
            celsius = temperature - 273.16
            fahrenheit = (temperature - 273.16) * 9/5 + 32
            result_text = f"Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F"

        lbl_result.config(text=result_text)

    except ValueError:
        lbl_result.config(text="Invalid input. Please enter a valid temperature.")

#creating the main window
root = tk.Tk()
root.title("Temperature Converter")

#creating the input widgets
lbl_temperature = tk.Label(root, text="Enter Temperature:")
lbl_temperature.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_temperature = tk.Entry(root)
entry_temperature.grid(row=0, column=1, padx=10, pady=10)

lbl_original_unit = tk.Label(root, text="Select Original Unit:")
lbl_original_unit.grid(row=1, column=0, padx=10, pady=10, sticky="e")

units = ["Celsius", "Fahrenheit", "Kelvin"]
combo_original_unit = ttk.Combobox(root, values=units)
combo_original_unit.set("Celsius")
combo_original_unit.grid(row=1, column=1, padx=10, pady=10)

#creating the conversion button
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.grid(row=2, column=0, columnspan=2, pady=10)

#creating the result label
lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0, columnspan=2, pady=10)

#back to main
root.mainloop()
