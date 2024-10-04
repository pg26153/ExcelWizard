#file_search_gui.py

import os
import common_code_gui as common
from concurrent.futures import ThreadPoolExecutor, as_completed
from tkinter import Toplevel, Label
import time
import threading

def search_file_in_directory(filename, search_path):
    """Search for a file in a given directory."""
    found_files = []
    try:
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                found_files.append(os.path.join(root, filename))
    except Exception as e:
        raise ValueError(f"Error searching in {search_path}: {str(e)}")
    return found_files

def get_accessible_drives():
    """Get a list of accessible drives based on the OS."""
    if os.name == 'nt':  # Windows
        drives = []
        for drive in range(65, 91):  # A: to Z:
            drive_letter = f"{chr(drive)}:\\"
            if os.path.exists(drive_letter):
                drives.append(drive_letter)
        return drives
    else:  # Unix-like systems 
        return ["/"] + [os.path.join("/mnt", d) for d in os.listdir("/mnt") if os.path.isdir(os.path.join("/mnt", d))]

def file_search_in_drives(filename,label):
    """Search for the file in all accessible drives using multiple threads."""
    found_files = []
    drives = get_accessible_drives()

    common.log_message(f"Detected drives: {drives}")

    with ThreadPoolExecutor(max_workers=len(drives)) as executor:
        futures = {executor.submit(search_file_in_directory, filename, drive): drive for drive in drives}

        for future in as_completed(futures):
            drive = futures[future]
            try:
                results = future.result()  # Get results from the completed thread
                found_files.extend(results)  # Collect found files
            except Exception as e:
                raise ValueError(f"Error searching in drive: {futures[future]} - {str(e)}")
            finally:
                # Update the label with completion message for the specific drive
                label.config(text=f"Completed search in: {drive}")  # Update user feedback                

    return found_files

def loading_animation(label, stop_event):
    """Animate the loading label with a text-based hourglass."""
    hourglass_frames = ["⧖", "⧗", "⧕", "⧔"]  # Hourglass symbols
    while not stop_event.is_set():
        for frame in hourglass_frames:
            if stop_event.is_set():
                break  # Exit if stop_event is set
            label.config(text=f"Searching for files {frame}")
            label.update()
            time.sleep(0.5)  # Adjust the speed of the spinner


def show_loading_screen():
    """Display a loading screen while the search is in progress."""
    loading_window = Toplevel()
    loading_window.title("Searching...")
    loading_window.geometry("300x100")
    loading_window.resizable(False, False)

    # Center the loading window
    screen_width = loading_window.winfo_screenwidth()
    screen_height = loading_window.winfo_screenheight()
    x = (screen_width // 2) - (300 // 2)
    y = (screen_height // 2) - (100 // 2)
    loading_window.geometry(f"300x100+{x}+{y}")

    # Set a background color
    loading_window.configure(bg="#f0f0f0")

    # Create a label for the loading spinner
    label = Label(loading_window, text="Searching for files", bg="#f0f0f0", font=("Helvetica", 14))
    label.pack(pady=20)

    return loading_window, label

def search_file(filename):
    """Main function to initiate the search and display results."""
    loading_window = None
    stop_event = threading.Event()

    def complete_search(found_files):
        """Handle the completion of the search."""
        stop_event.set()  # Stop the loading animation
        loading_window.destroy()  # Close loading screen

        # Log and display the found files
        try:
            if found_files:
                common.log_message(f"Found files:\n" + "\n".join(found_files))
                common.display_message("Found files:\n" + "\n".join(found_files), status="info")
            else:
                raise ValueError("No files found.")
        except Exception as e:
            raise e
        
    try:
        common.log_message(f"Starting search for file: {filename}")

        loading_window, label = show_loading_screen()
        loading_window.update()  # Update the loading screen immediately

        # Start the loading animation in a separate thread
        animation_thread = threading.Thread(target=loading_animation, args=(label, stop_event))
        animation_thread.start()

        # Perform the file search in a separate thread
        def run_file_search():
            try:
                found_files = file_search_in_drives(filename, label)  # Pass label for user feedback
                complete_search(found_files)
            except Exception as e:
                raise e

        search_thread = threading.Thread(target=run_file_search)
        search_thread.start()

    except Exception as e:
        if loading_window:  # Close loading screen if it exists
            loading_window.destroy()
        raise e