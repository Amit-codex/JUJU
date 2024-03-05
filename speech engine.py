from datetime import datetime
import pyttsx3
from decouple import config
import speech_recognition as sr

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
    except Exception as e:
        print(e)
        print("Could not understand audio")
        return "None"
    return query

def greet_user():
    """Greets the user according to the time"""
    hour = datetime.now().hour
    if 6 <= hour < 12:
        speak(f"Good Morning {USERNAME}")
    elif 12 <= hour < 16:
        speak(f"Good Afternoon {USERNAME}")
    elif 16 <= hour < 19:
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")
    
if __name__ == "__main__":
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 190)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    greet_user()
    
    while True:
        query = take_command().lower()
        
        # Add conditions for different commands or tasks
        
        # Example: If the user says "open Google", you can define a function to open a web browser with Google.
        if 'open google' in query:
            speak("Opening Google")
            # Function to open Google here
        
        # You can define other commands or tasks similarly
        
        elif 'exit' in query:
            speak(f"Goodbye {USERNAME}. Have a great day!")
            break
