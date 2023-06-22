import tkinter as tk


class GUIWindow:

    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Image Format Converter")

        # Unpack window geometry variables
        window_width, window_height, x_coord, y_coord = self._get_window_geometry()

        # Set the window's geometry
        self.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coord, y_coord))

        self._create_frames()

        # Start the main event loop
        self.root.mainloop()

    def _get_window_geometry(self):
        # Set the window size
        window_height = 500
        window_width = 900

        # Get the screen size information
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the coordinates to approximately center the window
        x_coord = int((screen_width / 2) - (window_width / 2))
        y_coord = int((screen_height / 2) - 2 * (window_height / 3))

        return [window_width, window_height, x_coord, y_coord]

    def _create_frames(self):
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
        drop_from.place(relx=0.5, rely=0.5, anchor="center")
        drop_to = tk.OptionMenu(right_frame, self.format_to, *self.formats)
        drop_to.place(relx=0.5, rely=0.5, anchor="center")


