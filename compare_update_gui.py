#compare_update_gui.py

import pandas as pd
import common_code_gui as common
import os
def compare_and_update(file1_path, file2_path, key_column, output_file_path):
    try:
        common.log_message(f"Starting update of '{file1_path}' based on '{file2_path}' using key column '{key_column}'")
        
        # Read the input files
        df1 = common.read_data(file1_path)
        df2 = common.read_data(file2_path)

        # Ensure key_column exists in both dataframes
        if key_column not in df1.columns:
            raise ValueError(f"Key column '{key_column}' not found in the first file.")

        if key_column not in df2.columns:
            raise ValueError(f"Key column '{key_column}' not found in the second file.")

        # Handle extra columns in df1
        extra_columns_file1 = set(df1.columns) - set(df2.columns)
        if extra_columns_file1:
            user_choice = common.simple_input_dialog(
                "Extra Columns in File 1",
                f"The following extra columns are in '{os.path.basename(file1_path)}' : \n\n{', '.join(extra_columns_file1)}.\n\n"
                "Do you want to:\n"
                "1. Remove these columns\n"
                "2. Keep these columns and fill with NA\n"
                "3. Keep these columns without any change\n\n"
                "Please type 'remove', 'fill', or 'keep':"
            )

            if user_choice.lower() == 'remove':
                df1.drop(columns=extra_columns_file1, inplace=True)
                common.log_message("Removed extra columns from the first file.", level='info')
            elif user_choice.lower() == 'fill':
                for col in extra_columns_file1:
                    df1[col].fillna("NA", inplace=True)
                common.log_message("Filled extra columns in the first file with 'NA'.", level='info')
            elif user_choice.lower() == 'keep':
                common.log_message("Kept extra columns in the first file without change.", level='info')
            else:
                raise ValueError(f"Invalid choice. Operation canceled.")


        # Update existing rows in df1 with values from df2 based on the key column
        for col in df2.columns:
            if col != key_column and col in df1.columns:
                df1[col].update(df2.set_index(key_column)[col])
        
        # Handle new columns in df2
        new_columns = set(df2.columns) - set(df1.columns)
        if new_columns:
            user_choice = common.simple_input_dialog(
                "New Columns from File 2",
                f"The following new columns are in '{os.path.basename(file2_path)}' : \n\n{', '.join(new_columns)}.\n\n"
                "Do you want to include these columns in the first file? (Type 'yes' to include or 'no' to skip):"
            )
            if user_choice and user_choice.lower() == 'yes':
                for col in new_columns:
                    df1[col] = df2.set_index(key_column)[col]  # Add new column values
                common.log_message("Included new columns from the second file.", level='info')
            elif user_choice.lower() == 'no':
                common.log_message("Skipped new columns from the second file.", level='info')
            else:
                raise ValueError(f"Invalid choice. Operation canceled.")    

        # Check for new rows in df2 that are not in df1
        new_rows = df2[~df2[key_column].isin(df1[key_column])]
        if not new_rows.empty:
            user_choice = common.simple_input_dialog(
                "New Rows from File 2",
                f"There are new rows in '{os.path.basename(file2_path)}' not present in '{os.path.basename(file1_path)}'.\n\n"
                f"Do you want to add these new rows to the '{os.path.basename(file1_path)}'? (Type 'yes' to include or 'no' to skip):"
            )
            if user_choice and user_choice.lower() == 'yes':
                df1 = pd.concat([df1, new_rows], ignore_index=True)
                common.log_message("Included new rows from the second file.", level='info')
            elif user_choice.lower() == 'no':
                common.log_message("Skipped new rows from the second file.", level='info')
            else:
                raise ValueError(f"Invalid choice. Operation canceled.")

        # Check for missing rows in df2 that are in df1
        missing_rows = df1[~df1[key_column].isin(df2[key_column])]
        if not missing_rows.empty:
            user_choice = common.simple_input_dialog(
                "Missing Rows in File 2",
                f"The following rows are in '{os.path.basename(file1_path)}' but not in '{os.path.basename(file2_path)}' :\n\n"
                f"{missing_rows[key_column].tolist()}.\n\n"
                "Do you want to:\n"
                "1. Keep these rows as is\n"
                "2. Set the values in these rows to NA\n\n"
                "Please type 'keep' or 'Set':"
            )

            if user_choice.lower() == 'set':
                for col in df1.columns:
                    if col != key_column:
                        df1.loc[missing_rows.index, col] = "NA"
                common.log_message("Set missing rows to 'NA' in the first file.", level='info')
            elif user_choice.lower() == 'keep':
                common.log_message("Kept missing rows in the first file as is.", level='info')
            else:
                raise ValueError(f"Invalid choice. Operation canceled.")


        # Save the updated DataFrame to the output file
        common.save_merged_file(df1, output_file_path)
        common.log_message(f"Updated file saved as '{output_file_path}'", level='info')
        common.display_message(f"Updated file saved as '{output_file_path}'.", status="success")

    except Exception as e:
        raise e
