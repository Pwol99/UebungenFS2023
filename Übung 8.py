import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.coeff_lbl = QLabel("Koeffizienten (durch Komma getrennt):", main_widget)
        self.coeff_le = QLineEdit(main_widget)

        self.range_lbl = QLabel("X-Bereich (durch Strich getrennt z.B. -5 5 )", main_widget)
        self.range_le = QLineEdit(main_widget)

        self.points_lbl = QLabel("Anzahl der Punkte:", main_widget)
        self.points_le = QLineEdit(main_widget)

        self.color_lbl = QLabel("Farbe:", main_widget)
        self.color_cb = QComboBox(main_widget)
        self.color_cb.addItems(['blau', 'rot', 'grün', 'schwarz'])

        self.plot_btn = QPushButton("Plotten", main_widget)
        self.plot_btn.clicked.connect(self.plot)

        main_layout = QVBoxLayout(main_widget)
        main_layout.addWidget(self.coeff_lbl)
        main_layout.addWidget(self.coeff_le)
        main_layout.addWidget(self.range_lbl)
        main_layout.addWidget(self.range_le)
        main_layout.addWidget(self.points_lbl)
        main_layout.addWidget(self.points_le)
        main_layout.addWidget(self.color_lbl)
        main_layout.addWidget(self.color_cb)
        main_layout.addWidget(self.plot_btn)

        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle("Polynom-Plotter")

    def plot(self):
        try:
            coeffs = [float(c.strip()) for c in self.coeff_le.text().split(",")]
            f = np.poly1d(coeffs)
        except:
            QMessageBox.critical(self, "Fehler", "Bitte Eingabe der Koeffizienten Überprüfen!")
            return

        try:
            x_range = [float(x.strip()) for x in self.range_le.text().split(" ")]
            if len(x_range) != 2:
                raise ValueError
        except:
            QMessageBox.critical(self, "Fehler", "Bitte Eingabe des Wertebereichs Überprüfen!")
            return

        try:
            num_points = int(self.points_le.text())
            if num_points <= 0:
                raise ValueError
        except:
            QMessageBox.critical(self, "Fehler", "Bitte Eingabe der Anzahl darzustellenden Punkte Überprüfen!")
            return

        color = self.color_cb.currentText()

        if color == "blau":
            color = "b"
        elif color == "rot":
            color = "r"
        elif color == "grün":
            color = "g"
        elif color == "schwarz":
            color = "k"

        x = np.linspace(x_range[0], x_range[1], num_points)
        y = f(x)
        plt.close()
        plt.clf()
        plt.plot(x, y, color=color)

        plt.title("Polynom-Plot")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
