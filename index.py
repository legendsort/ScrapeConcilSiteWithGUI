import PySimpleGUI as sg
from scrape import *

font=('courier', 18) #global font
layout = [
    [
        sg.Text("Input new keyword ", font=font),
        sg.In(size=(20, 3), enable_events=True, key="input", font=font),
    ],
    [sg.pin(sg.T("", font=font))],
    [
        sg.Button("Start", font=font),
        sg.Button("Stop", font=font),
        sg.Button("Exit", font=font),
    ],
]
window = sg.Window("Property application scraping software", layout, margins=(50, 40))

def start():

    pass

def stop():

    pass

# Run the Event Loop
while True:
    event, values = window.read()
    print(event, values)
    if event == "Exit" or event == sg.WIN_CLOSED:
        window.close()
        break
    if event == "Start":
        start()
        pass
    if event == "Stop":
        stop()
    