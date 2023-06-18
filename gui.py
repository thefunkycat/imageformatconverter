import tkinter as tk

def on_option_selected(selected_option):
    print("Selected option:", selected_option)


def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Image Format Converter")

    input_format = tk.StringVar(window)

    # Set the initial value for the dropdown
    input_format.set("None")

    dropdown_frame = tk.Frame(window)
    dropdown_frame.pack(pady=10, side=tk.LEFT)
    # Create the OptionMenu widget
    dropdown = tk.OptionMenu(dropdown_frame, input_format, "HEIC", "JPEG", "PNG")
    dropdown.pack()

    # Create a button to print the selected option
    button = tk.Button(window, text="Print Selection", command=lambda: on_option_selected(input_format.get()))
    button.pack()

    # Start the GUI event loop
    window.mainloop()
