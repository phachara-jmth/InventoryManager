import json
from datetime import datetime

class Database:
    def __init__(self):
        self.filename = "database.json"
        self.data = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {}

    def generate_item_code(self):
        date_code = datetime.now().strftime("%y%m%d")
        index = 1
        while f"{date_code}{index:03}" in self.data:
            index += 1
        return f"{date_code}{index:03}"

    def add_item(self, name, tags, status, staff_name, customer_name):
        item_code = self.generate_item_code()
        self.data[item_code] = {
            'Name': name,
            'Tag': tags,
            'Status': status,
            'Staff name': staff_name,
            'Customer name': customer_name,
            'Last edit date': datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        }

    def edit_item(self, item_code, data_key, data_val):
        if item_code in self.data and data_key in self.data[item_code]:
            self.data[item_code][data_key] = data_val
            self.data[item_code]['Last edit date'] = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        else:
            print("Item code or data key not found in database.")

    def remove_item(self, item_code):
        if item_code in self.data:
            del self.data[item_code]

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)


# Usage Example
if __name__ == "__main__":
    db = Database()
    db.add_item("camera01", ["#camera", "#SVS"], "stock", "James", "Denso")
    db.edit_item("240108001", "Status", "sold")
    db.save_data()
