import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from gui.recipe_window import RecipeWindow  # Import the existing recipe_window code

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
        recipe_button = QPushButton("➕ Manage Recipes")
        recipe_button.clicked.connect(self.open_recipe_window)
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
    
    def open_recipe_window(self):
        self.recipe_window = RecipeWindow()
        self.recipe_window.show()
    
    def open_components_window(self):
        # Implement opening of components window
        pass
    
    def open_vendor_window(self):
        # Implement opening of vendor window
        pass
    
    def open_settings_window(self):
        # Implement opening of settings window
        pass
    
    def open_help_window(self):
        # Implement opening of help window
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
