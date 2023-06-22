import tkinter as tk
from tkinter import filedialog


class GUIWindow:

    """
    A class representing the main GUI window for the Image Format Converter.

    Attributes:
        root (Tk): The main Tkinter window.
        formats (list): A list of supported image formats.
        format_from (StringVar): The selected format to convert from.
        format_to (StringVar): The selected format to convert to.
    """

    def __init__(self):

        """
        Initialize the GUIWindow class and create the main window.
        """

        # Create the main window
        self.root = tk.Tk()
        # Set title
        self.root.title("Image Format Converter")

        # Set the window's geometry
        self._set_window_geometry()

        # Set up frames
        self._create_frames()

        # Start the main event loop
        self.root.mainloop()

    def _set_window_geometry(self):
        """
        Set the geometry of the main window to be approximately centered
        based on screen size.
        The window size is set to a standard of 900x500 pixels.
        It is resizable.
        """
        # Set the window size
        window_height = 500
        window_width = 900

        # Get the screen size information
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the coordinates to approximately center the window
        x_coord = int((screen_width / 2) - (window_width / 2))
        y_coord = int((screen_height / 2) - 2 * (window_height / 3))

        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coord, y_coord))

    @staticmethod
    def button_click():
        print("Button clicked!")
        # Open the file dialog
        file_path = filedialog.askopenfilename()

    def _create_frames(self):
        """
        Create left and right frames and setup dropdown menus.
        """
        # Create left and right frames
        left_frame = tk.Frame(self.root)
        left_frame.pack(side="left", expand=True, fill="both")
        right_frame = tk.Frame(self.root)
        right_frame.pack(side="right", expand=True, fill="both")

        # Set up data and variables for dropdowns
        self.formats = ["HEIC", "JPEG", "JPG", "PNG"]
        self.format_from = tk.StringVar()
        self.format_to = tk.StringVar()

        # Set arbitrary initial values
        self.format_from.set("HEIC")
        self.format_to.set("JPG")

        # Create Dropdown menus
        drop_from = tk.OptionMenu(left_frame, self.format_from, *self.formats)
        button = tk.Button(left_frame, text="Click Me", command=self.button_click)
        button.place(relx=0.5, rely=0.5, anchor="center")
        drop_from.place(relx=0.5, rely=0.5, anchor="center")
        drop_to = tk.OptionMenu(right_frame, self.format_to, *self.formats)
        drop_to.place(relx=0.5, rely=0.5, anchor="center")

