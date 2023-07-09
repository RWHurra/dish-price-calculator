import json

class Vendor():
    vendors = []
    vendor_names = []

    def get_vendors(self):
        with open('vendors.json') as json_file:
            self.vendors = json.load(json_file)
        return self.vendors

    def save_vendors(self, vendors):
        with open("vendors.json", "w") as outfile:
            json.dump(vendors, outfile)
    
    def load_vendors(self):
        self.vendor_names = [item["name"] for item in self.get_vendors()]
        return self.vendor_names