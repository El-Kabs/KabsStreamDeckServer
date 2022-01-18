from obswebsocket import obsws, requests 
import os

def cambiarEscena(data):
    print(data)
    escena = data["escena"]
    host = "localhost"
    port = 4440
    password = os.environ.get('passOBS')

    ws = obsws(host, port, password)
    ws.connect()

    try:
        ws.call(requests.SetCurrentScene(escena))

    except KeyboardInterrupt:
        pass

    ws.disconnect()

def iniciarStream(data):
    host = "localhost"
    port = 4440
    password = os.environ.get('passOBS')

    ws = obsws(host, port, password)
    ws.connect()

    try:
        ws.call(requests.StartStreaming())

    except KeyboardInterrupt:
        pass

    ws.disconnect()

def pararStream(data):
    host = "localhost"
    port = 4440
    password = os.environ.get('passOBS')

    ws = obsws(host, port, password)
    ws.connect()

    try:
        ws.call(requests.StopStreaming())

    except KeyboardInterrupt:
        pass

    ws.disconnect()

def muteOBS(data):
    host = "localhost"
    port = 4440
    password = os.environ.get('passOBS')

    ws = obsws(host, port, password)
    ws.connect()

    try:
        ws.call(requests.ToggleMute("Mic/Aux"))

    except KeyboardInterrupt:
        pass

    ws.disconnect()
