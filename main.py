import os

from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import requests

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty("rate", 150)

def create_note():
    global recognizer

    speaker.say("Was möchtest du notieren?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio, language="de-DE")
                note = note.lower()

                speaker.say("Wähle ein Dateiname");
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, "w") as f:
                f.write(note)
                done = True
                speaker.say(f"Ich habe die Datei {filename} erstellt")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Das konnte ich nicht verstehen! Versuche es nochmal!")
            speaker.runAndWait()

def hello():
    speaker.say("Hallo Lars. Wie geht es dir heute?")
    speaker.runAndWait()

    done = False

    recognizer = speech_recognition.Recognizer()

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio, language="de-DE")
                message = message.lower()

                assistant.request(message)
                done = True

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
def fine_you():
    speaker.say("Ebenfalls. Danke. Kann ich etwas für dich tun?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio, language="de-DE")
                message = message.lower()

                assistant.request(message)
                done = True

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()

def discord():
    speaker.say("Discord wird gestartet!")
    speaker.runAndWait()
    os.startfile(r"D:\Desktop\Discord.lnk")

def chrome():
    speaker.say("Chrome wird gestartet!")
    speaker.runAndWait()
    os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")

def weather():
    api_key = "7da166bd5a144c464a592a29048885b5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Stuttgart"
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]
        z = x["weather"]

        speaker.say(" Die Temperatur beträgt " + str(int(current_temperature - 273.15)) + "Grad. ")
        speaker.runAndWait()

    else:
        print(" City Not Found ")

mappings = {"greeting": hello,
            "todo": create_note,
            "fine": fine_you,
            "discord": discord,
            "weather": weather,
            "chrome": chrome}

assistant = GenericAssistant("intents.json", intent_methods=mappings)
assistant.train_model()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            print("Recording...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            print("Recognitiom...")

            message = recognizer.recognize_google(audio, language="de-DE")
            message = message.lower()
            print(message)
        if "max" in message.split():
            print("hi")
            assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()