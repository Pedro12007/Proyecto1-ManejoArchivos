import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from interfaz_ui import Ui_MainWindow

class AppCafeteria(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
     
        self.pushButton_guardarCambios.clicked.connect(self.guardar_configuracion)      
        self.pushButton_seleccionarFoto.clicked.connect(self.seleccionar_foto)
        self.pushButton_restablecerValores.clicked.connect(self.cargar_valores_por_defecto)

        self.cargar_configuracion()

    def seleccionar_foto(self):
        """Abre el explorador para elegir una foto y la muestra en el QLabel"""
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar Foto de Perfil", "", "Imágenes (*.png *.jpg *.jpeg)")
        if ruta_imagen:
            print(f"Foto seleccionada: {ruta_imagen}")

    def cargar_configuracion(self):
        """Lee el archivo de configuración"""
        pass

    def cargar_valores_por_defecto(self):
        self.nombre_usuario.setText("Usuario por defecto") 
        self.tema_interfaz.setCurrentIndex(0) 
        self.idioma.setCurrentIndex(0) 
        self.tamano_fuente.setValue(12) 
        self.color_menu.setText("#FFFFFF") 
        self.color_letra.setText("#000000")

    def guardar_configuracion(self):
        """Lee los widgets y realiza la escritura"""

        datos_a_guardar = {
            "nombre": self.nombre_usuario.text(),
            "tema": self.tema_interfaz.currentText(), 
            "idioma": self.idioma.currentText(), 
            "fuente": self.tamano_fuente.value(), 
            "color_menu": self.color_menu.text(), 
            "color_letra": self.color_letra.text() 
        }
        

        
        print("Datos listos para guardar de forma segura:", datos_a_guardar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AppCafeteria()
    ventana.show()
    sys.exit(app.exec())