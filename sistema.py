import subprocess
import threading

def threadAbrir(ruta):
    if('steam://' in ruta):
        idApp = ruta.replace('steam://', '').split('/')[1]
        subprocess.call(r"C:\\Program Files (x86)\\Steam\\steam.exe -applaunch "+idApp)
    else:
        subprocess.call([ruta])

def abrirPrograma(data):    
    x = threading.Thread(target=threadAbrir, args=(data['ruta'],))
    x.start()

def atajo(atajo):
    pass

#abrirPrograma('C:\Program Files (x86)\Google\Chrome\Application\\chrome.exe')