# nlp_processing.py

from task_automation import open_file, check_weather, open_file_manager
from text_to_speech import speak

def route_command(command):
    # Simplified NLP routing with enhanced command handling
    if not command or command.strip() == "":
        speak("I didn't catch that. Could you please repeat?")
        return
    
    command_lower = command.lower().strip()
    
    # Check for "open file manager" command first (more specific)
    if "open file manager" in command_lower or "file manager" in command_lower:
        speak("Opening File Manager")
        success = open_file_manager()
        if not success:
            speak("Sorry, I couldn't open the file manager.")
    # Check for "open file" or just "open" commands
    elif "open file" in command_lower or "open" in command_lower:
        speak("Which file would you like to open?")
        file_path = input("Enter file path: ")
        
        # Handle incomplete or empty input
        if not file_path or file_path.strip() == "":
            speak("No file path provided. Canceling operation.")
            return
        
        success = open_file(file_path)
        if success:
            speak(f"File opened successfully")
        else:
            speak("Sorry, I couldn't open that file. Please check the path and try again.")
    elif "weather" in command_lower:
        check_weather()
    else:
        speak(f"Sorry, I don't understand the command '{command}'. Please try again with a supported command.")