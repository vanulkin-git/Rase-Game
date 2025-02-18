import os
import json

class TextDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_file = f"{db_name}.txt"
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r') as f:
                    content = f.read()
                    if content:
                        return json.loads(content)
                    else:
                        return {}
            except json.JSONDecodeError:
                print("Error: Database file is corrupted.  Starting with an empty database.")
                return {}
        else:
            return {}

    def save_data(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def create_table(self, table_name):
        if table_name not in self.data:
            self.data[table_name] = []
            self.save_data()
            return True
        else:
            return False

    def insert_data(self, table_name, *records):
        if table_name in self.data:
            self.data[table_name].extend(records)
            self.save_data()
            return True
        else:
            return False

    def get_all_data(self, table_name):
        if table_name in self.data:
            return self.data[table_name]
        else:
            return None

    def query_data(self, table_name, condition):
        if table_name in self.data:
            results = [record for record in self.data[table_name] if condition(record)]
            return results
        else:
            return None

    def update_data(self, table_name, condition, update_func):
        if table_name in self.data:
            updated_count = 0
            for i, record in enumerate(self.data[table_name]):
                if condition(record):
                    self.data[table_name][i] = update_func(record)
                    updated_count += 1
            self.save_data()
            return updated_count
        else:
            return 0

    def delete_data(self, table_name, condition):
        if table_name in self.data:
            original_length = len(self.data[table_name])
            self.data[table_name] = [record for record in self.data[table_name] if not condition(record)]
            deleted_count = original_length - len(self.data[table_name])
            self.save_data()
            return deleted_count
        else:
            return 0