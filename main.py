import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from interfaz_ui import Ui_MainWindow
import configuracion as cf

class AppCafeteria(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ruta_foto_perfil = ""
     
        self.pushButton_guardarCambios.clicked.connect(self.guardar_configuracion)      
        self.pushButton_seleccionarFoto.clicked.connect(self.seleccionar_foto)
        self.pushButton_restablecerValores.clicked.connect(self.cargar_valores_por_defecto)
        self.pushButton_colorMenu.clicked.connect(lambda: self.elegir_color(self.color_menu_swatch))
        self.pushButton_colorLetra.clicked.connect(lambda: self.elegir_color(self.color_letra_swatch))

        self.cargar_configuracion()

    def seleccionar_foto(self):
        """Abre el explorador para elegir una foto y la muestra en el QLabel"""
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar Foto de Perfil", "", "Imágenes (*.png *.jpg *.jpeg)")
        if ruta_imagen:
            self.ruta_foto_perfil = ruta_imagen
            self.foto_perfil.setPixmap(QPixmap(ruta_imagen))
            print(f"Foto seleccionada: {ruta_imagen}")

    def cargar_configuracion(self):
        """Lee el archivo de configuración"""
        info = cf.obtener_informacion()
        if info is not None:
            self.nombre_usuario.setText(info["nombre_usuario"])
            self.tema_interfaz.setCurrentIndex(info["tema_interfaz"])
            self.idioma.setCurrentIndex(info["idioma"]) 
            self.tamano_fuente.setValue(info["tamanio_fuente"]) 
            self.color_menu_valor = info["color_barra"] 
            self.color_menu_swatch.setStyleSheet(f"background-color: {info["color_barra"]};")
            self.color_letra_valor = info["color_letra"]
            self.color_letra_swatch.setStyleSheet(f"background-color: {info["color_letra"] };")

            self.ruta_foto_perfil = info["foto_perfil"]
            if os.path.exists(self.ruta_foto_perfil):
                self.foto_perfil.setPixmap(QPixmap(self.ruta_foto_perfil))
            else:
                self.foto_perfil.setText("Sin foto")

            self.aplicar_estilos()
        else:
            QMessageBox.warning(
                self,          
                "Advertencia",        
                "Configuración no guardada o corrupta. Se cargaran valores por defecto."        
            )

            self.cargar_valores_por_defecto()

        
        

    def cargar_valores_por_defecto(self):
        self.nombre_usuario.setText("Usuario por defecto") 
        self.tema_interfaz.setCurrentIndex(0) 
        self.idioma.setCurrentIndex(0) 
        self.tamano_fuente.setValue(12) 
        self.color_menu_valor = "#FFFFFF" 
        self.color_menu_swatch.setStyleSheet(f"background-color: #FFFFFF;")
        self.color_letra_valor = "#000000"
        self.color_letra_swatch.setStyleSheet(f"background-color: #000000;")

        self.ruta_foto_perfil = ""
        self.foto_perfil.clear()
        self.foto_perfil.setText("Sin foto")

        self.aplicar_estilos()

    def guardar_configuracion(self):
        """Lee los widgets y realiza la escritura"""

        nombre = self.nombre_usuario.text()
        tema = self.tema_interfaz.currentIndex() 
        idioma = self.idioma.currentIndex()      
        fuente = self.tamano_fuente.value() 
        color_menu = self.color_menu_valor 
        color_letra = self.color_letra_valor
        dir_foto = self.ruta_foto_perfil
        
        guardado = cf.guardar_informacion(nombre, tema, idioma, fuente, color_menu, color_letra, dir_foto)

        if guardado == False:
            QMessageBox.warning(
                self,          
                "Advertencia",        
                "La información no se ha guardado."        
            )

        self.aplicar_estilos()
        

    def aplicar_estilos(self):
        """Genera y aplica dinámicamente el stylesheet usando los valores seleccionados"""
        tema_idx = self.tema_interfaz.currentIndex()
        fondo_principal = "#ffffff" if tema_idx == 0 else "#2b2b2b"
        
        tamano = self.tamano_fuente.value()
        color_letra = self.color_letra_valor
        color_barra = self.color_menu_valor

        nuevos_estilos = f"""
        QMainWindow, QWidget {{
            background-color: {fondo_principal};
            color: {color_letra};
            font-size: {tamano}px;
        }}
        
        QPushButton {{
            border: 1px solid #555555;
            border-radius: 4px;
            padding: 4px 8px;
            background-color: {fondo_principal};
            color: {color_letra};
        }}
        
        QPushButton:hover {{
            background-color: #555555;
            color: #ffffff;
        }}
        
        QLineEdit, QComboBox, QSpinBox {{
            border: 1px solid #555555;
            border-radius: 3px;
            padding: 2px 4px;
            background-color: {fondo_principal};
            color: {color_letra};
        }}
        
        QTabBar::tab {{
            background-color: {color_barra};
            color: {color_letra};
            border: 1px solid #555555;
            padding: 6px 12px;
        }}
        
        QTabBar::tab:selected {{
            background-color: {fondo_principal};
            font-weight: bold;
        }}
        
        QGroupBox {{
            border: 1px solid #555555;
            border-radius: 4px;
            margin-top: 8px;
        }}
        """
        
        self.setStyleSheet(nuevos_estilos)

    def elegir_color(self, frame):
        color = QColorDialog.getColor()
        if color.isValid():
            frame.setStyleSheet(f"background-color: {color.name()};")
            if frame.objectName() == "color_menu_swatch":
                self.color_menu_valor = color.name()
            elif frame.objectName() == "color_letra_swatch":
                self.color_letra_valor = color.name()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AppCafeteria()
    ventana.show()
    sys.exit(app.exec())