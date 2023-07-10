import json
from objects.object import Object

class Component(Object):
    components = []
    component_names = []
    component_units = []
    component_names_and_units = []

    def create_component(self, name, price, unit, vendor):
        new_component = {}
        try:
            new_component = {
            "name": name,
            "price": price,
            "unit": unit,
            "vendor": vendor
            }
            return new_component
        except:
            Object.open_error_window("Something went wrong!")

    def get_components(self):
        with open('data/components.json') as json_file:
            self.components = json.load(json_file)
        return self.components

    def save_components(self, components):
        with open("data/components.json", "w") as outfile:
            json.dump(components, outfile)

    def load_components(self):
        self.component_names = [item["name"] for item in self.get_components()]
        self.component_units = [item["unit"] for item in self.get_components()]
        self.component_names_and_units = [f"{name} ({unit})" for name, unit in zip(self.component_names, self.component_units)]
        return self.component_names_and_units