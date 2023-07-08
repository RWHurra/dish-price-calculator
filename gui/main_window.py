import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from gui.dish_window import DishWindow  # Import the existing dish_window code
from gui.component_window import ComponentWindow  # Import the existing component_window code
from gui.help_window import HelpWindow  # Import the existing component_window code
from gui.vendor_window import VendorWindow  # Import the existing vendor_window code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setup_ui()
    
    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        
        # Create buttons to open windows
        recipe_button = QPushButton("➕ Manage Dishes")
        recipe_button.clicked.connect(self.open_dish_window)
        main_layout.addWidget(recipe_button)
        
        components_button = QPushButton("🔧 Manage Components")
        components_button.clicked.connect(self.open_components_window)
        main_layout.addWidget(components_button)
        
        vendor_button = QPushButton("🏬 Manage Vendors")
        vendor_button.clicked.connect(self.open_vendor_window)
        main_layout.addWidget(vendor_button)
        
        settings_button = QPushButton("⚙️ Settings")
        settings_button.clicked.connect(self.open_settings_window)
        main_layout.addWidget(settings_button)
        
        help_button = QPushButton("❓ Help")
        help_button.clicked.connect(self.open_help_window)
        main_layout.addWidget(help_button)
        
        self.setCentralWidget(main_widget)
    
    def open_dish_window(self):
        self.dish_window = DishWindow()
        self.dish_window.show()
    
    def open_components_window(self):
        self.component_window = ComponentWindow()
        self.component_window.show()
    
    def open_vendor_window(self):
        self.vendor_window = VendorWindow()
        self.vendor_window.show()
    
    def open_settings_window(self):
        # self.settings_window = SettingsWindow()
        # self.settings_window.show()
        # Implement opening of settings window
        pass
    
    def open_help_window(self):
        self.help_window = HelpWindow()
        self.help_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
