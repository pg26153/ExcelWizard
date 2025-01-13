# File Operations Tool

Welcome to the **File Operations Tool**—a comprehensive suite designed to streamline your file management tasks. Whether you need to search, compare, update, convert formats, or generate new files, this tool empowers you to perform these actions efficiently with a user-friendly graphical interface built using Tkinter.

##### Working Video : https://github.com/pg26153/ExcelWizard/blob/new_vide/Video.mp4

## 🚀 Features

### 🔍 **File Search (file_search_gui.py)**

- **Supercharged Search**: Leverage micro-threading to boost search speed. This advanced concept runs multiple search threads simultaneously, drastically reducing search time across drives.
  
- **Search Across All Drives**: Seamlessly search for files across multiple accessible drives, ensuring nothing gets left behind.
  
- **Visual Progress**: Track your search with an intuitive progress bar and live-loading animation, keeping you informed every step of the way.

### 🔄 **File Comparison & Update (compare_update_gui.py)**

- **Automated Comparison**: Let the tool automatically compare two files based on a selected key column—no need to manually inspect each row or column.
  
- **Error-Free Updates**: Forget human errors when updating files. The program ensures all discrepancies are handled, guaranteeing accurate and flawless updates.

- **Smooth Handling of Data**: The tool adapts to extra columns, new data, and missing rows, making updates straightforward and hassle-free.

### 🔄 **File Format Conversion (file_format_conv_gui.py)**

- **Seamless Format Conversion**: Convert between CSV and Excel effortlessly, while ensuring that your data remains intact and properly formatted.
  
- **Data Integrity Assurance**: Before and after conversion, a hash comparison is performed to ensure that no data is lost or modified during the process.

- **Easy-to-Use**: The conversion is simple and quick, so you can focus on the data, not the technical details.

### 📝 **File Generation (common_code_gui.py)**

- **Effortless File Creation**: Quickly generate new files by merging or updating data, or even create entirely new datasets based on provided inputs.

- **Eliminate Manual Errors**: Let the tool handle formatting, creation, and structuring of files, ensuring no mistakes in the process.

- **Custom Save Locations**: Choose where and in what format (CSV or Excel) to save your files, giving you complete flexibility over your workflow.

---

## 🧑‍💻 **How to Use**

### 1. **File Search Tool**

1. **Step 1**: Select the *"File Search"* option from the main menu.
2. **Step 2**: Enter the name of the file you’re looking for.
3. **Step 3**: The tool will search across all accessible drives using micro-threading for lightning-fast results.
4. **Step 4**: Track progress with the progress bar, and view the results when the search is completed.

---

### 2. **File Comparison and Update Tool**

1. **Step 1**: Choose the *"File Comparison & Update"* option from the main menu.
2. **Step 2**: Select the two files (File 1 and File 2) you wish to compare.
3. **Step 3**: Pick a key column for comparison.
4. **Step 4**: The tool will:
   - Compare rows based on the key column.
   - Handle extra columns, missing data, and new columns automatically.
   - Prompt you to either add missing rows or set them to *NA* in File 1.
5. **Step 5**: Save the updated file to your desired location.

---

### 3. **File Format Conversion Tool**

1. **Step 1**: Click on the *"File Format Conversion"* option from the main menu.
2. **Step 2**: Select the file you want to convert (either CSV or Excel).
3. **Step 3**: Choose your desired output format (CSV or Excel).
4. **Step 4**: The tool will:
   - Convert the file to the chosen format.
   - Ensure data integrity through hash comparisons.
   - Raise an error if any integrity issues are found.
5. **Step 5**: Save the converted file to your desired location.

---

### 4. **File Generation Tool**

1. **Step 1**: Select the *"File Generation"* option from the main menu.
2. **Step 2**: Provide the data you want to merge or use to create a new file.
3. **Step 3**: The tool will automatically create the new file, handling all formatting and structure.
4. **Step 4**: Choose where and in which format (CSV or Excel) to save the new file.

---

## 🌟 **Benefits**

### **File Search**

- **Fast and Efficient**: Powered by micro-threading, this tool outperforms traditional search methods, helping you find files across multiple drives faster than ever before.
  
- **No Manual Searching**: Say goodbye to manually hunting down files—let the tool do the heavy lifting for you.

- **Real-Time Feedback**: A progress bar keeps you informed of the search’s status.

---

### **File Comparison & Update**

- **Automation at its Best**: No need for manual comparisons. The tool automatically detects discrepancies and updates files based on a key column.
  
- **Reduced Human Error**: Automation minimizes the chances of errors, ensuring accurate updates every time.

- **Seamless Updates**: Handles new data, extra columns, and missing rows with ease, making the update process smoother.

---

### **File Format Conversion**

- **Hassle-Free Conversion**: Easily convert files between CSV and Excel formats without worrying about data loss or misalignment.

- **Guaranteed Data Integrity**: Ensure that the integrity of your data is preserved before and after conversion with hash comparisons.

- **Quick & Easy**: Simple steps to convert your files with peace of mind.

---

### **File Generation**

- **No More Manual Work**: Let the tool generate new files for you—whether merging data, updating existing files, or creating brand new ones.

- **Save Where You Want**: Choose your preferred format (CSV or Excel) and the location to save the generated files.

- **No Errors**: Automatic handling ensures the file is generated without any formatting or structural issues.

---

## 🚀 **Getting Started**

Follow these steps to run the project on your local machine:

### 1. **Clone the Repository**

First, clone the repository to your local machine by running:

Git clone [https://github.com/yourusername/file-operations-tool.git](https://github.com/pg26153/ExcelWizard/tree/main)

### 2. **Create a Virtual Environment**

```bash
python -m venv venv
```
### 3. **Activate the Virtual Environment**

Once the virtual environment is created, activate it:

```bash
.\venv\Scripts\activate
```
### 4. **Install the Dependencies**

Next, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
### 5. **Run the Application**

Once everything is set up, you can run the application:

```bash
python main.py
```
### 🤝 **Contribution**

We welcome contributions from the community! Feel free to fork the repository, submit issues, or create pull requests. When contributing, please ensure:

- **Thorough Testing**: New features should be fully tested before submission.
- **Documentation**: Any code changes should be accompanied by clear documentation.
- **Clear Descriptions**: Provide a detailed explanation of the problem being solved and how your contribution addresses it.

Together, we can make this tool even better! Happy coding! 🚀
