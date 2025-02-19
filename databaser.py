
import os
import uuid
import random


class database:  # (Код класса database из вашего примера)

    def __init__(self, db_name):
        """Initializes the database with the given name. Creates the database directory if it doesn't exist."""
        self.db_name = db_name
        if not os.path.exists(self.db_name):
            os.makedirs(self.db_name)

    def create_table(self, table_name, columns):
        """Creates a new table with the specified name and columns.  Writes the schema to a file."""
        table_path = os.path.join(self.db_name, table_name)
        if not os.path.exists(table_path):
            os.makedirs(table_path)
            with open(os.path.join(table_path, "schema.txt"), "w") as f:
                f.write(",".join(columns))
        else:
            print(f"Table '{table_name}' already exists.")

    def insert(self, table_name, records):
        """Inserts multiple records into the specified table.

        Each record should be a dictionary where keys correspond to column names.
        """
        table_path = os.path.join(self.db_name, table_name)
        if not os.path.exists(table_path):
            raise Exception("Table does not exist.")

        schema_path = os.path.join(table_path, "schema.txt")
        with open(schema_path, "r") as f:
            columns = f.read().strip().split(",")

        # Determine the next available record ID by counting existing files
        existing_files = [f for f in os.listdir(table_path) if f != "schema.txt"]
        next_record_id = len(existing_files) + 1

        for record in records:
            record_id = str(next_record_id) + ".txt"
            record_path = os.path.join(table_path, record_id)
            with open(record_path, "w") as f:
                f.write(",".join([str(record.get(col, "")) for col in columns]))
            next_record_id += 1  # Increment for the next record


    def select(self, table_name, condition=None):
        """Selects records from the specified table based on the given condition.

        If no condition is provided, all records are returned.
        """
        table_path = os.path.join(self.db_name, table_name)
        if not os.path.exists(table_path):
            raise Exception("Table does not exist.")

        schema_path = os.path.join(table_path, "schema.txt")
        with open(schema_path, "r") as f:
            columns = f.read().strip().split(",")

        results = []
        for record_file in os.listdir(table_path):
            if record_file == "schema.txt":
                continue
            record_path = os.path.join(table_path, record_file)
            with open(record_path, "r") as f:
                record_data = f.read().strip().split(",")
                record = dict(zip(columns, record_data))

                if not condition or condition(record):
                    results.append(record)
        return results


    def update(self, table_name, updates, condition=None):
        """Updates records in the specified table based on the given condition.

        Only records that satisfy the condition will be updated.
        """
        table_path = os.path.join(self.db_name, table_name)
        if not os.path.exists(table_path):
            raise Exception("Table does not exist.")

        schema_path = os.path.join(table_path, "schema.txt")
        with open(schema_path, "r") as f:
            columns = f.read().strip().split(",")

        for record_file in os.listdir(table_path):
            if record_file == "schema.txt":
                continue

            record_path = os.path.join(table_path, record_file)
            with open(record_path, "r") as f:
                record_data = f.read().strip().split(",")
                record = dict(zip(columns, record_data))

            if not condition or condition(record):
                # Apply updates
                for key, value in updates.items():
                    if key in record:  # Only update columns that exist
                        record[key] = value

                # Write the updated record back to the file
                with open(record_path, "w") as f:
                    f.write(",".join([str(record.get(col, "")) for col in columns]))


    def delete(self, table_name, condition=None):
        """Deletes records from the specified table based on the given condition.

        Only records that satisfy the condition will be deleted.
        """
        table_path = os.path.join(self.db_name, table_name)
        if not os.path.exists(table_path):
            raise Exception("Table does not exist.")

        schema_path = os.path.join(table_path, "schema.txt")
        with open(schema_path, "r") as f:
            columns = f.read().strip().split(",")

        for record_file in os.listdir(table_path):
            if record_file == "schema.txt":
                continue

            record_path = os.path.join(table_path, record_file)
            with open(record_path, "r") as f:
                record_data = f.read().strip().split(",")
                record = dict(zip(columns, record_data))

            if not condition or condition(record):
                os.remove(record_path)


def iterate_database(db_name):
    """
    Проходит по всей базе данных и выводит информацию о каждой таблице и записи.

    Args:
        db_name: Имя базы данных (директории).
    """

    for table_name in os.listdir(db_name):
        table_path = os.path.join(db_name, table_name)

        # Убедимся, что это директория (таблица)
        if not os.path.isdir(table_path):
            continue

        print(f"Таблица: {table_name}")

        # Читаем схему
        schema_path = os.path.join(table_path, "schema.txt")
        try:
            with open(schema_path, "r") as f:
                columns = f.read().strip().split(",")
                print(f"  Колонки: {columns}")
        except FileNotFoundError:
            print("  Файл схемы не найден.")
            continue

        # Проходим по записям в таблице
        for record_file in os.listdir(table_path):
            if record_file == "schema.txt":
                continue

            record_path = os.path.join(table_path, record_file)

            try:
                with open(record_path, "r") as f:
                    record_data = f.read().strip().split(",")
                    record = dict(zip(columns, record_data)) # Создаем словарь для удобства

                    print(f"    Запись: {record_file}")
                    for key, value in record.items():
                        print(f"      {key}: {value}")

            except FileNotFoundError:
                print(f"    Файл записи {record_file} не найден.")
            except Exception as e:
                print(f"    Ошибка при чтении записи {record_file}: {e}")