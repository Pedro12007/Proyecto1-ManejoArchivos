import json
import os

CONFIG = "config.json"
TEMPORAL = "config_temporal.json"
BACKUP = "config.bak"

def guardar_informacion(nombre:str, tema:int, idioma:int, fuente:int, color_barra:str, color_letra:str, dir_foto:str):
    guardado = False
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
        guardado = True

    os.replace(TEMPORAL, CONFIG)
    return guardado


def obtener_informacion():
    try:
        with open(CONFIG, "r", encoding="utf-8") as archivo:
            informacion = json.load(archivo)
            if not isinstance(informacion, dict):
                return None
            if (
                informacion["nombre_usuario"] is not None and isinstance(informacion["nombre_usuario"], str) and
                informacion["tema_interfaz"] is not None and isinstance(informacion["tema_interfaz"], int) and not isinstance(informacion["tema_interfaz"], bool) and
                informacion["idioma"] is not None and isinstance(informacion["idioma"], int) and not isinstance(informacion["idioma"], bool) and
                informacion["tamanio_fuente"] is not None and isinstance(informacion["tamanio_fuente"], int) and not isinstance(informacion["tamanio_fuente"], bool) and
                informacion["color_barra"] is not None and isinstance(informacion["color_barra"], str) and
                informacion["color_letra"] is not None and isinstance(informacion["color_letra"], str) and
                informacion["foto_perfil"] is not None and isinstance(informacion["foto_perfil"], str)
                ):

                return informacion
            return None

    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        try:
            with open(BACKUP, "r", encoding="utf-8") as backup:
                informacion = json.load(backup)
                if (
                    informacion["nombre_usuario"] is not None and isinstance(informacion["nombre_usuario"], str) and
                    informacion["tema_interfaz"] is not None and isinstance(informacion["tema_interfaz"], int) and not isinstance(informacion["tema_interfaz"], bool) and
                    informacion["idioma"] is not None and isinstance(informacion["idioma"], int) and not isinstance(informacion["idioma"], bool) and
                    informacion["tamanio_fuente"] is not None and isinstance(informacion["tamanio_fuente"], int) and not isinstance(informacion["tamanio_fuente"], bool) and
                    informacion["color_barra"] is not None and isinstance(informacion["color_barra"], str) and
                    informacion["color_letra"] is not None and isinstance(informacion["color_letra"], str) and
                    informacion["foto_perfil"] is not None and isinstance(informacion["foto_perfil"], str)
                    ):

                    return informacion
                return None
            
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return None

