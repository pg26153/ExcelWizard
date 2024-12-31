#sample_file_gen_gui.py

import pandas as pd
import random
from faker import Faker
import common_code_gui as common
import re  # Import regular expression module

# Initialize Faker for generating dummy data
fake = Faker()

# Mapping of human-readable column names to Faker method names
column_to_method_map = {
    'phone': 'phone_number',
    'address': 'address',
    'email': 'email',
    'name': 'name',
    'company': 'company',
    'city': 'city',
    'country': 'country',
    'date_of_birth': 'date_of_birth',
    'ssn': 'ssn',
    'text': 'text',
    'word': 'word',
    'paragraph': 'paragraph',
    'uuid': 'uuid4',
    'job': 'job',
    'date': 'date_this_century',
    'time': 'time',
    'timezone': 'timezone',
    'credit_card': 'credit_card_number',
    'url': 'url',
    'image': 'image_url',
    'boolean': 'boolean',
    # Add more mappings as necessary
}

def is_numeric_type(column_type):
    """Check if the column type is numeric (integer, float, etc.)."""
    try:
        # Normalize the column_type to lowercase
        column_type = column_type.lower()

        # Define common numeric types
        numeric_types = ['int', 'integer', 'float', 'double', 'decimal', 'numeric']

        # Check if the column_type is one of the common numeric types
        if column_type in numeric_types:
            return True

    except Exception:
        return False

def generate_dummy_data(num_rows, column_info):
    """Generates dummy data for the specified number of rows and given column info."""
    data = {}

    # Loop through the column names and dynamically call the appropriate Faker method
    for column_name, column_type in column_info.items():
        try:
            # Check if the column type name contains only valid characters (alphanumeric or underscores)
            if not re.match(r'^[a-zA-Z0-9_]+$', column_type):
                raise ValueError(f"Invalid characters found in column type name '{column_type}' for column '{column_name}'.")

            # Normalize column name to check in our column_to_method_map
            method_name = column_to_method_map.get(column_name.lower(), None)

            if method_name:
                method = getattr(fake, method_name)  # Get the corresponding Faker method
                # Generate the corresponding values using the method
                data[column_name] = [method() for _ in range(num_rows)]
            elif is_numeric_type(column_type):  # Handle numeric types dynamically
                print(f"Warning: No specific rule for column '{column_name}'. Using random numbers.")
                data[column_name] = [random.randint(1, 1000) for _ in range(num_rows)]  # Random integers as default
            else:
                print(f"Warning: No specific rule for column '{column_name}'. Using random words as default.")
                data[column_name] = [fake.word() for _ in range(num_rows)]  # Random words as fallback

        except ValueError as e:
            print(f"Error: {e}")  # Log the invalid column type error
            continue  # Skip the invalid column and continue with the next

    return pd.DataFrame(data)

def save_to_file(df):
    """Prompts the user to save the DataFrame to a specified file format using common functions."""
    filename, filetype = common.save_file_dialog("Save Dummy Data")  # Prompt for filename and type

    if filename:
        try:
            common.save_merged_file(df, filename)
            common.log_message(f"Generated {len(df)} records and saved to {filename}.", level='info')
            common.display_message(f"Generated {len(df)} records and saved to {filename}.", status="success")
        except Exception as e:
            raise e
    else:
        raise ValueError("File not saved.")
