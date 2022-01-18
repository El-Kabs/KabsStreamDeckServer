import keyboard

def playToggle(data):
    keyboard.send("play/pause")

def prevTrack(data):
    keyboard.send("previous track")

def nextTrack(data):
    keyboard.send("next track")

def volumenMute(data):
    keyboard.send("volume mute")

def volumenUp(data):
    keyboard.send("volume up")

def volumenDown(data):
    keyboard.send("volume down")

#playToggle("")