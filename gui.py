import tkinter as tk
from tkinter import filedialog

import tkinter as tk
import tkinter.font as tkFont


class GUIWindow:

    """
    A class representing the main GUI window for the Image Format Converter.

    Attributes:
        _root (Tk): The main Tkinter window.
        _FORMATS (list): A list of supported image formats.
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

        self._upload_path = None
        self._output_path = None

        # Set title
        self._root.title("Image Format Converter")

        # Set the window's geometry
        self._set_window_geometry()

        # Set up frames
        self._add_widgets()

        self.image_to_convert = None

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
        _window_height = 522
        _window_width = 637

        # Get the screen size information
        _screen_width = self._root.winfo_screenwidth()
        _screen_height = self._root.winfo_screenheight()

        # Calculate the coordinates to approximately center the window
        _x_coord = int((_screen_width / 2) - (_window_width / 2))
        _y_coord = int((_screen_height / 2) - 2 * (_window_height / 3))

        self._root.geometry("{}x{}+{}+{}".format(_window_width, _window_height, _x_coord, _y_coord))

    def upload_image(self):
        # Open the file dialog
        self._upload_path = filedialog.askopenfilename(filetypes=[('JPEG File', '*.jpeg'), ('HEIC File', '*.heic')])

    def converted_image_path(self):
        # Open the file dialog
        self._output_path = filedialog.askdirectory(title='Choose', mustexist=True)

    def _add_widgets(self):
        """
        Add the widgets to the window.
        """
        # Set up dropdown data
        self._format_to = tk.StringVar()

        # Set arbitrary initial values
        self._format_to.set("JPG")

        ft = tkFont.Font(size=12)
        upload_button = tk.Button(self._root,
                                  bg="#c71585",
                                  fg="#ffffff",
                                  font=ft,
                                  justify="center",
                                  text="Upload Image",
                                  relief="flat",
                                  command=self.upload_image)
        upload_button.place(x=100, y=200, width=106, height=47)

        ft = tkFont.Font(family='Times', size=10)
        format_dropdown = tk.OptionMenu(self._root, self._format_to, *self._FORMATS)
        format_dropdown.configure(font=ft,
                                  justify="center",
                                  text="Choose")
        format_dropdown.place(x=430, y=160, width=60, height=31)

        convert_button = tk.Button(self._root,
                                   bg="#6ca26c",
                                   fg="#ffffff",
                                   font=ft,
                                   justify="center",
                                   text="Convert",
                                   relief="flat",
                                   command=self.upload_image)
        convert_button.place(x=250, y=400, width=133, height=44)

        output_path_button = tk.Button(self._root,
                                       bg="#98bcbc",
                                       fg="#ffffff",
                                       font=ft,
                                       justify="center",
                                       text="Save here",
                                       command=self.converted_image_path)
        output_path_button.place(x=410, y=250, width=111, height=30)

        format_label = tk.Label(self._root)
        ft = tkFont.Font(family='Times', size=9)
        format_label["font"] = ft
        format_label["fg"] = "#333333"
        format_label["justify"] = "center"
        format_label["text"] = "Which format do you want to convert to?"
        format_label.place(x=410, y=120, width=139, height=30)

        output_path_label = tk.Label(self._root)
        ft = tkFont.Font(family='Times', size=9)
        output_path_label["font"] = ft
        output_path_label["fg"] = "#333333"
        output_path_label["justify"] = "center"
        output_path_label["text"] = "Where do you want to save the converted image?"
        output_path_label.place(x=410, y=210, width=143, height=30)
