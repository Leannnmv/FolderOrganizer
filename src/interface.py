import tkinter as tk
from tkinter import filedialog, messagebox

class App:
    """
    A Tkinter application window that displays a folder selection dialog,
    requests confirmation, and processes the user's response.
    """
    def __init__(self):
        """
        Initializes the App window, opens the folder selection dialog,
        and processes the confirmation.
        """
        self.root = tk.Tk()
        self.root.withdraw()
        self.folder_path = self.select_and_confirm_folder()
        self.root.quit()

    def select_and_confirm_folder(self) -> str:
        """
        Opens a folder selection dialog, asks the user for confirmation,
        and retrieves the selected folder's path if confirmed.

        Returns:
            str: The path of the selected folder if confirmed, or an empty 
            string if no folder was selected or the user canceled.
        """
        folder_path = filedialog.askdirectory(title="Select folder")
        if not folder_path:
            return ""

        # Show a confirmation dialog
        confirm = messagebox.askyesno(
            "Confirm Folder",
            f"Has seleccionado la carpeta:\n{folder_path}\n\n¿Deseas continuar?"
        )

        if confirm:
            return folder_path
        else:
            return ""

def get_folder_path() -> str:
    """
    Launches the folder selection dialog and returns the selected folder path 
    after user confirmation.

    Returns:
        str: The path of the selected folder if confirmed, or an empty string 
        if no folder was selected or the user canceled.
    """
    app = App()
    return app.folder_path
