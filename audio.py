from playsound import playsound
from os import path
import subprocess
import threading
                                               
def convertirMP3toWAV(ruta):
    subprocess.call(['ffmpeg', '-y', '-i', ruta, ruta.replace('.mp3', '.wav')])

def reproducir(ruta):
    playsound(ruta)

def reproducirSonido(data):
    ruta = data['ruta']
    print(ruta)
    if('.mp3' in ruta):
        print(ruta)
        convertirMP3toWAV(ruta)
        x = threading.Thread(target=reproducir, args=(ruta.replace('.mp3', '.wav'),))
        x.start()
    elif('.wav' in ruta):
        x = threading.Thread(target=reproducir, args=(ruta,))
        x.start()