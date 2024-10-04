#sample_file_gen_gui.py

import pandas as pd
import random
from faker import Faker
import common_code_gui as common

# Initialize Faker for generating dummy data
fake = Faker()

def generate_dummy_data(num_rows, column_info):
    """Generates dummy data for the specified number of rows and given column info."""
    data = {}

    for column_name, data_type in column_info.items():
        if data_type == "Name":
            data[column_name] = [fake.name() for _ in range(num_rows)]
        elif data_type == "Age":
            data[column_name] = [random.randint(18, 70) for _ in range(num_rows)]
        elif data_type == "Email":
            data[column_name] = [fake.email() for _ in range(num_rows)]
        elif data_type == "Text":
            data[column_name] = [fake.text(max_nb_chars=20) for _ in range(num_rows)]
        else:
            data[column_name] = [fake.word() for _ in range(num_rows)]  # Default to random words

    return pd.DataFrame(data)

def save_to_file(df):
    """Prompts the user to save the DataFrame to a specified file format using common functions."""
    filename, filetype = common.save_file_dialog("Save Dummy Data", "excel")  # Prompt for filename and type

    if filename:
        try:
            common.save_merged_file(df, filename)
            common.log_message(f"Generated {len(df)} records and saved to {filename}.", level='info')
            common.display_message(f"Generated {len(df)} records and saved to {filename}.", status="success")
        except Exception as e:
            raise e
    else:
        raise ValueError("File not saved.")
