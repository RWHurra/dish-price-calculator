import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QComboBox

class DishWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dish Manager")
        self.setup_ui()
        
        # Initialize dish data
        self.dishes = []
        self.load_dishes()  # Load existing dishes from JSON or dictionary
        
        # Populate table with dishes
        self.populate_table()
    
    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        
        # Create table widget for displaying dishes
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Total Price", "Dish Components"])
        main_layout.addWidget(self.table_widget)
        
        # Create widget for adding a new dish
        add_widget = QWidget()
        add_layout = QVBoxLayout()
        add_widget.setLayout(add_layout)
        
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        add_layout.addWidget(name_label)
        add_layout.addWidget(self.name_input)
        
        # Create table widget for listing assigned dish components
        self.components_table = QTableWidget()
        self.components_table.setColumnCount(2)
        self.components_table.setHorizontalHeaderLabels(["Dish Component", "Quantity"])
        add_layout.addWidget(self.components_table)
        
        component_layout = QHBoxLayout()
        component_label = QLabel("Dish Component:")
        self.component_combo = QComboBox()
        self.component_combo.addItems(["Dish Component 1", "Dish Component 2", "Dish Component 3"])  # Add your defined dish components here
        quantity_label = QLabel("Quantity:")
        self.quantity_input = QLineEdit()
        add_component_button = QPushButton("➕ Add Dish Component")
        add_component_button.clicked.connect(self.add_component)
        component_layout.addWidget(component_label)
        component_layout.addWidget(self.component_combo)
        component_layout.addWidget(quantity_label)
        component_layout.addWidget(self.quantity_input)
        component_layout.addWidget(add_component_button)
        add_layout.addLayout(component_layout)
        
        save_button = QPushButton("💾 Save Dish")
        save_button.clicked.connect(self.save_dish)
        add_layout.addWidget(save_button)
        
        main_layout.addWidget(add_widget)
        
        self.setCentralWidget(main_widget)
    
    def populate_table(self):
        self.table_widget.setRowCount(len(self.dishes))
        
        for row, dish in enumerate(self.dishes):
            name_item = QTableWidgetItem(dish["name"])
            total_price_item = QTableWidgetItem(str(dish["total_price"]))
            components_item = QTableWidgetItem(str(self.list_dish_components(dish['components'])))
            
            self.table_widget.setItem(row, 0, name_item)
            self.table_widget.setItem(row, 1, total_price_item)
            self.table_widget.setItem(row, 2, components_item)
    
    def list_dish_components(self, components_list):
        components = ', '.join([item['component'] for item in components_list])
        return components

    def add_component(self):
        component = self.component_combo.currentText()
        quantity = self.quantity_input.text()
        
        # Perform any necessary validation on input
        
        # Add component to the components table
        row_count = self.components_table.rowCount()
        self.components_table.setRowCount(row_count + 1)
        self.components_table.setItem(row_count, 0, QTableWidgetItem(component))
        self.components_table.setItem(row_count, 1, QTableWidgetItem(quantity))
        
        # Clear the component and quantity input fields
        self.quantity_input.clear()
    
    def save_dish(self):
        name = self.name_input.text()
        
        # Retrieve components from the components table
        component_rows = self.components_table.rowCount()
        components = []
        for row in range(component_rows):
            component = self.components_table.item(row, 0).text()
            quantity = self.components_table.item(row, 1).text()
            components.append({"component": component, "quantity": quantity})
        
        # Perform any necessary validation on input
        
        # Calculate total price based on component prices and quantities
        
        # Create the dish dictionary
        dish = {
            "name": name,
            "total_price": 0,  # total_price (implement calculation logic),
            "components": components
        }
        
        # Add the dish to the list
        self.dishes.append(dish)
        
        # Update the table
        self.populate_table()
        
        # Clear the input fields
        self.name_input.clear()
        self.components_table.clearContents()
        self.components_table.setRowCount(0)
    
    def delete_dish(self):
        selected_rows = self.table_widget.selectedItems()
        
        if selected_rows:
            row = selected_rows[0].row()
            del self.dishes[row]
            self.populate_table()
        else:
            QMessageBox.warning(self, "Error", "Please select a dish to delete.")
    
    def load_dishes(self):
        # Load dishes from JSON or dictionary and populate self.dishes
        pass
        
    def save_dishes(self):
        # Save self.dishes to JSON or dictionary
        pass
    
    def closeEvent(self, event):
        self.save_dishes()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DishWindow()
    window.show()
    sys.exit(app.exec())