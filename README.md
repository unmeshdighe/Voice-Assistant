# Amigo Voice Assistant

This repository contains a Python-based voice assistant application with both a Command-Line Interface (CLI) and a Graphical User Interface (GUI) which I created for Slash Mark Internship Intermediate Task 2 as my project. The assistant can perform various tasks such as searching Wikipedia, opening websites, playing music, and controlling system operations like shutdown, restart, or locking the computer. This code contains two modified versions of the Amigo assistant: a Command-Line Interface (CLI) version and a Graphical User Interface (GUI) version. Both versions provide a range of functionalities to interact with your system using voice commands.

**Note: This code is originally taken from [@jaspreetsidhu3](https://github.com/jaspreetsidhu3/voice_assistant)**

## Features
1. Voice Interaction: Communicate with the assistant using voice commands.
2. Web Search: Search Wikipedia and get summaries.
3. Website and Application Launching: Open websites and local applications.
4. Music Playback: Play random songs from a specified music directory.
5. System Control: Perform system operations such as shutdown, restart, log out, and lock.
6. Time Check: Get the current time.
7. Assistant Controls: Pause, Resume and Terminate the voice assistant as necessary.

# CLI Version
The CLI version of the Amigo assistant provides a text-based interface for interacting with the assistant through the command line.

_**File: [amigo-cli.py](https://github.com/atharva39/Slash-Mark-Python-Intermediate-Tasks/blob/83942719d38b8e4918f691e0bc60372e96518dee/Intermediate-Task-2/amigo-cli.py)**_

## Features:
- Greet the user based on the time of day.
- Execute commands to search Wikipedia, open websites, play music, and control the system.
- Continuous listening with options to pause or exit.

## Usage:
1. Run the script using Python.
2. Speak commands or type them in the terminal.

# GUI Version
The GUI version of the Amigo assistant offers a graphical interface with a microphone button to initiate voice commands.

_**File: [amigo-gui.py](https://github.com/atharva39/Slash-Mark-Python-Intermediate-Tasks/blob/83942719d38b8e4918f691e0bc60372e96518dee/Intermediate-Task-2/amigo-gui.py)**_

## Features:
- Provides a user-friendly graphical interface with a microphone button.
- Includes a status display for ongoing interactions.
- Supports the same functionalities as the CLI version.

## Usage:
1. Ensure [mic_icon.png](https://github.com/atharva39/Slash-Mark-Python-Intermediate-Tasks/blob/83942719d38b8e4918f691e0bc60372e96518dee/Intermediate-Task-2/mic_icon.png) is present in your working directory.
2. Run the script using Python.
3. Click the microphone icon to start listening for commands.

## Installation
Ensure you have Python 3.12 installed on your system.

Install the required Python packages using the provided [requirements.txt](https://github.com/atharva39/Slash-Mark-Python-Intermediate-Tasks/blob/83942719d38b8e4918f691e0bc60372e96518dee/Intermediate-Task-2/requirements.txt) file:
```
pip install -r requirements.txt
```

## Requirements
- Python 3.x
- pyttsx3
- speech_recognition
- wikipedia
- webbrowser
- os
- datetime
- random
- tkinter (for GUI version)
- PIL (for GUI version)
