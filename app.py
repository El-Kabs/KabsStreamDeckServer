from flask import Flask, request, jsonify, send_from_directory
import os
from utils import getBotones, modificarBoton, getBotonByPosition, resetBotones
from sistema import abrirPrograma
from audio import reproducirSonido
from discord import muteToggle
from multimedia import playToggle, nextTrack, prevTrack, volumenDown, volumenMute, volumenUp
from govee import apagarLuces, prenderLuces, cambiarBrillo, cambiarColor
from obs import cambiarEscena, iniciarStream, muteOBS, pararStream
from flask_cors import CORS, cross_origin

UPLOAD_FOLDER = './upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/botones', methods=["GET", "POST"])
@cross_origin()
def botones():
    if(request.method=="GET"):
        perfil = request.args.get('perfil')
        with open('last.txt', 'w') as f:
                f.write(str(perfil))
        return jsonify(getBotones(perfil))
    else:
        data = request.get_json()
        pos = data['pos']
        dataNueva = data['data']
        perfil = 1
        with open('last.txt', 'r') as f:
            perfil = f.readlines()[0]
        if('titulo' not in dataNueva):
            err = {'error': 'No hay titulo'}
            return jsonify(err)
        elif('pos' in dataNueva):
            err = {'error': 'No se puede modificar la posicion'}
            return jsonify(err)
        result = modificarBoton(int(pos), dataNueva, perfil)
        if(result):
            return jsonify(getBotonByPosition(pos, perfil))
        else:
            err = {'err': 'No se pudo modificar el archivo JSON'}
            return jsonify(err)

@app.route('/ejecutar', methods=["POST"])
@cross_origin()
def ejecutar():
    commands = {
        "playToggle": playToggle,
        "abrirPrograma": abrirPrograma,
        "reproducirSonido": reproducirSonido,
        "muteToggle": muteToggle,
        "nextTrack": nextTrack,
        "prevTrack": prevTrack,
        "volumenDown": volumenDown,
        "volumenMute": volumenMute,
        "volumenUp": volumenUp,
        "apagarLuces": apagarLuces,
        "prenderLuces": prenderLuces,
        "cambiarBrillo": cambiarBrillo,
        "cambiarColor": cambiarColor,
        "cambiarEscena": cambiarEscena,
        "iniciarStream": iniciarStream,
        "muteOBS": muteOBS,
        "pararStream": pararStream
    }
    data = request.get_json()
    try:
        commands[data['func']](data['args'])
        ok = {'ok': 'Accion enviada'}
        return jsonify(ok)
    except Exception as e:
        err = {'err': 'Fallo al ejecutar', 'excepcion': str(e)}
        return jsonify(err)

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'err': 'No se encontró el archivo'})
        file = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        return jsonify({'path': path})

@app.route('/upload/<path:filename>', methods=['GET', 'POST'])
@cross_origin()
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)

@app.route('/reset', methods=['GET'])
@cross_origin()
def reset():
    perfil = request.args.get('perfil')
    resp = resetBotones(perfil)
    if(resp):
        return jsonify({'ok': 'ok'})
    else:
        return jsonify({'err': 'El archivo no pudo ser escrito'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')