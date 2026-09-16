import json
import os

CONFIG = "config.json"
TEMPORAL = "config_temporal.json"
BACKUP = "config.bak"

def guardar_informacion(nombre:str, tema:str, idioma:str, fuente:int, color_barra:str, color_letra:str, dir_foto:str):
    try:
        with open(TEMPORAL, "w", encoding="utf-8") as archivo, \
            open(BACKUP, "w", encoding="utf-8") as backup:
            config_anterior = obtener_informacion()

            if config_anterior != None:
                json.dump(config_anterior, backup, indent=4)
            else:
                pass

            informacion = {
                "nombre_usuario": nombre,
                "tema_interfaz": tema,
                "idioma": idioma,
                "tamanio_fuente": fuente,
                "color_barra": color_barra,
                "color_letra": color_letra,
                "foto_perfil": dir_foto
            }



            json.dump(informacion, archivo, indent=4)
            os.replace(TEMPORAL, CONFIG)

    except FileNotFoundError:
        pass

def obtener_informacion():
    try:
        with open(CONFIG, "r", encoding="utf-8") as archivo:
            informacion = json.load(archivo)
            if (informacion["nombre_usuario"] and informacion["tema_interfaz"] and 
                informacion["idioma"] and informacion["tamanio_fuente"] and 
                informacion["color_barra"] and informacion["color_letra"] and 
                informacion["foto_perfil"]):

                return informacion
            return None


    except FileNotFoundError:
        return None

