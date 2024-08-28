import pandas as pd
import os
import string

def validate_name(name):
    """Ensure the file name is valid for Excel files, with exactly one dot.

    Args:
        name (str): The name to validate.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    # Define invalid characters and reserved names
    invalid_chars = set(':/*?"<>|')
    reserved_names = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
                       'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'}
    
    # Validate length constraints
    max_length = 255
    if len(name) > max_length:
        print(f"Invalid name. It should not exceed {max_length} characters.")
        return False

    # Check for invalid characters
    if any(char in invalid_chars for char in name):
        print("Invalid name. It contains invalid characters.")
        return False

    # Ensure the name contains exactly one dot
    if name.count('.') != 1:
        print("Invalid name. It should contain exactly one dot.")
        return False

    # Check if the name has an extension
    if '.' not in name or name.rsplit('.', 1)[-1] == '':
        print("Invalid name. It should have a file extension.")
        return False

    #check if the file extension is csv or xlsx.
    if name.rsplit('.', 1)[-1].lower() not in ('csv','xlsx'):
        print("Invalid name. It should have a valid file extension such as xlsx or csv.")
        return False

    # Check for reserved names (excluding extension)
    base_name = name.split('.')[0]
    if base_name.upper() in reserved_names:
        print("Invalid name. It is a reserved name.")
        return False

    # Check for leading or trailing spaces
    if name != name.strip():
        print("Invalid name. It should not have leading or trailing spaces.")
        return False
    

    return True

def check_and_prompt_file_overwrite(filename):
    """
    Check if the file exists and prompt the user if they want to overwrite it.
    Returns True if the file should be overwritten, False otherwise.
    """
    if os.path.exists(filename):
        overwrite = input(f"The file '{filename}' already exists. Do you want to overwrite it? (yes/no): ").strip().lower()
        return overwrite == 'yes'
    return True

def convert_to_excel(input_filename, output_filename):
    """Convert a CSV file to Excel format."""
    try:
        if input_filename.endswith('.csv'):
            df = pd.read_csv(input_filename)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV file.")
        
        temp_excel_path = 'temp_conversion.xlsx'
        df.to_excel(temp_excel_path, index=False)
        print(f"Temporary Excel file '{os.path.abspath(temp_excel_path)}' created.")

        if check_data_integrity(input_filename, temp_excel_path):
            os.rename(temp_excel_path, output_filename)
            print(f"File '{os.path.abspath(input_filename)}' converted to Excel file '{os.path.abspath(output_filename)}'.")
        else:
            print("Data integrity check failed. Conversion aborted.")
            os.remove(temp_excel_path)
            print(f"Temporary file '{os.path.abspath(temp_excel_path)}' removed.")

    except Exception as e:
        print(f"Failed to convert file '{os.path.abspath(input_filename)}' to Excel format. Error: {e}")
        raise

def convert_from_excel(input_filename, output_filename):
    """Convert an Excel file back to CSV format."""
    try:
        df = pd.read_excel(input_filename)
        temp_csv_path = 'temp_conversion.csv'
        df.to_csv(temp_csv_path, index=False)
        print(f"Temporary CSV file '{os.path.abspath(temp_csv_path)}' created.")
        
        if check_data_integrity(input_filename, temp_csv_path):
            os.rename(temp_csv_path, output_filename)
            print(f"Excel file '{os.path.abspath(input_filename)}' converted to CSV file '{os.path.abspath(output_filename)}'.")
        else:
            print("Data integrity check failed. Conversion aborted.")
            os.remove(temp_csv_path)
            print(f"Temporary file '{os.path.abspath(temp_csv_path)}' removed.")

    except Exception as e:
        print(f"Failed to convert Excel file '{os.path.abspath(input_filename)}' to CSV format. Error: {e}")
        raise

def check_data_integrity(original_file, converted_file):
    """Check if the data in the converted file matches the original file."""
    try:
        original_df = pd.read_csv(original_file) if original_file.endswith('.csv') else pd.read_excel(original_file)
        converted_df = pd.read_csv(converted_file) if converted_file.endswith('.csv') else pd.read_excel(converted_file)
        
        if original_df.equals(converted_df):
            print(f"Data integrity check passed. The file '{os.path.abspath(converted_file)}' matches the original file {os.path.abspath(original_file)}.")
            return True
        else:
            print(f"Data integrity check failed. The file '{os.path.abspath(converted_file)}' does not match the original {os.path.abspath(original_file)}.")
            return False
    except Exception as e:
        print(f"Failed to perform data integrity check. Error: {e}")
        return False

def generate_excel_with_practice_data():
    """Generate an Excel file with practice data based on user inputs."""
    filename = input("Enter the name of the Excel file to generate (e.g., 'data.xlsx') ( Note : Only can generate xlsx file. if you want to convert it to csv file, an option will be provided at the later stage): ")
    if not validate_name(filename):
        return
    
    if check_and_prompt_file_overwrite(filename):
        return
    
    try:
        num_rows = int(input("Enter the number of rows: "))
        num_cols = int(input("Enter the number of columns: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for rows and columns.")
        return

    if num_rows <= 0 or num_cols <= 0:
        print("Number of rows and columns must be positive integers.")
        return

    # Ensure filename ends with .xlsx
    if not filename.lower().endswith('.xlsx'):
        print("Error: The file extension should be '.xlsx'.")
        return
    data = {f'Column{i+1}': [f'SampleData_{i+1}_{j+1}' for j in range(num_rows)] for i in range(num_cols)}
    df = pd.DataFrame(data)


    try:
        print("Generating Excel file...")
        df.to_excel(filename, index=False)
        print(f"Excel file '{os.path.abspath(filename)}' generated successfully.")
    except Exception as e:
        print(f"An error occurred while generating the Excel file: {e}")
        return

    # Ask user if they want a CSV version
    convert_to_csv = input("Do you want to convert the Excel file to CSV format? (yes/no): ").strip().lower()
    if convert_to_csv in {'yes', 'y'}:
        csv_filename = filename.rsplit('.', 1)[0] + '.csv'
        convert_from_excel(filename, csv_filename)
        print(f'Removing {os.path.abspath(filename)} excel file')
        os.remove(filename)
    else:
        print("CSV conversion skipped.")

def generate_excel():
    """Generate an Excel file based on user inputs."""
    filename = input("Enter the name of the Excel file to generate (e.g., 'data.xlsx') ( Note : Only can generate xlsx file. if you want to convert it to csv file, an option will be provided at the later stage): ")
    if not validate_name(filename):
        return
    
    if check_and_prompt_file_overwrite(filename):
        return

    try:
        num_rows = int(input("Enter the number of rows: "))
        num_cols = int(input("Enter the number of columns: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for rows and columns.")
        return

    if num_rows <= 0 or num_cols <= 0:
        print("Number of rows and columns must be positive integers.")
        return
    
    # Ensure filename ends with .xlsx
    if not filename.lower().endswith('.xlsx'):
        print("Error: The file extension should be '.xlsx'.")
        return

    # Initialize an empty DataFrame with user-defined column names
    column_names = []
    for i in range(num_cols):
        col_name = input(f"Enter name for column {i + 1}: ").strip()
        column_names.append(col_name)

    df = pd.DataFrame(index=range(num_rows), columns=column_names)
    
    default_value = pd.NA

    for col in df.columns:
        print(f"\nEntering values for {col}:")
        for i in range(num_rows):
            user_input = input(f"Enter value for {col} (row {i+1}) or press Enter to use default value: ").strip()
            df.at[i, col] = user_input if user_input else default_value


    try:
        print("Generating Excel file...")
        df.to_excel(filename, index=False)
        print(f"Excel file '{os.path.abspath(filename)}' generated successfully.")
    except Exception as e:
        print(f"An error occurred while generating the Excel file: {e}")
        return


    # Ask user if they want a CSV version
    convert_to_csv = input("Do you want to convert the Excel file to CSV format? (yes/no): ").strip().lower()
    if convert_to_csv in {'yes', 'y'}:
        csv_filename = filename.rsplit('.', 1)[0] + '.csv'
        convert_from_excel(filename, csv_filename)
        print(f'Removing {os.path.abspath(filename)} excel file')
        os.remove(filename)
    else:
        print("CSV conversion skipped.")

def modify_excel():
    """Modify an existing file (CSV or Excel) based on user inputs."""
    filename = input("Enter the filename of the file to modify (CSV or Excel): ").strip()
    
    if not validate_name(filename):
        return

    if not os.path.exists(filename):
        print(f"File '{os.path.abspath(filename)}' does not exist.")
        return

    temp_excel_file = "temp_modify.xlsx"
    temp_csv_file = "temp_modify.csv"

    try:
        if filename.endswith('.csv'):
            convert_to_excel(filename, temp_excel_file)
            file_to_modify = temp_excel_file
            output_file = filename
        elif filename.endswith('.xls') or filename.endswith('.xlsx'):
            file_to_modify = filename
            output_file = filename
        else:
            print("Unsupported file format. Please provide a CSV or Excel file.")
            return

        df = pd.read_excel(file_to_modify)
        print("\nExisting columns:", df.columns.tolist())

        if input("Do you want to add new columns? (yes/no): ").strip().lower() == 'yes':
            column_names = [name.strip() for name in input("Enter the names of the new columns, separated by commas: ").strip().split(',')]
            default_values = [value.strip() if value.strip() else pd.NA for value in input("Enter default values for each column, separated by commas (leave blank for manual input): ").strip().split(',')]

            if len(column_names) != len(default_values):
                print("The number of column names must match the number of default values.")
                return

            for col, default in zip(column_names, default_values):
                df[col] = default
                if pd.isna(default):
                    for i in range(len(df)):
                        df.at[i, col] = input(f"Enter value for {col} (row {i+1}): ")

        if input("Do you want to delete columns? (yes/no): ").strip().lower() == 'yes':
            del_col_names = [name.strip() for name in input("Enter the names of the columns to delete, separated by commas: ").strip().split(',')]
            for col in del_col_names:
                if col in df.columns:
                    df.drop(columns=[col], inplace=True)
                    print(f"Column '{col}' deleted from '{os.path.abspath(file_to_modify)}'.")
                else:
                    print(f"Column '{col}' does not exist in '{os.path.abspath(file_to_modify)}'.")

        if input("Do you want to add new rows? (yes/no): ").strip().lower() == 'yes':
            num_new_rows = int(input("Enter the number of new rows to add: "))
            for _ in range(num_new_rows):
                new_row = {col: input(f"Enter value for {col}: ") for col in df.columns}
                df = df.append(new_row, ignore_index=True)
                print(f"New row added to '{os.path.abspath(file_to_modify)}'.")

        if input("Do you want to delete rows? (yes/no): ").strip().lower() == 'yes':
            del_row_indices = [int(index.strip()) for index in input("Enter the indices of the rows to delete, separated by commas: ").strip().split(',')]
            for index in del_row_indices:
                if 0 <= index < len(df):
                    df.drop(index=index, inplace=True)
                    df.reset_index(drop=True, inplace=True)
                    print(f"Row {index} deleted from '{os.path.abspath(file_to_modify)}'.")
                else:
                    print(f"Row index {index} is out of range in '{os.path.abspath(file_to_modify)}'.")

        if filename.endswith('.csv'):
            convert_from_excel(temp_excel_file, temp_csv_file)
            if not check_data_integrity(filename, temp_csv_file):
                print("Data integrity check failed. The CSV file may not be correctly updated.")
            os.remove(temp_excel_file)
            print(f"Temporary file '{os.path.abspath(temp_excel_file)}' removed.")
            os.rename(temp_csv_file, output_file)
            print(f"CSV file '{os.path.abspath(filename)}' updated successfully.")
        else:
            df.to_excel(output_file, index=False)
            print(f"Excel file '{os.path.abspath(filename)}' updated successfully.")

    except Exception as e:
        print(f"Failed to modify file '{os.path.abspath(filename)}'. Error: {e}")
    finally:
        if os.path.exists(temp_excel_file):
            os.remove(temp_excel_file)
            print(f"Temporary file '{os.path.abspath(temp_excel_file)}' removed.")
        if os.path.exists(temp_csv_file):
            os.remove(temp_csv_file)
            print(f"Temporary file '{os.path.abspath(temp_csv_file)}' removed.")

def compare_and_update_excel():
    """Compare two files (CSV or Excel) and update the first one based on the second."""
    file1 = input("Enter the filename of the first file (to update, CSV or Excel): ").strip()
    file2 = input("Enter the filename of the second file (to compare against, CSV or Excel): ").strip()

    if not validate_name(file1) or not validate_name(file2):
        return

    temp_file1_excel = "temp_file1.xlsx"
    temp_file2_excel = "temp_file2.xlsx"

    # Convert files to Excel format if they are not already
    if file1.endswith('.csv'):
        convert_to_excel(file1, temp_file1_excel)
        file1 = temp_file1_excel
    elif not file1.endswith(('.xls', '.xlsx')):
        print("Unsupported file format for the first file. Please provide a CSV or Excel file.")
        return

    if file2.endswith('.csv'):
        convert_to_excel(file2, temp_file2_excel)
        file2 = temp_file2_excel
    elif not file2.endswith(('.xls', '.xlsx')):
        print("Unsupported file format for the second file. Please provide a CSV or Excel file.")
        return

    # Read the files
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Show existing columns
    print("\nColumns in the first file:", df1.columns.tolist())
    print("Columns in the second file:", df2.columns.tolist())

    # Get key column from user
    key_column = input("Enter the key column name (must exist in both files): ")

    if key_column not in df1.columns or key_column not in df2.columns:
        print(f"Column '{key_column}' does not exist in one or both files.")
        return

    print("Comparing files and updating...")

    # Add new columns to df1 if they are in df2
    for column in df2.columns:
        if column not in df1.columns:
            df1[column] = pd.NA
            print(f"Column '{column}' added to '{os.path.abspath(file1)}'.")

    # Update existing rows and add new rows
    for index, row in df2.iterrows():
        key_value = row[key_column]
        if key_value in df1[key_column].values:
            for col in df2.columns:
                if not pd.isna(row[col]):
                    df1.loc[df1[key_column] == key_value, col] = row[col]
            print(f"Row with {key_column} = '{key_value}' updated in '{os.path.abspath(file1)}'.")
        else:
            df1 = df1.append(row, ignore_index=True)
            print(f"Row with {key_column} = '{key_value}' added to '{os.path.abspath(file1)}'.")

    # Handle unmatched rows
    print("\nHow do you want to handle rows in the first file that are not in the second file?")
    print("1. Delete unmatched rows")
    print("2. Replace unmatched rows with 'NA'")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        df1 = df1[df1[key_column].isin(df2[key_column].values)]
        print(f"Rows not present in the second file have been deleted from '{os.path.abspath(file1)}'.")
    elif choice == '2':
        unmatched_rows = ~df1[key_column].isin(df2[key_column].values)
        df1.loc[unmatched_rows, df1.columns] = pd.NA
        print(f"Unmatched rows have been replaced with 'NA' in '{os.path.abspath(file1)}'.")
    else:
        print("Invalid choice. No rows were deleted or replaced.")

    # Save the updated file
    df1.to_excel(file1, index=False)
    print(f"\nFile '{os.path.abspath(file1)}' updated successfully based on differences with '{os.path.abspath(file2)}'.")

    # Remove temporary files if they were created
    if file1 == temp_file1_excel and os.path.exists(temp_file1_excel):
        os.remove(temp_file1_excel)
        print(f"Temporary file '{os.path.abspath(temp_file1_excel)}' removed.")
    if file2 == temp_file2_excel and os.path.exists(temp_file2_excel):
        os.remove(temp_file2_excel)
        print(f"Temporary file '{os.path.abspath(temp_file2_excel)}' removed.")

def main():
    choice = input("What do you want to do?\n1. Generate a new Excel file with practice data\n2. Generate a new Excel file with user input\n3. Modify an existing Excel file\n4. Compare two Excel files and update the first one\nEnter 1, 2, 3, or 4: ")

    if choice == '1':
        generate_excel_with_practice_data()
    elif choice == '2':
        generate_excel()
    elif choice == '3':
        modify_excel()
    elif choice == '4':
        compare_and_update_excel()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
