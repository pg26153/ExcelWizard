#common_code_gui.py

import pandas as pd
import os
from tkinter import filedialog, Toplevel
import tkinter as tk
from main_menu_gui import logging
import tkinter.font as tkFont

def log_message(message, level='info'):
    """Logs a message with the specified severity level."""
    if level == 'info':
        logging.info(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'debug':
        logging.debug(message)

def handle_exception(e):
    """Handles exceptions by displaying an error message and logging it."""
    error_message = str(e)
    log_message(error_message, level='error')
    display_message(error_message, status="error")
    #sys.exit(1)  # Exit with a non-zero status to indicate an error

def display_message(message, status="info"):
    """Displays a message to the user with a standard message box appearance."""
    title = {
        "success": "Success",
        "fail": "Fail",
        "error": "Error",
        "info": "Information"
    }.get(status, "Information")

    # Create a new Toplevel window for custom message display
    msg_window = Toplevel()
    msg_window.title(title)
    
    # Style the window
    msg_window.configure(bg="white")
    msg_window.resizable(False, False)

    # Create a frame for padding
    frame = tk.Frame(msg_window, padx=20, pady=20, bg="white")
    frame.pack(expand=True)  # Allow the frame to expand and center

    # Create a label for the message with different colors based on status
    msg_color = {
        "success": "green",
        "fail": "red",
        "error": "darkred",
        "info": "blue"
    }.get(status, "black")

    msg_label = tk.Label(frame, text=message, wraplength=300, bg="white", fg=msg_color)
    msg_label.pack(pady=10)  # Center the message vertically

    # Add an OK button to close the message window
    ok_button = tk.Button(frame, text="OK", command=msg_window.destroy, bg="lightgrey")
    ok_button.pack(pady=(10, 0))  # Add some space above the button

    # Center the message window
    msg_window.transient()  # Make the window a "transient" window for the parent
    msg_window.grab_set()   # Grab the focus

    # Calculate center position
    window_width = 400
    window_height = 200
    screen_width = msg_window.winfo_screenwidth()
    screen_height = msg_window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    msg_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Make the window modal
    msg_window.focus_set()  # Set focus to the message box
    msg_window.wait_window()  # Wait for the message box to be closed

def read_data(file_path):
    try:
        if file_path.endswith('.csv'):
            return pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Please select a CSV or Excel file.")
    except Exception as e:
        raise e

def save_merged_file(merged_df, output_file_path):
    """Automatically detects whether the output file is a .csv or .xlsx and handles the file creation."""
    try:
        file_extension = os.path.splitext(output_file_path)[1].lower()

        if file_extension == '.xlsx':
            merged_df.to_excel(output_file_path, index=False)
        elif file_extension == '.csv':
            merged_df.to_csv(output_file_path, index=False)
        else:
            raise ValueError("Unsupported file format. Please use .xlsx or .csv extensions.")
    except Exception as e:
        raise e

def validate_filename(file_path, status=""):
    """Validates the filename for various criteria."""
    # Check for spaces and valid extensions regardless of status
    if ' ' in os.path.basename(file_path):
        return False, "Filename should not contain spaces."
    
    if not file_path.endswith(('.csv', '.xls', '.xlsx')):
        return False, "Invalid file extension. Please use CSV or Excel files."
    
    # If opening a file, check if it exists
    if status != "save_file" and not os.path.exists(file_path):
        return False, "File does not exist."

    return True, ""

def open_file_dialog(title):
    """Open a file dialog to select a file."""
    file_path = filedialog.askopenfilename(title=title)
    if not file_path:
        return False, "No file provided"
    
    is_valid, error_message = validate_filename(file_path)
    if not is_valid:
        return False, error_message
    
    return file_path,""

def save_file_dialog(title):
    """Open a save file dialog to select where to save the file."""

    filetypes = (
        [("xlsx", "*.xlsx"),("Csv", "*.csv")]
    )

    file_path = filedialog.asksaveasfilename(
        title=title,
        initialdir=os.getcwd(),
        initialfile="File1.xlsx",
        defaultextension=".xlsx",
        filetypes=filetypes
    )

    if not file_path:
        return False, "No file provided"
    
    is_valid, error_message = validate_filename(file_path,"save_file")
    if not is_valid:
        return False, error_message
    
    return file_path,""

def simple_input_dialog(title, prompt):
    """Create a stylish Tkinter dialog to get user input."""
    # Create a new top-level window for the input dialog
    dialog = Toplevel()
    dialog.title(title)

    # Create a label to measure text size
    label_font = tkFont.Font(family="Helvetica", size=12)

    # Measure the width and height of the prompt text
    label_width = label_font.measure(prompt)  # Adding some padding
    label_height = label_font.metrics("linespace") * (prompt.count('\n') + 1)  # Height based on lines in prompt

    # Set fixed heights for entry and button
    entry_height = 30  
    button_height = 30  
    padding = 40  # Additional padding

    total_width = min(label_width, 500)

    # Calculate total height required
    total_height = label_height + entry_height + button_height + padding +50

    # Set the geometry of the dialog based on the calculated size
    dialog.geometry(f"{total_width}x{total_height}")

    # Create a frame for padding
    frame = tk.Frame(dialog, padx=20, pady=20)
    frame.pack()

    # Create a label for the prompt with a stylish font
    label = tk.Label(frame, text=prompt, font=("Helvetica", 12), wraplength=total_width - 40)  # Adjusting wraplength
    label.pack(pady=(0, 10))

    # Create an entry widget for user input with a border
    entry = tk.Entry(frame, width=30, font=("Helvetica", 12), bd=2, relief=tk.SUNKEN)
    entry.pack(pady=(0, 10))

    # Variable to hold the result
    result = None

    # Function to handle the OK button click
    def on_ok():
        nonlocal result  # Use the nonlocal variable
        result = entry.get()
        dialog.destroy()  # Close the dialog

    # Add an OK button with styling
    ok_button = tk.Button(frame, text="OK", command=on_ok, font=("Helvetica", 12), bg="#4CAF50", fg="white", bd=0, padx=10, pady=5)
    ok_button.pack()

     # Bind the Enter key to trigger the OK button click
    dialog.bind('<Return>', lambda event: on_ok())  # This binds the Enter key to the on_ok function

    # Center the dialog and set it to always be on top
    dialog.transient()  # Make the window a "transient" window for the parent
    dialog.grab_set()   # Grab the focus
    dialog.geometry("+%d+%d" % (dialog.winfo_screenwidth() // 2 - total_width // 2, dialog.winfo_screenheight() // 2 - total_height // 2))

    # Make the window modal
    dialog.focus_set()  # Set focus to the dialog
    dialog.wait_window()  # Wait for the dialog to be closed

    # Return the result (after dialog is closed)
    return result