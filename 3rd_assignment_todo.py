import psycopg2


class Todo:
    """Handles Todo items adding, reading, updating items, and deleting items"""

    def __init__(self):
        self._DB_CONFIG = {
            'host': 'localhost',
            'database': 'Bincom3rdAssignment',
            'user': 'postgres',
            'password': 'Command22__',
            'port': '5432'
        }

        # Establish a connection to the PostgreSQL database
        self._connection = psycopg2.connect(**self._DB_CONFIG)
        self._cursor = self._connection.cursor()

    def add_item(self, item):
        try:
            # Create a table if it doesn't exist (you may need to customize this based on your data)
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS TodoLists (
                name VARCHAR(255) UNIQUE
            );
            '''
            self._cursor.execute(create_table_query)

            # Insert the item into the table
            insert_query = f'''
            INSERT INTO TodoLists
            VALUES (%s);
            '''
            self._cursor.execute(insert_query, (item,))
            # Commit the changes and close the connection
            self._connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def list_items(self):
        try:
            # Execute a SELECT query to retrieve all items from the table
            select_query = 'SELECT * FROM TodoLists;'
            self._cursor.execute(select_query)

            # Fetch all rows
            items = self._cursor.fetchall()
            # Print or use the retrieved items
            for item in items:
                print(item[0])

        except Exception as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()

    def update_item(self, item, new_item):
        try:
            # Execute a SELECT query to retrieve all items from the table
            select_query = f'UPDATE TodoLists SET name=%s WHERE name=%s;'
            self._cursor.execute(select_query, (new_item, item))

            # Commit the changes and close the connection
            self._connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def delete_item(self, item):
        try:
            # Execute a DELETE query to remove the item from the table
            delete_query = 'DELETE FROM TodoLists WHERE name = %s;'
            self._cursor.execute(delete_query, (item,))

            # Commit the changes
            self._connection.commit()

            print(f"Item with ID {item} deleted successfully.")

        except Exception as e:
            print(f"Error: {e}")


items = ["daniel", "udokike", "ikegbunam", "developer"]
obj = Todo()

for item in items:
    obj.add_item(item)

print("----------All items ----------")
obj.list_items()
print("------------------------------")

# Update the first 3 names to Python, Django, Programming"
items_to_change = ["daniel", "udokike", "ikegbunam"]
new_items = ["Python", "Django", "Programming"]

for old_item, new_item in zip(items_to_change, new_items):
    obj.update_item(old_item, new_item)
print("----------New Updated items ----------")
obj.list_items()
print("------------------------------")

# Delete Developer from the DB
obj.delete_item("developer")
print("----------Items After deleting developer ----------")
obj.list_items()
print("------------------------------")

# Close the connection
obj.close_connection()
