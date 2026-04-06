import json
import os
import hashlib

class ChangeMonitor:
    def __init__(self, storage_dir='storage'):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def get_storage_path(self, site_name):
        return os.path.join(self.storage_dir, f"{site_name}.json")

    def load_previous_data(self, site_name):
        path = self.get_storage_path(site_name)
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        return None

    def save_current_data(self, site_name, data):
        path = self.get_storage_path(site_name)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)

    def generate_hash(self, data):
        data_str = json.dumps(data, sort_keys=True)
        return hashlib.md5(data_str.encode()).hexdigest()

    def has_changed(self, site_name, current_data):
        previous_data = self.load_previous_data(site_name)
        if previous_data is None:
            return True, "Initial data collected"
        
        current_hash = self.generate_hash(current_data)
        previous_hash = self.generate_hash(previous_data)

        if current_hash != previous_hash:
            # Here we could do more complex diffing
            return True, "Content changed"
        
        return False, None
