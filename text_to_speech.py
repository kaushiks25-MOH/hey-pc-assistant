# text_to_speech.py

import pyttsx3

def speak(text):
    # Text-to-Speech
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    print(f"Assistant: {text}")