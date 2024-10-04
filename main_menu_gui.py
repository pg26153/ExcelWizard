#main_menu_gui.py

import tkinter as tk
from tkinter import simpledialog, messagebox
import common_code_gui as common
from compare_update_gui import compare_and_update
from file_format_conv_gui import file_format_conversion_ops
from file_search_gui import search_file
from sample_file_gen_gui import generate_dummy_data,save_to_file
import logging
from datetime import datetime
import os

# Create a directory for logs if it doesn't exist
log_dir = 'log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Generate a timestamped log file name
log_file_name = f"application_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_file_path = os.path.join(log_dir, log_file_name)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Function for "File Compare and Update"
def file_compare_update():
    try:
        file1, message1 = common.open_file_dialog("Select First Excel or CSV File")
        if not file1:
            raise ValueError(message1)
        
        file2, message2 = common.open_file_dialog("Select Second Excel or CSV File")
        if not file2:
            raise ValueError(message2)
        
        key_column = common.simple_input_dialog("Input", "Enter the key column name:")
        if not key_column:
            raise ValueError("No key column provided")

        if file1 == file2:
            raise ValueError("Cannot select Same file again")
        
        # Ask user for confirmation to update the first file
        if messagebox.askyesno("Confirmation", f"Do you want to update '{file1}' with changes from '{file2}'?"):
            output_file, message3 = common.save_file_dialog("Save Updated File As")
            if not output_file:
                raise ValueError(message3)
            
            # Call the compare_and_update function
            compare_and_update(file1, file2, key_column, output_file)

    except Exception as e:
        common.handle_exception(e)

# Function for "File Search"
def file_search():
    try:
        filename = common.simple_input_dialog("Input", "Enter the filename to search for (with extension):")
        if filename:
            search_file(filename)  # Call the search function from the search module
        else:
            raise ValueError("Filename cannot be empty.")

    except Exception as e:
        common.handle_exception(e)

# Function for "File Format Conversion"
def file_format_conversion():
    try:
        file_format_conversion_ops()
    except Exception as e:
        common.handle_exception(e)

# Function for "Sample File Generation"
def sample_file_generation():
    """Main function to execute the dummy data generation process."""
    try:
        num_columns = int(common.simple_input_dialog("Input", "Enter the number of columns:"))
        num_rows = int(common.simple_input_dialog("Input", "Enter the number of rows:"))
        column_info = {}

        for i in range(num_columns):
            column_name = common.simple_input_dialog("Input", f"Enter the name for Column {i + 1}:")
            data_type = common.simple_input_dialog(f"Input", f"Enter the data type for '{column_name}' (Name, Age, Email, Text, or Other):")
            column_info[column_name] = data_type

        # Generate dummy data
        dummy_data_df = generate_dummy_data(num_rows, column_info)

        # Save the generated data to a file
        save_to_file(dummy_data_df)

    except Exception as e:
        common.handle_exception(e)

# Main Menu GUI
def main_menu():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("400x300")
    
    # Center the window
    window_width = 500
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a frame for buttons
    frame = tk.Frame(root)
    frame.pack(expand=True)

    def quit_app():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.quit()

    # Add buttons for each operation with styling
    buttons = [
        ("File Compare and Update", file_compare_update),
        ("File Search", file_search),
        ("File Format Conversion", file_format_conversion),
        ("Sample File Generation", sample_file_generation),
        ("Quit", quit_app),
    ]

    for (text, command) in buttons:
        button = tk.Button(frame, text=text, command=command, width=25, height=2)
        button.pack(pady=10, padx=10)

    # Style the buttons
    for button in frame.winfo_children():
        button.config(bg="lightblue", fg="black", font=("Arial", 12))

    root.mainloop()

if __name__ == "__main__":
    main_menu()
