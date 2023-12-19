## Overview
This project is a voice-activated chatbot that utilizes the OpenAI GPT-3.5 model for generating responses and a text-to-speech (TTS) engine for vocalizing them. The system listens for specific wake words, processes spoken queries, fetches responses from ChatGPT, and then reads them aloud.

## Features
- **Voice Activation:** Listens continuously for the wake words "Hey John" or "Goodbye John".
- **Speech Recognition:** Converts spoken words into text using Google's speech recognition API.
- **ChatGPT Integration:** Sends recognized speech to OpenAI's ChatGPT for processing.
- **Text-to-Speech:** Converts ChatGPT responses into audible speech.
- **Wake Word Termination:** Stops listening when "Goodbye John" is detected.

## Requirements
- Python 3.x
- `speech_recognition` Python library
- `requests` Python library
- `playsound` Python library
- OpenAI API key

## Installation
1. Install the required Python libraries:
   ```bash
   pip install speech_recognition requests playsound
   ```
2. Clone this repository or download the source code.

## Usage
1. Set your OpenAI API key in the script.
2. Run the script:
   ```bash
   python script_name.py
   ```
3. Say "Hey John" followed by your query.
4. The program will process your speech, get a response from ChatGPT, and read it aloud.
5. To exit, say "Goodbye John".

## Configuration
- The API key for OpenAI needs to be set in the `api_key` variable.
- The wake word can be changed by modifying the `listen_for_wake_word` function.

## Limitations
- Requires a stable internet connection for API calls.
- Dependent on the availability and response time of the OpenAI API.
- Speech recognition accuracy can vary based on environmental noise and clarity of speech.
