# assistant.py

# Entry point for Hey PC Assistant
from wake_word import detect_wake_word
from voice_recognition import recognize_voice
from nlp_processing import route_command
from text_to_speech import speak

def main():
    print("Hey PC Assistant is running...")
    while True:
        if detect_wake_word():
            speak("Yes, how can I help you?")
            command = recognize_voice()
            route_command(command)

if __name__ == "__main__":
    main()