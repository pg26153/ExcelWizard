#file_format_conv_gui.py

import pandas as pd
import common_code_gui as common
import hashlib
import os

def hash_dataframe(dataframe):
    """Create a hash for the DataFrame to check for data integrity."""
    # Convert the DataFrame to a string, then encode and hash it
    return hashlib.md5(pd.util.hash_pandas_object(dataframe).values).hexdigest()

def file_format_conversion_ops():
    try:
        # Open a file dialog to select an Excel or CSV file
        input_file, error_message = common.open_file_dialog("Select Excel or CSV File to Convert")
        if not input_file:
            raise ValueError(error_message)
        
        # Ask the user for the desired output format
        output_format = common.simple_input_dialog("Input", "Enter the format to convert to (CSV, XLSX):")
        if output_format and output_format.upper() in ["CSV", "XLSX"]:
            # Read the input file using the common read_data function
            original_dataframe = common.read_data(input_file)

            # Hash the original DataFrame
            original_hash = hash_dataframe(original_dataframe)

            # Prepare the output file path using a save file dialog
            output_file, error_message = common.save_file_dialog("Save Converted File As",output_format.lower())
            if not output_file:
                raise ValueError(error_message)

            # Save the DataFrame to the selected format
            common.save_merged_file(original_dataframe, output_file)

            # Read back the converted file for post-validation
            converted_dataframe = common.read_data(output_file)

            # Hash the converted DataFrame
            converted_hash = hash_dataframe(converted_dataframe)

            # Compare hashes to check for data integrity
            if original_hash != converted_hash:
                os.remove(output_file)
                raise ValueError("Data integrity check failed: The data has changed during conversion.")

            common.log_message(f"Updated file saved as '{output_format}'", level='info')
            common.display_message(f"File successfully converted to {output_format}.", status="success")
        else:
            raise ValueError("Invalid format choice.")
    except Exception as e:
        raise e
