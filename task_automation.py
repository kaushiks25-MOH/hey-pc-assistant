# task_automation.py

import os

def open_file(file_path):
    # Task: Open a file
    try:
        os.startfile(file_path)
        print(f"Opening {file_path}")
    except Exception as e:
        print(f"Error opening file: {e}")

def check_weather():
    print("Checking weather...")
    # This would typically involve an API call to a weather service.