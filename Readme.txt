Excel Operations Program
1. Project Overview
The Excel Operations Program is a graphical user interface (GUI) application built with Python and Tkinter. It is designed to help users perform common Excel and CSV file operations, including:

Comparing and updating files based on a key column.
Searching for files within the local directory.
Converting files between CSV and Excel formats.
Generating sample files with user-defined data.
This program focuses on streamlining the process of comparing and updating datasets, ensuring data consistency between files. It is especially useful for users working with large datasets in Excel or CSV formats.

2. Features Overview
2.1 File Compare and Update
This feature allows users to compare two files (Excel or CSV) and update one based on the content of the other. The comparison is done based on a key column (e.g., ID or unique identifier). The user can choose how to handle discrepancies such as extra columns, missing rows, or new columns in the second file. After the comparison and update, the updated file is saved.

Key features:

Compare two files based on a key column (e.g., "ID").
Handle missing rows in the first file (keep or set to NA).
Handle new columns from the second file (include or skip).
Handle extra columns in the first file (keep, remove, or fill with NA).
Save the updated file in the desired location (CSV or Excel).
2.2 File Search
This feature allows users to search for a specific file by name within the local directory. The user simply enters the filename, and the program will display the results for easy navigation.

2.3 File Format Conversion
The program enables the conversion of files between CSV and Excel formats. Data integrity is ensured through a hash check before and after the conversion to verify that no changes occurred during the process.

Key features:

Select an input file (CSV or Excel) to convert.
Choose the desired output format (CSV or Excel).
Save the converted file to a user-defined location.
Perform a data integrity check to ensure the content remains unchanged after conversion.
2.4 Sample File Generation
This feature allows users to generate sample files based on user input. Users can specify the number of rows, columns, and data types (e.g., text, numbers, or emails) for the generated data.

3. Project Structure
graphql
Copy code
/Excel_ops
    ├── main_menu_gui.py            # Main GUI and program logic
    ├── compare_update_gui.py       # File comparison and update logic
    ├── file_search_gui.py          # File search logic
    ├── file_format_conv_gui.py     # File format conversion logic
    ├── sample_file_gen_gui.py      # Sample file generation logic
    └── common_code_gui.py          # Common functions/utilities
4. File Compare and Update Feature
4.1 Steps for Comparing and Updating Files:
Select Two Files for Comparison:
The user selects the first and second files via a file dialog. These can be in CSV or Excel format.

Provide a Key Column for Comparison:
The user is prompted to provide the name of the key column (e.g., "ID") that will be used to match rows between the two files.

Comparison Process:
The program compares the files based on the key column and identifies discrepancies:

Missing rows in the first file.
New columns in the second file.
Extra columns in the first file that are not in the second file.
User Options for Handling Data:

Extra Columns in the First File: Choose to either keep, remove, or fill extra columns with "NA".
New Columns from the Second File: Decide whether to include the new columns or skip them.
Missing Rows in the First File: Handle missing rows by keeping them or setting them to "NA".
Save the Updated File:
After making the necessary updates, the user can save the updated file in CSV or Excel format to a location of their choice.

4.2 Example Workflow:
File 1 (file1.csv): Contains employee data with columns "ID", "Name", and "Age".
File 2 (file2.csv): Contains similar data but includes an extra column "Email" and some missing rows.
Steps:

Select file1.csv as the first file and file2.csv as the second file.
Specify "ID" as the key column for comparison.
The application identifies the new "Email" column in file2.csv and missing rows in file1.csv.
The user opts to:
Keep the extra columns in file1.csv.
Include the new "Email" column from file2.csv.
Set missing rows in file1.csv to "NA".
Save the updated file1.csv to the specified location, now including the updated data.
5. Functional Requirements for File Compare and Update
File Selection: Users must be able to select the files to compare via a file dialog.
Key Column Input: The user must provide a valid key column for comparison.
Handling Data Changes: The system should allow the user to choose how to handle extra columns, missing rows, and new columns.
Saving the Updated File: The user must be able to select the location to save the updated file in either CSV or Excel format.
6. Error Handling and Logging
The application handles errors gracefully by catching exceptions and displaying user-friendly messages. Common issues such as invalid file paths, missing key columns, or unsupported file formats are logged and displayed for easy resolution.

Error Logging: All user actions, including errors and file modifications, are logged in a timestamped log file.
File Modifications: If any discrepancies or issues occur during file comparison or conversion, detailed logs are maintained for reference.
7. Assumptions and Constraints
Assumptions:
The user has basic knowledge of Excel and CSV file formats.
The files being compared contain at least one common key column for matching rows.
Constraints:
The program currently supports only CSV and Excel file formats for comparison and conversion.
A valid key column must be provided for comparison.
8. Getting Started
8.1 Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/excel-operations.git
8.2 Install Dependencies:
Make sure Python 3.x and the required libraries are installed. Run the following command to install the dependencies:

bash
Copy code
pip install pandas openpyxl
8.3 Run the Application:
To start the application, run the following command:

bash
Copy code
python main_menu_gui.py
This will open the main menu where you can choose from the available operations (File Compare and Update, File Search, File Format Conversion, Sample File Generation).

