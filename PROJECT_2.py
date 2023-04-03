import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

layout = [
    
    [sg.InputText(key="-INPUT-"),sg.Button("Speak", key="-SPEAK-")],
    [sg.Text("Select a voice:"),sg.Radio("Male", "VOICE", default=True, key="-MALE-"),sg.Radio("Female", "VOICE", key="-FEMALE-")],
]

window = sg.Window("Text To Speech App", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-EXIT-":
        break
    if event == "-SPEAK-":
        text = values["-INPUT-"]
        voice_id = None
        if values["-MALE-"]:
            voice_id = 0
        elif values["-FEMALE-"]:
            voice_id = 1
        if voice_id is not None:
            engine.setProperty('voice', voices[voice_id].id)
        engine.say(text)
        engine.runAndWait()

window.close()
engine.stop()