import speech_recognition as sr
import pyttsx3

# Initialize recognizer
recognizer = sr.Recognizer()

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Function to check if wake word is present
def check_wake_word(text, wake_word):
    return wake_word.lower() in text.lower()

# Function to respond to wake word
def respond_to_wake_word(wake_word):
    while True:
        user_input = listen()
        if check_wake_word(user_input, wake_word):
            print("Assistant: Yes, how can I help you?")
            speak("Yes, how can I help you?")
            # Add your response logic here
            # For example, you can call another function to handle further commands
            handle_commands()
            break

# Function to handle further commands after wake word is recognized
def handle_commands():
    while True:
        user_input = listen()
        # Add your logic to handle further commands here
        # For example, you can process the user's input and perform actions accordingly
        if "stop" in user_input.lower():
            print("Assistant: Goodbye!")
            speak("Goodbye!")
            break

        elif "how are you" in user_input.lower():
            print("Assistant: I'm doing well, thank you for asking!")
            speak("I'm doing well, thank you for asking!")
        else:
            print("Assistant: I'm still listening. Say something.")
            speak("I'm still listening. Say something.")

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Call the function to respond to the wake word
respond_to_wake_word("Jarvis")
