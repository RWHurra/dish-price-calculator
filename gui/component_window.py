import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QComboBox
from objects.component import Component
from objects.vendor import Vendor

class ComponentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Component Manager")
        self.setup_ui()
        
        # Initialize Component class
        self.component_instance = Component()

        # Initialize component data
        self.components = []
        self.load_components()  # Load existing components from JSON or dictionary
        
        # Populate table with components
        self.populate_table()
    
    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Initialize Vendor class
        vendor_instance = Vendor()
        
        # Create table widget for displaying components
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Price", "Unit", "Vendor"])
        main_layout.addWidget(self.table_widget)
        
        # Create widget for adding a new component
        add_widget = QWidget()
        add_layout = QVBoxLayout()
        add_widget.setLayout(add_layout)
        
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        add_layout.addWidget(name_label)
        add_layout.addWidget(self.name_input)
        
        price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        add_layout.addWidget(price_label)
        add_layout.addWidget(self.price_input)
        
        unit_label = QLabel("Unit:")
        self.unit_input = QLineEdit()
        add_layout.addWidget(unit_label)
        add_layout.addWidget(self.unit_input)
        
        vendor_label = QLabel("Vendor:")
        self.vendor_combo = QComboBox()
        try:
            self.vendor_combo.addItems(vendor_instance.load_vendors())
        except:
            self.vendor_combo.addItems(["No vendors found"])
        add_layout.addWidget(vendor_label)
        add_layout.addWidget(self.vendor_combo)
        
        save_button = QPushButton("💾 Save Component")
        save_button.clicked.connect(self.add_component)  # Change to add_component()
        add_layout.addWidget(save_button)
        
        main_layout.addWidget(add_widget)
        
        self.setCentralWidget(main_widget)
    
    def populate_table(self):
        self.table_widget.setRowCount(len(self.components))
        
        for row, component in enumerate(self.components):
            name_item = QTableWidgetItem(component["name"])
            price_item = QTableWidgetItem(str(component["price"]))
            unit_item = QTableWidgetItem(component["unit"])
            vendor_item = QTableWidgetItem(component["vendor"])
            
            self.table_widget.setItem(row, 0, name_item)
            self.table_widget.setItem(row, 1, price_item)
            self.table_widget.setItem(row, 2, unit_item)
            self.table_widget.setItem(row, 3, vendor_item)
    
    def add_component(self):
        name = self.name_input.text()
        price = float(self.price_input.text())
        unit = self.unit_input.text()
        vendor = self.vendor_combo.currentText()
        
        # Perform any necessary validation on input
        
        # Create the component dictionary
        component = {
            "name": name,
            "price": price,
            "unit": unit,
            "vendor": vendor
        }
        
        # Add the component to the list
        self.components.append(component)
        
        # Update the table
        self.populate_table()
        
        # Clear the input fields
        self.name_input.clear()
        self.price_input.clear()
        self.unit_input.clear()
    
    def save_components(self):
        self.component_instance.save_components(self.components)
    
    def load_components(self):
        try:
            self.components =  self.component_instance.get_components()
        except:
            pass
    
    def closeEvent(self, event):
        self.save_components()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ComponentWindow()
    window.show()
    sys.exit(app.exec())
