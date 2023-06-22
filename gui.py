import tkinter as tk
from tkinter import filedialog


class GUIWindow:

    """
    A class representing the main GUI window for the Image Format Converter.

    Attributes:
        _root (Tk): The main Tkinter window.
        _FORMATS (list): A list of supported image formats.
        _format_from (StringVar): The selected format to convert from.
        _format_to (StringVar): The selected format to convert to.
    """

    def __init__(self):

        """
        Initialize the GUIWindow class and create the main window.
        """

        # Create the main window
        self._root = tk.Tk()

        # Set up format list
        self._FORMATS = ["HEIC", "JPEG", "JPG", "PNG"]

        # Set title
        self._root.title("Image Format Converter")

        # Set the window's geometry
        self._set_window_geometry()

        # Set up frames
        self._create_frames()

        # Start the main event loop
        self._root.mainloop()

    def _set_window_geometry(self):
        """
        Set the geometry of the main window to be approximately centered
        based on screen size.
        The window size is set to a standard of 900x500 pixels.
        It is resizable.
        """
        # Set the window size
        _window_height = 500
        _window_width = 900

        # Get the screen size information
        _screen_width = self._root.winfo_screenwidth()
        _screen_height = self._root.winfo_screenheight()

        # Calculate the coordinates to approximately center the window
        _x_coord = int((_screen_width / 2) - (_window_width / 2))
        _y_coord = int((_screen_height / 2) - 2 * (_window_height / 3))

        self._root.geometry("{}x{}+{}+{}".format(_window_width, _window_height, _x_coord, _y_coord))

    @staticmethod
    def button_click():
        # Open the file dialog
        file_path = filedialog.askopenfilename()

    def _create_frames(self):
        """
        Create left and right frames and setup dropdown menus.
        """
        # Create left and right frames
        _left_frame = tk.Frame(self._root)
        _left_frame.pack(side="left", expand=True, fill="both")
        _right_frame = tk.Frame(self._root)
        _right_frame.pack(side="right", expand=True, fill="both")

        # Set up dropdown data
        self._format_from = tk.StringVar()
        self._format_to = tk.StringVar()

        # Set arbitrary initial values
        self._format_from.set("HEIC")
        self._format_to.set("JPG")

        # Create Dropdown menus
        _drop_from = tk.OptionMenu(_left_frame, self._format_from, *self._FORMATS)
        _button = tk.Button(_left_frame, text="Click Me", command=self.button_click)
        _button.place(relx=0.5, rely=0.5, anchor="center")
        _drop_from.place(relx=0.5, rely=0.5, anchor="center")
        _drop_to = tk.OptionMenu(_right_frame, self._format_to, *self._FORMATS)
        _drop_to.place(relx=0.5, rely=0.5, anchor="center")
