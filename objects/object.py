from PyQt6.QtWidgets import QMessageBox

class Object():
    def open_error_window(self, error_message):
        QMessageBox.warning(self, "Error", error_message)