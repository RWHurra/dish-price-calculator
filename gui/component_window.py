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
        self.main_layout = QHBoxLayout()
        main_widget.setLayout(self.main_layout)

        # Initialize Vendor class
        self.vendor_instance = Vendor()
        
        # Create table widget for displaying components
        self.create_table_widget()
        
        # Create widget for adding a new component
        self.create_add_component_widget()
        
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

    def create_table_widget(self):
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Price", "Unit", "Vendor"])
        self.main_layout.addWidget(self.table_widget)

    def create_add_component_widget(self):
        add_widget = QWidget()
        add_layout = QVBoxLayout()
        add_widget.setLayout(add_layout)
        
        # Create input for component name
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        add_layout.addWidget(name_label)
        add_layout.addWidget(self.name_input)
        
        # Create input for component price
        price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        add_layout.addWidget(price_label)
        add_layout.addWidget(self.price_input)
        
        # Create input for component unit
        unit_label = QLabel("Unit:")
        self.unit_input = QLineEdit()
        add_layout.addWidget(unit_label)
        add_layout.addWidget(self.unit_input)
        
        # Create input for component vendor
        vendor_label = QLabel("Vendor:")
        self.vendor_combo = QComboBox()
        try:
            self.vendor_combo.addItems(self.vendor_instance.load_vendors())
        except:
            self.vendor_combo.addItems(["No vendors found"])
        add_layout.addWidget(vendor_label)
        add_layout.addWidget(self.vendor_combo)

        # Create save component button
        save_button = QPushButton("💾 Save Component")
        save_button.clicked.connect(self.add_component)
        add_layout.addWidget(save_button)
        
        self.main_layout.addWidget(add_widget)

    def add_component(self):
        # Get user input for new component
        name, price, unit, vendor = self.get_user_input()
        
        # Validate user input data
        if not self.user_input_validated(name, price, unit, vendor):
            return

        # Create the component dictionary
        component = self.component_instance.create_component(name, price, unit, vendor)

        # Add the component to the list
        self.components.append(component)

        # Update the table
        self.populate_table()
        
        # Clear the input fields
        self.name_input.clear()
        self.price_input.clear()
        self.unit_input.clear()
    
    def get_user_input(self):
        name = self.name_input.text()
        price = self.price_input.text()
        unit = self.unit_input.text()
        vendor = self.vendor_combo.currentText()
        return name, price, unit, vendor

    def user_input_validated(self, name, price, unit, vendor):
        if (name == "" or unit == ""):
            QMessageBox.warning(self, "Error", "Make sure to enter a name and unit.")
            return False
        try:
            float(price)
        except:
            QMessageBox.warning(self, "Error", "Make sure price is of type float.")
            return False
        else:
            return True
        

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
