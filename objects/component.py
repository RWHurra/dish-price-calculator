import json

class Component():
    components = []
    component_names = []

    def get_components(self):
        with open('components.json') as json_file:
            self.components = json.load(json_file)
        return self.components

    def save_components(self, components):
        with open("components.json", "w") as outfile:
            json.dump(components, outfile)

    def load_components(self):
        self.component_names = [item["name"] for item in self.get_components()]
        return self.component_names