from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *
from PyQt5.QtWebEngineWidgets import *
import urllib.parse
import sys

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Kapitel_1/UebungenFS2023/showmap.ui",self)
        self.show()
        self.pushButton.clicked.connect(self.show_map)
        self.show()

    def show_map(self):
        # Adresse, Ort und PLZ auslesen
        lange = self.lineEdit.text()
        breite = self.lineEdit_2.text()

        # URL für Google Maps zusammensetzen
        url = f"https://www.google.ch/maps/place/{lange}+{breite}"
        # Umlaute und Sonderzeichen ersetzen
        url = urllib.parse.quote(url, safe=':/?=&')

        # Google Maps im Browser öffnen
        QDesktopServices.openUrl(QUrl(url))   # benötigt QtCore & QtGui


app = QApplication([])
win = UIFenster()
app.exec()
sys.exit(app.exec())