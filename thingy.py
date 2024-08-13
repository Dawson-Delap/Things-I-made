import shutil
import os
import subprocess
from tkinter import Tk, Label

# Get the path of the current script
current_script_path = os.path.abspath(__file__)
current_script_directory = os.path.dirname(current_script_path)

def get_next_filename(directory, base_name, extension):
    """
    Generate the next filename with an incrementing number.
    """
    i = 1
    while True:
        # Construct a potential filename
        filename = f"{base_name}{i}{extension}"
        file_path = os.path.join(directory, filename)
        
        # Check if the file already exists
        if not os.path.exists(file_path):
            return filename
        
        i += 1

def copy_and_run_script():
    try:
        # Determine the new filename and path in the current script's directory
        base_name = 'banana'
        extension = os.path.splitext(current_script_path)[1]  # Get the current file extension
        new_filename = get_next_filename(current_script_directory, base_name, extension)
        new_path = os.path.join(current_script_directory, new_filename)
        
        # Copy the script to the new path
        shutil.copy(current_script_path, new_path)
        print(f"Script copied to {new_path}")

        # Run the copied script from its new location
        subprocess.Popen(['python', new_path], shell=True)
        print(f"Script {new_path} has been executed.")

    except Exception as e:
        print(f"An error occurred: {e}")

def create_gui():
    """
    Create a Tkinter GUI window.
    """
    root = Tk()
    root.title("Banana")
    root.configure(background="yellow")
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("300x300+50+50")

    # Add a label for demonstration
    label = Label(root, text="This is a Tkinter window", bg="yellow")
    label.pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    # Copy and run the script
    copy_and_run_script()
    
    # Create and run the Tkinter GUI
    create_gui()