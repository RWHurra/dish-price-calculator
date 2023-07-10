import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QComboBox
from objects.component import Component
from objects.dish import Dish

class DishWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dish Manager")
        self.setup_ui()
        
        # Initialize Dish class
        self.dish_instance = Dish()

        # Initialize dish data
        self.dishes = []
        self.load_dishes()
        
        # Populate table with dishes
        self.populate_table()

    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Initialize Component class
        self.component_instance = Component()

        # Create layout for the left side (dishes table and delete button)
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        # Create table widget for displaying dishes
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Total Price", "Dish Components"])
        left_layout.addWidget(self.table_widget)

        # Create button for deleting a dish
        delete_button = QPushButton("🗑️ Delete Dish")
        delete_button.clicked.connect(self.delete_dish)
        left_layout.addWidget(delete_button)

        # Create layout for the right side (GUI to create a new dish)
        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

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
        try:
            self.component_combo.addItems(self.component_instance.load_components())
        except:
            self.component_combo.addItems(['No components found'])
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

        right_layout.addWidget(add_widget)

        self.setCentralWidget(main_widget)

    def populate_table(self):
        self.table_widget.setRowCount(len(self.dishes))
        
        for row, dish in enumerate(self.dishes):
            name_item = QTableWidgetItem(dish["name"])
            total_price_item = QTableWidgetItem(str(dish["total_price"]))
            component_details = self.get_component_details(dish)
            components_item = QTableWidgetItem(str(component_details))
            
            self.table_widget.setItem(row, 0, name_item)
            self.table_widget.setItem(row, 1, total_price_item)
            self.table_widget.setItem(row, 2, components_item)
    
    def get_component_details(self, dish):
        # I have no idea how the line below works, got it from ChatGPT
        # but it lists the components of the dish in the following format:
        # <component_name> <component_quantity> <component_unit>
        components_with_quantity_and_unit = (", ".join([f"{component['component']} {component['quantity']} {next(item['unit'] for item in self.component_instance.get_components() if item['name'] == component['component'])}" for component in dish['components']]))
        return components_with_quantity_and_unit

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
            component = self.components_table.item(row, 0).text().split(" (")[0] # The split removes unit from string
            quantity = self.components_table.item(row, 1).text()
            components.append({"component": component, "quantity": quantity})
        
        # Perform any necessary validation on input
        
        # Calculate total price based on component prices and quantities
        
        # Create the dish dictionary
        dish = {
            "name": name,
            "total_price": self.dish_instance.get_total_cost(components),  # total_price (implement calculation logic),
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
        try:
            self.dishes =  self.dish_instance.get_dishes()
        except:
            pass
        
    def save_dishes(self):
        self.dish_instance.save_dishes(self.dishes)
        pass
    
    def closeEvent(self, event):
        self.save_dishes()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DishWindow()
    window.show()
    sys.exit(app.exec())