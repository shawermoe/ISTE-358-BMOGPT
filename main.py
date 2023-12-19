import speech_recognition as sr
import requests
from playsound import playsound

def get_chatgpt_response(text, api_key):
    chatgpt_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": text}]
    }
    response = requests.post(chatgpt_url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        print(f"Error getting response from ChatGPT: {response.text}")
        return ""

def synthesize_speech(text, api_key):
    api_url = "https://api.openai.com/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "tts-1",
        "input": text,
        "voice": "alloy"
    }
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        file_path = "speech.mp3"
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("Speech synthesized successfully, saved as 'speech.mp3'")
        playsound(file_path)  # Play the synthesized speech
    else:
        print("Error: Unable to connect to the API.")


def listen_for_wake_word(api_key):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for 'Hey John' or 'Goodbye John'...")
        while True:
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio).lower()
                if "hey john" in text:
                    following_text = text.split("hey john")[1].strip()
                    print(f"Received: {following_text}")
                    chatgpt_response = get_chatgpt_response(following_text, api_key)
                    print(f"ChatGPT response: {chatgpt_response}")
                    synthesize_speech(chatgpt_response, api_key)
                elif "goodbye john" in text:
                    print("Goodbye detected, stopping...")
                    break
            except sr.UnknownValueError:
                pass

api_key = "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"


listen_for_wake_word(api_key)
