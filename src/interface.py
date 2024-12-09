import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import QTimer

"""
This script provides a PyQt5-based implementation for selecting a folder. It 
displays a folder selection dialog and retrieves the chosen folder path. The 
dialog is implemented in a minimal window that automatically closes after 
the selection is made.
"""

class App(QWidget):
    """
    A PyQt5 application window that displays a folder selection dialog 
    and automatically closes after the user selects a folder or cancels 
    the operation.
    """
    def __init__(self):
        """
        Initializes the App window, sets up its title and geometry, 
        opens the folder selection dialog, and closes the window immediately 
        after interaction.
        """
        super().__init__()
        self.setWindowTitle("Select folder")
        self.setGeometry(300, 300, 400, 200)
        self.folder_path = self.select_folder()
        QTimer.singleShot(0, self.close)

    def select_folder(self) -> str:
        """
        Opens a folder selection dialog and retrieves the selected folder's path.

        Returns:
            str: The path of the selected folder, or an empty string if no 
            folder was selected.
        """
        folder_path = QFileDialog.getExistingDirectory(self, "Select folder")
        
        return folder_path if folder_path else ""

def get_folder_path() -> str:
    """
    Launches the folder selection dialog and returns the selected folder path.

    If no QApplication instance is running, it creates one, initializes the App 
    class to show the dialog, and starts the event loop. After the user 
    interacts with the dialog, the selected folder path is retrieved.

    Returns:
        str: The path of the selected folder, or an empty string if no folder 
        was selected.
    """
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    window = App()
    app.exec_()
    
    return window.folder_path
