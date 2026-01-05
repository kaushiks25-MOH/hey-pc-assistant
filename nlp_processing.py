# nlp_processing.py

from task_automation import open_file, check_weather
from text_to_speech import speak

def route_command(command):
    # Simplified NLP routing
    if "open file" in command:
        speak("Which file would you like to open?")
        file_path = input("Enter file path: ")
        open_file(file_path)
    elif "weather" in command:
        check_weather()
    else:
        speak("Sorry, I can't handle that command yet.")