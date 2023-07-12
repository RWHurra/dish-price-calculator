import json
from objects.component import Component

class Dish():
    dishes = []
    total_cost = 0
    component_instance = Component()

    def create_dish(self, name, components):
        dish = {
            "name": name,
            "total_price": self.get_total_cost(components),
            "components": components
        }
        return dish

    def get_dishes(self):
        with open('data/dishes.json') as json_file:
            self.dishes = json.load(json_file)
        return self.dishes

    def save_dishes(self, dishes):
        with open("data/dishes.json", "w") as outfile:
            json.dump(dishes, outfile)

    def get_total_cost(self, components):
        for item in components:
            component_name = item["component"]#.split(" (")[0]
            quantity = float(item["quantity"])
            
            for component in self.component_instance.get_components():
                if component["name"] == component_name:
                    price = component["price"]
                    cost = price * quantity
                    self.total_cost += cost
                    break
        return self.total_cost