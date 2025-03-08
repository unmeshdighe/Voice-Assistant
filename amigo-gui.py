# Slash Mark Python Internship (Intermediate: Task 2)

import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import random
import tkinter as tk
from PIL import Image, ImageTk

# Initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # Set the voice (1 is typically female, 0 is male)

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("300x200")

        # Microphone icon setup
        self.mic_image = Image.open("mic_icon.png")  # Ensure this image is in your working directory
        self.mic_image = self.mic_image.resize((50, 50), Image.Resampling.LANCZOS)
        self.mic_photo = ImageTk.PhotoImage(self.mic_image)
        
        self.mic_button = tk.Button(root, image=self.mic_photo, command=self.listen_for_commands)
        self.mic_button.pack(pady=20)
        
        self.status = tk.Label(root, text="Press the microphone to start", font=("Helvetica", 12))
        self.status.pack(pady=10)

        # Set up the exit button
        self.exit_button = tk.Button(root, text="Exit", command=self.exit_assistant)
        self.exit_button.pack(pady=10)

    def speak(self, text):
        """Convert text to speech."""
        engine.say(text)
        engine.runAndWait()
    
    def take_command(self):
        """Listen for a voice command and return it as text."""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.status.config(text="Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            self.status.config(text="Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            return query.lower()
        except Exception as e:
            self.speak("I didn't catch that. Could you please repeat?")
            return "None"

    def process_command(self, query):
        """Process and execute the command based on the user's query."""
        if 'wikipedia' in query:
            self.speak("What topic would you like to search for?")
            topic = self.take_command().replace("search", "")
            self.search_wikipedia(topic)

        elif 'open youtube' in query:
            self.open_website("https://youtube.com", "YouTube")

        elif 'open google' in query:
            self.open_website("https://google.com", "Google")

        elif 'open spotify' in query:
            spotify_path = "C:\\Users\\athar\\AppData\\Roaming\\Spotify\\Spotify.exe"
            self.open_application(spotify_path, "Spotify")
        
        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            self.open_application(chrome_path, "Chrome")

        elif 'play music' in query:
            self.play_random_music()

        elif 'time' in query:
            self.check_time()

        elif 'log out' in query or 'shutdown' in query or 'restart' in query or 'lock' in query:
            self.system_control(query)

        elif 'who are you' in query or 'what is your name' in query:
            self.speak("I am Amigo, your virtual assistant created to make your life easier.")

        elif 'goodbye' in query or 'exit' in query:
            self.exit_assistant()

    def search_wikipedia(self, query):
        """Search Wikipedia for the given query and speak the summary."""
        try:
            results = wikipedia.summary(query, sentences=2)
            self.speak("According to Wikipedia:")
            self.speak(results)
        except wikipedia.exceptions.DisambiguationError:
            self.speak("Your search term is ambiguous, please specify more clearly.")
        except wikipedia.exceptions.PageError:
            self.speak("No results found on Wikipedia. Please try another query.")
        except Exception:
            self.speak("An error occurred while searching Wikipedia.")

    def open_website(self, url, website_name):
        """Open a specified website in the default web browser."""
        self.speak(f"Opening {website_name}.")
        webbrowser.open(url)

    def open_application(self, path, app_name):
        """Open a local application using its file path."""
        try:
            self.speak(f"Opening {app_name}.")
            os.startfile(path)
        except Exception as e:
            self.speak(f"Sorry, I could not open {app_name}. Please check the path.")
    
    def play_random_music(self):
        """Play a random song from a predefined music directory."""
        music_dir = "C:\\Users\\athar\\Music"
        songs = os.listdir(music_dir)
        if songs:
            song = random.choice(songs)
            self.speak(f"Playing {song}")
            os.startfile(os.path.join(music_dir, song))
        else:
            self.speak("No music files found in your music directory.")
    
    def check_time(self):
        """Speak the current time."""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}.")

    def system_control(self, command):
        """Perform system operations like shutdown, restart, logout, or lock."""
        if 'logout' in command:
            self.speak("Logging out from the computer.")
            os.system("shutdown -l")
        elif 'shutdown' in command:
            self.speak("Shutting down the computer.")
            os.system("shutdown /s /t 1")
        elif 'restart' in command:
            self.speak("Restarting the computer.")
            os.system("shutdown /r /t 1")
        elif 'lock' in command:
            self.speak("Locking the computer.")
            os.system("rundll32.exe user32.dll, LockWorkStation")
    
    def listen_for_commands(self):
        """Start listening for commands when the microphone button is pressed."""
        query = self.take_command()
        self.process_command(query)
        self.status.config(text="Press the microphone to start")

    def exit_assistant(self):
        """Exit the assistant program with a goodbye message."""
        self.speak("Goodbye! Have a nice day!")
        self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()
