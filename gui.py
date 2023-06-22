import tkinter as tk


def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Image Format Converter")

    # Set the window size
    window_height = 500
    window_width = 900

    # Get the screen size information
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the coordinates to approximately center the window
    x_coord = int((screen_width / 2) - (window_width / 2))
    y_coord = int((screen_height / 2) - 2 * (window_height / 3))

    # Set the window's geometry
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coord, y_coord))

    # Start the main event loop
    root.mainloop()

