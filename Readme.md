File Operations Tool

This project provides a suite of tools for manipulating and managing data in CSV and Excel files, allowing for tasks like searching, comparing, updating, and format conversion. The tools come with a user-friendly graphical user interface (GUI) built using Tkinter for easy interaction.
Features

File Search (file_search_gui.py)

•	Micro-Threading Search: The tool uses a micro-threading concept to speed up the search process. This allows for faster file searches compared to traditional computer search methods. Multiple threads are run simultaneously, reducing the overall time it takes to find a file across all available drives.

•	Search Across Multiple Drives: Enables searching for a file across all accessible drives, ensuring that no files are missed.

•	Progress Bar & Loading Animation: Displays a progress bar to visualize the search process, making it easier for users to track the progress.

File Comparison & Update (compare_update_gui.py)

•	Automated Comparison: The tool automatically compares two files based on a chosen key column, saving time and effort. There's no need to manually compare rows and columns— the program handles all of it.

•	No Human Error: The program eliminates human error by ensuring the files are updated automatically. You no longer need to worry about incorrectly updating values or missing rows and columns.

•	High Satisfaction Rate: With built-in logic for handling extra columns, new columns, missing rows, and more, the program ensures a smooth and accurate update process with minimal intervention required.

File Format Conversion (file_format_conv_gui.py)

•	Seamless File Format Conversion: Easily convert between CSV and Excel file formats. This tool ensures that data is correctly transferred and formatted when changing between the two formats.

•	Data Integrity Check: Before and after conversion, the tool checks for data integrity using hash comparisons, ensuring that no data is lost or changed during the process.

•	Flexible and User-Friendly: Allows you to convert files quickly and easily while providing peace of mind that the data is intact.

File Generation (common_code_gui.py)
•	Simple File Generation: The tool allows users to generate new files based on the data provided. Whether you’re merging data, updating files, or simply creating new ones, the tool makes the process easy and efficient.
•	Prevents Manual Errors: The tool handles the creation and formatting of files without requiring manual intervention, ensuring that no formatting errors or inconsistencies occur.
•	Save to Desired Location and Format: Users can choose to save files in their preferred format (CSV or Excel) and location, providing flexibility and convenience in managing files.


How to Use

1. File Search Tool
    •	Step 1: Select the "File Search" option from the main menu.
    •	Step 2: Enter the name of the file you want to search for.
    •	Step 3: The tool will search for the file on all accessible drives using micro-threading to speed up the search process.
    •	Step 4: A progress bar will be displayed, and the results will be shown once the search is complete.
________________________________________
2. File Comparison and Update Tool
    •	Step 1: Select the "File Comparison & Update" option from the main menu.
    •	Step 2: Select two files (File 1 and File 2) to compare.
    •	Step 3: Choose the key column to perform the comparison.
    •	Step 4: The tool will:
        o	Compare the rows based on the key column.
        o	Automatically handle extra columns, new columns, and missing rows.
        o	Prompt you to add new rows or set missing rows to NA in File 1.
    •	Step 5: Save the updated file to your desired location.
________________________________________
3. File Format Conversion Tool
    •	Step 1: Select the "File Format Conversion" option from the main menu.
    •	Step 2: Choose the file you want to convert (CSV or Excel).
    •	Step 3: Select the desired output file format (CSV or Excel).
    •	Step 4: The tool will:
        o	Convert the file to the specified format.
        o	Ensure data integrity through hash comparison.
        o	Delete the converted file and raise an error if data integrity fails.
    •	Step 5: The converted file will be saved to your desired location.
________________________________________
4. File Search Tool
    •	Step 1: Select the "File Search" option from the main menu.

    •	Step 2: Enter the keyword or phrase you want to search within the file.

    •	Step 3: The tool will:
        o	Perform a fast search using a micro-threading approach, which speeds up the process compared to regular computer search algorithms.
        o	Display search results with matched keywords and file locations.
    •	Step 4: You can select the result to view the content containing the search keyword.

Benefits

File Search
    •	Fast and Efficient: With the use of micro-threading, file searches are faster than traditional methods, allowing users to find files on multiple drives more efficiently.
    •	No Manual Searching: You no longer need to manually search each drive for your file. The program handles the entire process.
    •	Visual Progress: The progress bar and loading animation make it easier to track search progress in real-time.
File Comparison & Update
    •	Automation: Automatically compare files and update them based on a key column— no manual comparison required.
    •	Minimizes Errors: By automating the process, the risk of human error in the update process is greatly reduced.
    •	High Satisfaction Rate: The program ensures that the comparison and update process is accurate and streamlined, ensuring a high satisfaction rate for users.
File Format Conversion
    •   Seamless Conversion: Easily convert between CSV and Excel formats without worrying about data loss or formatting issues.
    •	Data Integrity Check: Ensure that the converted file retains the same data as the original by checking for data integrity using hash comparisons.
    •	Easy to Use: The conversion process is simple and quick, allowing you to focus on the content rather than the technical details.
File Generation
    •	Automatic File Creation: The tool helps generate new files based on your operations (such as merging or updating data).
    •	Custom Save Options: Choose where to save files and in what format, providing flexibility for your workflow.
    •	Prevent Manual Errors: Automatic file creation reduces the risk of formatting errors that could arise from manual processes.

Contribution

Feel free to fork the repository, report issues, or submit pull requests. Contributions are always welcome! When contributing, please ensure:
•	New features are thoroughly tested.
•	Any changes to the codebase are documented.
•	A description of the problem and solution is provided in your pull request.

