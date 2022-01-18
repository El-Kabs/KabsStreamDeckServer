import json

def escribirJSON(data, perfil):
    with open(str(perfil)+'.json', 'w') as f:
        json.dump(data, f)

def getBotones(perfil):
    data = []
    with open(str(perfil)+'.json') as f:
        data = json.load(f)
    return data

def getBotonByPosition(pos, perfil):
    data = getBotones(perfil)
    for x in data:
        if(x['boton']==pos):
            return x

def modificarBoton(pos, nuevo, perfil):
    nuevo['boton'] = pos
    try:
        data = getBotones(perfil)
        for x in range(0, len(data)):
            if(data[x]['boton']==pos):
                data[x] = nuevo
        escribirJSON(data, perfil)
    except Exception as e:
        print(e)
        return False
    return True

def resetBotones(perfil):
    data = getBotones(perfil)
    for x in range(0, len(data)):
        aux = {"titulo": "", "boton": data[x]["boton"]}
        data[x] = aux
    escribirJSON(data, perfil)
    return True
