import json

class Vendor():
    vendors = []
    vendor_names = []

    def create_vendor(self, name, contact):
        vendor = {
        "name": name,
        "contact": contact
        }
        return vendor

    def get_vendors(self):
        with open('data/vendors.json') as json_file:
            self.vendors = json.load(json_file)
        return self.vendors

    def save_vendors(self, vendors):
        with open("data/vendors.json", "w") as outfile:
            json.dump(vendors, outfile)
    
    def load_vendors(self):
        self.vendor_names = [item["name"] for item in self.get_vendors()]
        return self.vendor_names