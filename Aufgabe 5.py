import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
import urllib.parse
import datetime


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmieren")

        # layout erzeugen
        layout = QFormLayout()

        # gui Elemente erstellen
        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QCalendarWidget()
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.save_button = QPushButton("Save")
        self.quit_action = QAction("Quit", self)
        self.save_action = QAction("Save", self)
        self.show_map_button = QPushButton("Auf Karte zeigen")
        self.load_action = QAction("Load", self)
        self.load_button = QPushButton("Load")

        # gui Elemente dem Layout hinzufügen
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.save_button)
        layout.addRow(self.show_map_button)
        layout.addRow(self.load_button)
        
        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

        # File-Menu erstellen und Einträge hinzufügen
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.load_action)
        file_menu.addAction(self.quit_action)

        # View-Menu erstellen und Eintrag hinzufügen
        view_menu = menubar.addMenu("View")
        view_menu.addAction("Karte").triggered.connect(self.show_map)

        # Verbindung der Action mit Slots (Funktionen)
        self.save_action.triggered.connect(self.save_data)
        self.quit_action.triggered.connect(self.quit_app)
        self.show_map_button.clicked.connect(self.show_map)
        self.load_action.triggered.connect(self.load_data)
        self.name.textChanged.connect(self.check_name)
        self.load_button.clicked.connect(self.load_data)

        self.show()

    def check_name(self, text):
        if text.lower() == "ostern":
            QMessageBox.information(self, "Happy Easter", "Herzlichen Glückwunsch! Sie haben das Easter Egg gefunden!")
            self.setWindowTitle("GUI-Programmierung - Easter Egg gefunden!")

    def save_data(self):
        # Daten aus den GUI-Elementen lesen
        Vorname = self.vorname.text()
        Name = self.name.text()
        Geburtstag = self.geburtstag.selectedDate().toString("dd.mm.yyyy")
        Adresse = self.adresse.text()
        Plz = self.plz.text()
        Ort = self.ort.text()
        Land = self.land.currentText()

        # Daten in einer Zeile mit Komma trennen
        data = f"{Vorname},{Name},{Geburtstag},{Adresse},{Plz},{Ort},{Land}"

    # Daten in eine Datei schreiben
        import datetime

        now = datetime.datetime.now()
        date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = "C:/Users/patri/Nextcloud/FHNW/S4/Geoprogrammierung/Kapitel_1/UebungenFS2023/output_{}.txt".format(date_string)

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(data)

        self.check_name(Name)

    def quit_app(self):
    # Programm beenden
        QApplication.quit()

    def show_map(self):
        # Adresse, Ort und PLZ auslesen
        Adresse = self.adresse.text()
        Ort = self.ort.text()
        Plz = self.plz.text()

    # URL für Google Maps zusammensetzen
        url = f"https://www.google.ch/maps/place/{Adresse}+{Plz}+{Ort}"
    # Umlaute und Sonderzeichen ersetzen
        url = urllib.parse.quote(url, safe=':/?=&')

    # Google Maps im Browser öffnen
        QDesktopServices.openUrl(QUrl(url))   # benötigt QtCore & QtGui


    def load_data(self):
    # File-Dialog öffnen
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text files (*.txt)")

        if file_dialog.exec_():
        # Datei auslesen
            file_name = file_dialog.selectedFiles()[0]

            with open(file_name, "r", encoding="UTF-8") as f:
                data = f.read()

        # Daten in GUI-Elemente einfügen
            Vorname, Name, Geburtstag, Adresse, Plz, Ort, Land = data.split(",")
            self.vorname.setText(Vorname)
            self.name.setText(Name)
            datum = Geburtstag.split(".") 
            y = int(datum[2])
            m = int(datum[1])
            d = int(datum[0])
            g = datetime.date(y,m,d)
            #self.geburtstag.setDateTextFormat(g, "dd.MM.yyyy")
            self.geburtstag.setSelectedDate(g)
            self.adresse.setText(Adresse)
            self.plz.setText(Plz)
            self.ort.setText(Ort)
            self.land.setCurrentText(Land)

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()