import psycopg2

from baby_names import NameReader


class BabyName:
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

    def add_baby_name(self, baby_name):
        try:
            # Create a table if it doesn't exist (you may need to customize this based on your data)
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS BabyNames (
                name VARCHAR(255)
            );
            '''
            self._cursor.execute(create_table_query)

            # Insert the item into the table
            insert_query = f'''
            INSERT INTO BabyNames
            VALUES (%s);
            '''
            self._cursor.execute(insert_query, (baby_name,))
            # Commit the changes and close the connection
            self._connection.commit()
            print(f"Successfully added {baby_name} ---- 100%")
        except Exception as e:
            print(f"Error: {e}")

    def close_db_connection(self):
        if self._connection:
            self._cursor.close()
            self._connection.close()


# Get all baby names
baby_names = NameReader("baby2008.html").read_baby_names()
for baby_name in baby_names:
    BabyName().add_baby_name(baby_name)
