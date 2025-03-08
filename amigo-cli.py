# Slash Mark Python Internship (Intermediate: Task 2)

import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import random
import sys

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init("sapi5")  # "sapi5" is used for Windows
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # Set the voice (1 is typically female, 0 is male)

# Global variable to control whether the assistant is running
assistant_running = True

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Amigo, your personal assistant. How can I assist you today?")

def take_command():
    """Listen for a voice command and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Error:", e)
        speak("I didn't catch that. Could you please repeat?")
        return "None"
    return query.lower()

def search_wikipedia(query):
    """Search Wikipedia for the given query and speak the summary."""
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Your search term is ambiguous, please specify more clearly.")
        print(e)
    except wikipedia.exceptions.PageError as e:
        speak("No results found on Wikipedia. Please try another query.")
        print(e)
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")
        print(e)

def open_website(url, website_name):
    """Open a specified website in the default web browser."""
    speak(f"Opening {website_name}.")
    webbrowser.open(url)

def open_application(path, app_name):
    """Open a local application using its file path."""
    try:
        speak(f"Opening {app_name}.")
        os.startfile(path)
    except Exception as e:
        speak(f"Sorry, I could not open {app_name}. Please check the path.")
        print(e)

def play_random_music():
    """Play a random song from a predefined music directory."""
    music_dir = "C:\\Users\\athar\\Music"
    songs = os.listdir(music_dir)
    if songs:
        song = random.choice(songs)
        speak(f"Playing {song}")
        os.startfile(os.path.join(music_dir, song))
    else:
        speak("No music files found in your music directory.")

def check_time():
    """Speak the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")

def exit_assistant():
    """Exit the assistant program with a goodbye message."""
    speak("Goodbye! Have a nice day!")
    sys.exit()

def system_control(command):
    """Perform system operations like shutdown, restart, logout, or lock."""
    if 'logout' in command:
        speak("Logging out from the computer.")
        os.system("shutdown -l")
    elif 'shutdown' in command:
        speak("Shutting down the computer.")
        os.system("shutdown /s /t 1")
    elif 'restart' in command:
        speak("Restarting the computer.")
        os.system("shutdown /r /t 1")
    elif 'lock' in command:
        speak("Locking the computer.")
        os.system("rundll32.exe user32.dll, LockWorkStation")

def listen_for_commands():
    """Continuously listen for commands while the assistant is running."""
    global assistant_running
    while assistant_running:
        query = take_command()

        if query in ["pause", "stop", "exit"]:
            speak("Pausing. Say 'resume' to continue or 'terminate' to exit.")
            print("Assistant paused. Say 'resume' to continue or 'terminate' to exit.")
            while True:
                pause_command = take_command()
                if pause_command == "resume":
                    speak("Resuming.")
                    print("Resuming assistant...")
                    break
                elif pause_command in ["terminate", "exit"]:
                    exit_assistant()
        else:
            process_command(query)

def process_command(query):
    """Process and execute the command based on the user's query."""
    if 'wikipedia' in query:
        speak("What topic would you like to search for?")
        topic = take_command().replace("search", "")
        search_wikipedia(topic)

    elif 'open youtube' in query:
        open_website("https://youtube.com", "YouTube")

    elif 'open google' in query:
        open_website("https://google.com", "Google")

    elif 'open spotify' in query:
        spotify_path = "C:\\Users\\athar\\AppData\\Roaming\\Spotify\\Spotify.exe"
        open_application(spotify_path, "Spotify")
        
    elif 'open chrome' in query:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        open_application(chrome_path, "Chrome")

    elif 'play music' in query:
        play_random_music()

    elif 'time' in query:
        check_time()

    elif 'log out' in query or 'shutdown' in query or 'restart' in query or 'lock' in query:
        system_control(query)

    elif 'who are you' in query or 'what is your name' in query:
        speak("I am Amigo, your virtual assistant created to make your life easier.")

    elif 'goodbye' in query or 'exit' in query:
        exit_assistant()

if __name__ == '__main__':
    greet_user()  # Start by greeting the user
    listen_for_commands()  # Continuously listen for and process user commands
