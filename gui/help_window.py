import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Help")
        self.setup_ui()

    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Create labels for button descriptions
        recipe_label = QLabel("➕ <b>Manage Dishes</b>: "
                              + "Opens the dishes window to view and add a new dish.")
        component_label = QLabel("🔧 <b>Manage Components</b>: "
                                 + "Opens the component window to view and add a new component.")
        vendor_label = QLabel("🏬 <b>Manage Vendors</b>: "
                              + "Opens the vendor window to view and add a new vendor.")
        settings_label = QLabel("⚙️ <b>Settings</b>: "
                                + "Opens the settings window to configure application settings.")
        help_label = QLabel("❓ <b>Help</b>: "
                            + "Opens the help window to get assistance ☝️")

        # Add labels to the layout
        main_layout.addWidget(recipe_label)
        main_layout.addWidget(component_label)
        main_layout.addWidget(vendor_label)
        main_layout.addWidget(settings_label)
        main_layout.addWidget(help_label)

        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())
