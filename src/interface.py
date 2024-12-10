import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer

class App(QWidget):
    """
    A PyQt5 application window that displays a folder selection dialog, 
    requests confirmation, and automatically closes after the user confirms 
    or cancels the operation.
    """
    def __init__(self):
        """
        Initializes the App window, sets up its title and geometry, 
        opens the folder selection dialog, and processes the confirmation.
        """
        super().__init__()
        self.setWindowTitle("Select folder")
        self.setGeometry(300, 300, 400, 200)
        self.folder_path = self.select_and_confirm_folder()
        QTimer.singleShot(0, self.close)

    def select_and_confirm_folder(self) -> str:
        """
        Opens a folder selection dialog, asks the user for confirmation, 
        and retrieves the selected folder's path if confirmed.

        Returns:
            str: The path of the selected folder if confirmed, or an empty 
            string if no folder was selected or the user canceled.
        """
        folder_path = QFileDialog.getExistingDirectory(self, "Select folder")
        if not folder_path:
            return ""

        # Show a confirmation dialog
        confirm = QMessageBox.question(
            self,
            "Confirm Folder",
            f"Has seleccionado la carpeta:\n{folder_path}\n\n¿Deseas continuar?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            return folder_path
        else:
            return ""

def get_folder_path() -> str:
    """
    Launches the folder selection dialog and returns the selected folder path 
    after user confirmation.

    If no QApplication instance is running, it creates one, initializes the App 
    class to show the dialog, and starts the event loop. After the user 
    interacts with the dialog, the selected folder path is retrieved.

    Returns:
        str: The path of the selected folder if confirmed, or an empty string 
        if no folder was selected or the user canceled.
    """
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    window = App()
    app.exec_()
    
    return window.folder_path
