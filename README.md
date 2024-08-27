# ExcelWizard
This project provides a set of Python utilities for managing and manipulating Excel and CSV files using the pandas library. It includes functions to generate, modify, convert, and compare Excel and CSV files.

Overview :

This Python script provides functionality to manage Excel and CSV files, including:

1. Generating Excel Files:
   - Create an Excel file with practice data.
   - Generate an Excel file based on user input.

2. Modifying Existing Files:
   - Modify an existing Excel or CSV file by adding/deleting columns or rows.

3. File Conversion:
   - Convert between CSV and Excel formats while maintaining data integrity.

4. Comparing and Updating Files:
   - Compare two files (CSV or Excel) and update the first file based on differences with the second.

Requirements :

- Python 3.x: Ensure you have Python 3 installed on your system.
- pandas: Install pandas using `pip install pandas`.
- openpyxl: For Excel file support, install openpyxl using `pip install openpyxl`.

Usage :

Run the script from the command line using: python your_script_name.py

Menu Options :

1. Generate a new Excel file with practice data:
   - Creates an Excel file with sample data based on user-provided dimensions (number of rows and columns).
   - Optionally converts the Excel file to CSV format.

2. Generate a new Excel file with user input:
   - Creates an Excel file with user-defined values for each cell.
   - Allows specifying default values or manual input for each cell.

3. Modify an existing Excel file:
   - Allows adding or deleting columns and rows in an existing Excel or CSV file.
   - Supports manual input for new values or default values.

4. Compare two Excel files and update the first one:
   - Compares two files based on a key column.
   - Updates the first file with data from the second file, adds new columns, and handles unmatched rows.

Function Descriptions :

1. validate_name(name) : Checks if a file name is valid for Excel files. Ensures the name has:
- Exactly one dot.
- A valid extension (.csv or .xlsx).
- No invalid characters or reserved names.

2. convert_to_excel(input_filename, output_filename) : Converts a CSV file to an Excel file. Performs a data integrity check before renaming the temporary file.

3. convert_from_excel(input_filename, output_filename) : Converts an Excel file to a CSV file. Performs a data integrity check before renaming the temporary file.

4. check_data_integrity(original_file, converted_file) : Compares the data in the original file with the converted file to ensure integrity.

5. generate_excel_with_practice_data() : Generates an Excel file with practice data based on user input and optionally converts it to CSV.

6. generate_excel() : Generates an Excel file based on user input for data entry. Supports default values and manual input.

7. modify_excel() : Modifies an existing Excel or CSV file by adding or deleting columns and rows. Handles user inputs for changes.

8. compare_and_update_excel() : Compares two files and updates the first file based on the second file. Handles unmatched rows with options to delete or replace with 'NA'.

Notes :

- Temporary files created during conversions and modifications are automatically deleted after use.
- Ensure that input filenames match the expected formats (CSV or Excel).
- The script handles common errors and provides informative messages for troubleshooting.
