import csv

class CSVReader:
    """
    A class for reading data from CSV files.
    """

    def __init__(self, directory):
        """
        Initializes the CSVReader with the directory containing the CSV files.
        """
        self.directory = directory

    def read_csv_file(self, filename):
        """
        Reads data from a CSV file and returns it as a list of dictionaries.
        """
        filepath = f"{self.directory}/{filename}"
        data = []
        try:
            with open(filepath, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Error: File not found: {filepath}")
            return None
        except Exception as e:
            print(f"Error reading file: {filepath} - {e}")
            return None
        return data

    def read_employees_data(self, filename):
        """
        Reads employee data from a CSV file, adds a unique employee_id,
        and returns it as a list of dictionaries.
        """
        employee_data = self.read_csv_file(filename)
        if employee_data is None:
            return None

        # Add unique employee_id (starting from 1)
        for i, employee in enumerate(employee_data):
            employee['employee_id'] = i + 1

        return employee_data