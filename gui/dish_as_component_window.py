from PyQt6.QtWidgets import (QMainWindow,
                             QWidget,
                             QVBoxLayout,
                             QLabel,
                             QLineEdit,
                             QPushButton,
                             QMessageBox)
from objects.component import Component

class DishAsComponent(QMainWindow):
    def __init__(self, dish, component_combo):
        super().__init__()
        self.setWindowTitle("Save Dish as Component")
        
        # Create DishWindow instance
        self.component_instance = Component()
        self.dish = dish
        self.component_combo = component_combo

        # Create the central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create the layout
        layout = QVBoxLayout(self.central_widget)

        self.inputs = {
            "unit": "Enter unit for component",
            "price adjustment": dish["total_price"]
            }

        # Create labels and line edits for each input
        self.line_edits = {}
        for key, value in self.inputs.items():
            # Create label
            label_widget = QLabel(key)
            layout.addWidget(label_widget)

            # Create the line edit and set the default value
            line_edit = QLineEdit(str(value))
            self.line_edits[key] = line_edit
            layout.addWidget(line_edit)

        self.save_button = QPushButton("💾 Save")
        self.save_button.clicked.connect(self.save_changes)
        layout.addWidget(self.save_button)

    def save_changes(self):
        unit, price = self.get_user_input()

        if not self.user_input_validated(unit, price):
            return
        
        # Calculate price if inputted as formula, and make float
        if type(price) is not float:
            price = float(eval(price))
        self.add_dish_as_component(unit, price)
        self.close()

    def add_dish_as_component(self, unit, price):
        component = self.component_instance.create_component(self.dish['name'], price, unit, 'In house')
        components = self.component_instance.get_components()
        components.append(component)
        self.component_instance.save_components(components)
        self.component_combo.addItem(component['name'] + " (" + component['unit'] + ")")

    def get_user_input(self):
        for key, value in self.line_edits.items():
            match key:
                case "price adjustment":
                    price = value.text()
                case "unit":
                    unit = value.text()
        return unit, price

    def user_input_validated(self, unit, price):
        if unit == "":
            QMessageBox.warning(self, "Error", "Make sure to enter a unit.")
            return False
        try:
            price = eval(price)
            float(price)
        except:
            QMessageBox.warning(self, "Error", "Make sure price is of type float.")
            return False
        else:
            return True