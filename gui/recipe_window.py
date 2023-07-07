import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QComboBox

class RecipeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recipe Manager")
        self.setup_ui()
        
        # Initialize recipe data
        self.recipes = []
        self.load_recipes()  # Load existing recipes from JSON or dictionary
        
        # Populate table with recipes
        self.populate_table()
    
    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)
        
        # Create table widget for displaying recipes
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Total Price", "Ingredients"])
        main_layout.addWidget(self.table_widget)
        
        # Create widget for adding a new recipe
        add_widget = QWidget()
        add_layout = QVBoxLayout()
        add_widget.setLayout(add_layout)
        
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        add_layout.addWidget(name_label)
        add_layout.addWidget(self.name_input)
        
        # Create table widget for listing assigned ingredients
        self.ingredients_table = QTableWidget()
        self.ingredients_table.setColumnCount(2)
        self.ingredients_table.setHorizontalHeaderLabels(["Ingredient", "Quantity"])
        add_layout.addWidget(self.ingredients_table)
        
        ingredient_layout = QHBoxLayout()
        ingredient_label = QLabel("Ingredient:")
        self.ingredient_combo = QComboBox()
        self.ingredient_combo.addItems(["Ingredient 1", "Ingredient 2", "Ingredient 3"])  # Add your defined ingredients here
        quantity_label = QLabel("Quantity:")
        self.quantity_input = QLineEdit()
        add_ingredient_button = QPushButton("➕ Add Ingredient")
        add_ingredient_button.clicked.connect(self.add_ingredient)
        ingredient_layout.addWidget(ingredient_label)
        ingredient_layout.addWidget(self.ingredient_combo)
        ingredient_layout.addWidget(quantity_label)
        ingredient_layout.addWidget(self.quantity_input)
        ingredient_layout.addWidget(add_ingredient_button)
        add_layout.addLayout(ingredient_layout)
        
        save_button = QPushButton("💾 Save Recipe")
        save_button.clicked.connect(self.save_recipe)
        add_layout.addWidget(save_button)
        
        main_layout.addWidget(add_widget)
        
        self.setCentralWidget(main_widget)
    
    def populate_table(self):
        self.table_widget.setRowCount(len(self.recipes))
        
        for row, recipe in enumerate(self.recipes):
            name_item = QTableWidgetItem(recipe["name"])
            total_price_item = QTableWidgetItem(str(recipe["total_price"]))
            print(recipe)
            print(recipe['ingredients'])
            print(type(recipe['ingredients']))
            # ingredients_item = QTableWidgetItem(", ".join(recipe["ingredients"]))
            ingredients_item = QTableWidgetItem(str(self.list_ingredients(recipe['ingredients'])))
            
            self.table_widget.setItem(row, 0, name_item)
            self.table_widget.setItem(row, 1, total_price_item)
            self.table_widget.setItem(row, 2, ingredients_item)
    
    def list_ingredients(self, ingredients_list):
        # ingredients = [ingredient["ingredient"] for ingredient in ingredients_list]
        ingredients =  ', '.join([item['ingredient'] for item in ingredients_list])
        # for item in ingredients_list:
        #     ingredient = item["ingredient"]
        #     ingredients.append(ingredient)
        return ingredients

    def add_ingredient(self):
        ingredient = self.ingredient_combo.currentText()
        quantity = self.quantity_input.text()
        
        # Perform any necessary validation on input
        
        # Add ingredient to the ingredients table
        row_count = self.ingredients_table.rowCount()
        self.ingredients_table.setRowCount(row_count + 1)
        self.ingredients_table.setItem(row_count, 0, QTableWidgetItem(ingredient))
        self.ingredients_table.setItem(row_count, 1, QTableWidgetItem(quantity))
        
        # Clear the ingredient and quantity input fields
        self.quantity_input.clear()
    
    def save_recipe(self):
        name = self.name_input.text()
        
        # Retrieve ingredients from the ingredients table
        ingredient_rows = self.ingredients_table.rowCount()
        ingredients = []
        for row in range(ingredient_rows):
            ingredient = self.ingredients_table.item(row, 0).text()
            quantity = self.ingredients_table.item(row, 1).text()
            ingredients.append({"ingredient": ingredient, "quantity": quantity})
        
        # Perform any necessary validation on input
        
        # Calculate total price based on ingredient prices and quantities
        
        # Create the recipe dictionary
        recipe = {
            "name": name,
            "total_price": 0, #total_price, create def total_price(recipe)?
            "ingredients": ingredients
        }
        
        # Add the recipe to the list
        self.recipes.append(recipe)
        
        # Update the table
        self.populate_table()
        
        # Clear the input fields
        self.name_input.clear()
        self.ingredients_table.clearContents()
        self.ingredients_table.setRowCount(0)
    
    def delete_recipe(self):
        selected_rows = self.table_widget.selectedItems()
        
        if selected_rows:
            row = selected_rows[0].row()
            del self.recipes[row]
            self.populate_table()
        else:
            QMessageBox.warning(self, "Error", "Please select a recipe to delete.")
    
    def load_recipes(self):
        # Load recipes from JSON or dictionary and populate self.recipes
        pass
        
    def save_recipes(self):
        # Save self.recipes to JSON or dictionary
        pass
    
    def closeEvent(self, event):
        self.save_recipes()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecipeWindow()
    window.show()
    sys.exit(app.exec())
