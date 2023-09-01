import speech_recognition as sr
from time import sleep
from pynput.mouse import Controller, Button

mouse = Controller()
PATH = "C:/Users/talha/Downloads/chromedriver_win32/chromedriver.exe"
r = sr.Recognizer()
mousePaths = [(10, 1070), (10, 1000), (10, 925)]


def Record():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="en-EN")
            print(voice)

        except sr.UnknownValueError:
            print("Can't detected.")

        except sr.RequestError:
            print("System is not working.")

        return voice


def Response(voice):
    if "close" in voice:
        ClosePC()


def LeftClick():
    sleep(1)
    mouse.press(Button.left)
    sleep(0.1)
    mouse.release(Button.left)
    sleep(1)


def ClosePC():
    for i in mousePaths:
        mouse.position = i
        LeftClick()


sleep(1)
print("System started.")

while True:
    voice = Record()
    Response(voice)