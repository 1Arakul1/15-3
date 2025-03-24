import pyodbc
from csv_reader import CSVReader  # Import the CSVReader class


def insert_data_into_tables():
    """
    Reads data from the CSV files and inserts it into the tables.
    """
    try:
        # Connection string to the Northwind database
        connection_string = (
            r"Driver={ODBC Driver 17 for SQL Server};"
            r"Server=DESKTOP-AM0MSA0\SQLEXPRESS;"  # Твое имя сервера
            r"Database=Northwind;"
            r"UID=Hakimov;"  # Твое имя пользователя
            r"PWD=NIAZrezeda12;"  # Твой пароль
        )

        cnxn = pyodbc.connect(connection_string)
        cursor = cnxn.cursor()

        csv_reader = CSVReader(".")

        # Insert data into customers_data
        customers_data = csv_reader.read_csv_file("customers_data.csv")
        if customers_data:
            for customer in customers_data:
                cursor.execute("""
                    INSERT INTO customers_data (customer_id, company_name, contact_name)
                    VALUES (?, ?, ?)
                """, customer['customer_id'], customer['company_name'], customer['contact_name'])
            print("Data inserted into 'customers_data' successfully.")

        # Insert data into employees_data
        employees_data = csv_reader.read_employees_data("employees_data.csv")
        if employees_data:
            for employee in employees_data:
                # Pass birth_data as is (string)
                birth_date = employee['birth_data']
                cursor.execute("""
                    INSERT INTO employees_data (employee_id, first_name, last_name, title, birth_data, notes)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, employee['employee_id'], employee['first_name'], employee['last_name'], employee['title'], birth_date, employee['notes'])
            print("Data inserted into 'employees_data' successfully.")

        # Insert data into orders_data
        orders_data = csv_reader.read_csv_file("orders_data.csv")
        if orders_data:
            for order in orders_data:
                # Pass order_date as is (string)
                order_date = order['order_date']
                cursor.execute("""
                    INSERT INTO orders_data (order_id, customer_id, employee_id, order_date, ship_city)
                    VALUES (?, ?, ?, ?, ?)
                """, order['order_id'], order['customer_id'], order['employee_id'], order_date, order['ship_city'])
            print("Data inserted into 'orders_data' successfully.")

        cnxn.commit()
        cnxn.close()

    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print("Error inserting data into tables!")
        print("SQL Error Code:", sqlstate)
        print("Error Details:", ex)
    except Exception as e:
        print(f"Other Error: {e}")


if __name__ == "__main__":
    insert_data_into_tables()