import pyodbc
from csv_reader import CSVReader  # Import the CSVReader class


def generate_insert_statements():
    """
    Generates SQL INSERT statements for the data in the CSV files.
    """
    try:
        csv_reader = CSVReader(".")
        output_file = "insert_data.sql"

        # Read data from CSV files
        customers_data = csv_reader.read_csv_file("customers_data.csv")
        employees_data = csv_reader.read_employees_data("employees_data.csv")
        orders_data = csv_reader.read_csv_file("orders_data.csv")

        with open(output_file, "w", encoding="utf-8") as f:
            # Generate INSERT statements for customers_data
            if customers_data:
                for customer in customers_data:
                    sql = f"""
                    INSERT INTO customers_data (customer_id, company_name, contact_name)
                    VALUES ('{customer['customer_id']}', '{customer['company_name'].replace("'", "''")}', '{customer['contact_name'].replace("'", "''")}');
                    """
                    f.write(sql + "\n")
                print("INSERT statements generated for 'customers_data'.")

            # Generate INSERT statements for employees_data
            if employees_data:
                for employee in employees_data:
                    #  Wrap birth_data in single quotes
                    sql = f"""
                    INSERT INTO employees_data (employee_id, first_name, last_name, title, birth_data, notes)
                    VALUES ({employee['employee_id']}, '{employee['first_name'].replace("'", "''")}', '{employee['last_name'].replace("'", "''")}', '{employee['title'].replace("'", "''")}', '{employee["birth_date"]}', '{employee['notes'].replace("'", "''")}');
                    """
                    f.write(sql + "\n")
                print("INSERT statements generated for 'employees_data'.")

            # Generate INSERT statements for orders_data
            if orders_data:
                for order in orders_data:
                    sql = f"""
                    INSERT INTO orders_data (order_id, customer_id, employee_id, order_date, ship_city)
                    VALUES ({order['order_id']}, '{order['customer_id']}', {order['employee_id']}, '{order['order_date']}', '{order['ship_city'].replace("'", "''")}');
                    """
                    f.write(sql + "\n")
                print("INSERT statements generated for 'orders_data'.")

        print(f"SQL INSERT statements saved to '{output_file}'.")

    except Exception as e:
        print(f"Error generating SQL: {e}")


if __name__ == "__main__":
    generate_insert_statements()
