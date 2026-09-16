import json
import os

CONFIG = "config.json"
TEMPORAL = "config_temporal.json"
BACKUP = "config.bak"

def guardar_informacion(nombre:str, tema:int, idioma:int, fuente:int, color_barra:str, color_letra:str, dir_foto:str):
    
    hay_informacion = False
    config_anterior = obtener_informacion()

    if config_anterior != None:
        hay_informacion = True
        with open(BACKUP, "w", encoding="utf-8") as backup:
            json.dump(config_anterior, backup, indent=4)


    informacion = {
        "nombre_usuario": nombre,
        "tema_interfaz": tema,
        "idioma": idioma,
        "tamanio_fuente": fuente,
        "color_barra": color_barra,
        "color_letra": color_letra,
        "foto_perfil": dir_foto
    }

    if hay_informacion is not True:
        with open(BACKUP, "w", encoding="utf-8") as backup:
            json.dump(informacion, backup, indent=4)

    with open(TEMPORAL, "w", encoding="utf-8") as archivo:
        json.dump(informacion, archivo, indent=4)

    os.replace(TEMPORAL, CONFIG)


def obtener_informacion():
    try:
        with open(CONFIG, "r", encoding="utf-8") as archivo:
            informacion = json.load(archivo)
            if (informacion["nombre_usuario"] != None and informacion["tema_interfaz"] != None and 
                informacion["idioma"] != None and informacion["tamanio_fuente"] != None and 
                informacion["color_barra"] != None and informacion["color_letra"] != None and 
                informacion["foto_perfil"] != None):

                return informacion
            return None

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        try:
            with open(BACKUP, "r", encoding="utf-8") as backup:
                informacion = json.load(backup)
                if (informacion["nombre_usuario"] != None and informacion["tema_interfaz"] != None and 
                    informacion["idioma"] != None and informacion["tamanio_fuente"] != None and 
                    informacion["color_barra"] != None and informacion["color_letra"] != None and 
                    informacion["foto_perfil"] != None):

                    return informacion
                return None
            
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return None

