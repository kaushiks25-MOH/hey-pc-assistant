# task_automation.py

import os

def open_file(file_path):
    # Task: Open a file with improved path handling
    try:
        # Normalize the file path to handle incomplete inputs
        normalized_path = os.path.normpath(file_path)
        
        # If path is too short or invalid, provide feedback
        if len(normalized_path) < 2:
            print(f"Invalid file path: '{file_path}' is too short or incomplete.")
            return False
        
        # Check if the file or directory exists
        if not os.path.exists(normalized_path):
            print(f"File or directory not found: {normalized_path}")
            return False
        
        os.startfile(normalized_path)
        print(f"Opening {normalized_path}")
        return True
    except Exception as e:
        print(f"Error opening file: {e}")
        return False

def open_file_manager():
    # Task: Open Windows File Explorer at C:\
    try:
        os.startfile("C:\\")
        print("Opening File Manager at C:\\")
        return True
    except Exception as e:
        print(f"Error opening file manager: {e}")
        return False

def check_weather():
    print("Checking weather...")
    # This would typically involve an API call to a weather service.