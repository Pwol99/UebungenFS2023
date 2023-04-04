import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Fenster-Titel definieren:
        self.setWindowTitle("GUI-Programmierung")

    # layout erzeugen
        layout = QFormLayout()

    # gui Elemente erstellen
        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QCalendarWidget()
    # ja es wäre ein QLineEdit, aber ich finde es mit dem QCAlenderWidget schöner und angenehmer. 
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.save_button = QPushButton("Save")
        self.quit_action = QAction("Quit", self)
        self.save_action = QAction("Save", self)

    # gui Elemente dem Layout hinzufügen
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Name:", self.name)
        layout.addRow("Geburtstag:", self.geburtstag)
        layout.addRow("Adresse:", self.adresse)
        layout.addRow("Postleitzahl:", self.plz)
        layout.addRow("Ort:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.save_button)

        center = QWidget()
        center.setLayout(layout)

        self.setCentralWidget(center)

    # File-Menu erstellen und Einträge hinzufügen
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.quit_action)

    # Verbindung der Action mit Slots (Funktionen)
        self.save_action.triggered.connect(self.save_data)
        self.quit_action.triggered.connect(self.quit_app)
        self.save_button.clicked.connect(self.save_data)
        self.name.textChanged.connect(self.check_name)

        self.show()
    #Spass an Spielereien....
    def check_name(self, text):
        if text.lower() == "ostern":
            QMessageBox.information(self, "Happy Easter", "Herzlichen Glückwunsch! Sie haben das Easter Egg gefunden!")
            self.setWindowTitle("GUI-Programmierung - Easter Egg gefunden!")

    def save_data(self):
    # Daten aus den GUI-Elementen lesen
        Vorname = self.vorname.text()
        Name = self.name.text()
        Geburtstag = self.geburtstag.selectedDate().toString()
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

        with open(file_name, "w") as f:
            f.write(data)

        self.check_name(Name)

    def quit_app(self):
    # Programm beenden
        QApplication.quit()

def main():
    app = QApplication(sys.argv)  # Qt Applikation erstellen
    mainwindow = MyWindow()       # Instanz Fenster erstellen
    mainwindow.raise_()           # Fenster nach vorne bringen
    app.exec_()                   # Applikations-Loop starten

if __name__ == '__main__':
    main()