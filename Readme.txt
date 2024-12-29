Excel Operations Program
1. Project Overview
The Excel Operations Program provides a graphical user interface (GUI) built with Python and Tkinter. It enables users to easily manage Excel and CSV files by performing common operations such as:

Comparing and updating files based on a key column.
Searching files within the local directory.
Converting file formats between CSV and Excel.
Generating sample files with user-defined data.
The primary focus of this application is to streamline the comparison and update process between two files, making it easy for users to ensure consistency between datasets.

2. Features Overview
2.1 File Compare and Update
The application enables users to compare two files (Excel or CSV) and update one of them based on the content of the other. The key aspects of this feature include:

Compare two files based on a key column (e.g., ID or unique identifier).
Update the first file with data from the second file, including handling missing rows, new columns, and extra columns.
User-defined actions to:
Remove or keep extra columns in the first file.
Include or skip new columns from the second file.
Handle missing rows in the first file (either keep them or set to NA).
Save the updated file to a user-defined location.
2.2 File Search
Users can search for a file by its name in the local directory. The results of the search are displayed for easy navigation.

2.3 File Format Conversion
Users can convert files between CSV and Excel formats with a simple dialog for selecting the desired format.

2.4 Sample File Generation
This feature allows users to generate a sample file based on their input, specifying the number of rows, columns, and data types (e.g., text, number, email).

3. Project Structure

/Excel_ops
    ├── main_menu_gui.py            # Main GUI and program logic
    ├── compare_update_gui.py       # File comparison and update logic
    ├── file_search_gui.py          # File search logic
    ├── file_format_conv_gui.py     # File format conversion logic
    ├── sample_file_gen_gui.py      # Sample file generation logic
    └── common_code_gui.py          # Common functions/utilities

4. File Compare and Update Feature
The File Compare and Update feature allows users to compare two files (Excel or CSV) based on a key column, and then update the first file with information from the second. Below is a detailed breakdown of the functionality:

4.1 Steps for Comparing and Updating Files:
Select Two Files for Comparison:

The user selects the first and second files via a file dialog. These can be in CSV or Excel format.
Provide a Key Column for Comparison:

The user is prompted to provide the name of the key column that will be used to match rows between the two files (e.g., "ID").
Comparison Process:

The program compares the files based on the key column:
It identifies missing rows in the first file.
It detects new columns in the second file.
It identifies extra columns in the first file that are not in the second file.
User Options for Handling Data:

Extra Columns in the First File:
The user can choose to either:
Keep the extra columns.
Remove the extra columns.
Fill extra columns with NA (Not Available).
New Columns from the Second File:
The user can decide whether to include the new columns in the first file or skip them.
Missing Rows in the First File:
The user can select how to handle missing rows:
Keep the missing rows as they are.
Set missing rows to NA.
Save the Updated File:

After the comparison and update process is completed, the user can save the updated file to a location of their choice.
The application supports saving in both CSV and Excel formats.
4.2 Example Workflow:
File 1 (file1.csv): Contains employee data with columns "ID", "Name", "Age".
File 2 (file2.csv): Contains similar data but includes an extra column "Email" and some missing rows.
Steps:
The user selects file1.csv as the first file and file2.csv as the second file.
The user specifies "ID" as the key column for comparison.
The application identifies that file2.csv contains a new column ("Email") and some missing rows.
The user opts to:
Keep the extra columns in file1.csv.
Include the new "Email" column from file2.csv.
Set the missing rows in file1.csv to NA.
The updated file1.csv is saved to the specified location, now including the updated data.


5. Functional Requirements for File Compare and Update
File Selection:
Users must be able to select the files to compare via a file dialog.
Key Column Input:
The user must specify the key column for comparison.
Handling Data Changes:
The system should handle extra columns, missing rows, and new columns by offering user-defined options (e.g., remove, keep, fill with NA).
Saving the Updated File:
The user must be able to select the location to save the updated file.


6. Error Handling and Logging
The application ensures smooth user experience by handling errors gracefully. If there are issues such as:

Invalid file paths.
Missing key columns.
Unsupported file formats.
These will be caught, logged, and a user-friendly message will be displayed. All user actions, including errors and file modifications, are logged in a log file for future reference.



7. Assumptions and Constraints
Assumptions:
The user has basic knowledge of Excel and CSV file formats.
The files being compared contain at least one common key column.
Constraints:
The system supports only CSV and Excel files for comparison.
The user must provide a valid key column for comparison.



8. Getting Started
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/excel-operations.git
Install Dependencies: Make sure Python 3.x and the required libraries are installed.

bash
Copy code
pip install pandas openpyxl
Run the Application:

bash
Copy code
python main_menu_gui.py


