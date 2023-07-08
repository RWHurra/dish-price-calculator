import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox

class VendorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vendor Manager")
        self.setup_ui()
        
        # Initialize vendor data
        self.vendors = []
        self.load_vendors()  # Load existing vendors from JSON or dictionary
        
        # Populate table with vendors
        self.populate_table()
    
    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        
        # Create table widget for displaying vendors
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Contact"])
        main_layout.addWidget(self.table_widget)
        
        # Create widget for adding a new vendor
        add_widget = QWidget()
        add_layout = QVBoxLayout()
        add_widget.setLayout(add_layout)
        
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        contact_label = QLabel("Contact:")
        self.contact_input = QLineEdit()
        add_button = QPushButton("➕ Add Vendor")
        add_button.clicked.connect(self.add_vendor)
        add_layout.addWidget(name_label)
        add_layout.addWidget(self.name_input)
        add_layout.addWidget(contact_label)
        add_layout.addWidget(self.contact_input)
        add_layout.addWidget(add_button)
        
        main_layout.addWidget(add_widget)
        
        self.setCentralWidget(main_widget)
    
    def populate_table(self):
        self.table_widget.setRowCount(len(self.vendors))
        
        for row, vendor in enumerate(self.vendors):
            name_item = QTableWidgetItem(vendor["name"])
            contact_item = QTableWidgetItem(vendor["contact"])
            
            self.table_widget.setItem(row, 0, name_item)
            self.table_widget.setItem(row, 1, contact_item)
    
    def add_vendor(self):
        name = self.name_input.text()
        contact = self.contact_input.text()
        
        # Perform any necessary validation on input
        
        # Create the vendor dictionary
        vendor = {
            "name": name,
            "contact": contact
        }
        
        # Add the vendor to the list
        self.vendors.append(vendor)
        
        # Update the table
        self.populate_table()
        
        # Clear the input fields
        self.name_input.clear()
        self.contact_input.clear()
    
    def delete_vendor(self):
        selected_rows = self.table_widget.selectedItems()
        
        if selected_rows:
            row = selected_rows[0].row()
            del self.vendors[row]
            self.populate_table()
        else:
            QMessageBox.warning(self, "Error", "Please select a vendor to delete.")
    
    def load_vendors(self):
        # Load vendors from JSON or dictionary and populate self.vendors
        pass
        
    def save_vendors(self):
        # Save self.vendors to JSON or dictionary
        pass
    
    def closeEvent(self, event):
        self.save_vendors()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VendorWindow()
    window.show()
    sys.exit(app.exec())
