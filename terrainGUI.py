import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QVBoxLayout, QLabel
from PyQt5 import QtCore

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Execute Code Example')

        layout = QVBoxLayout(self)

        self.button = QPushButton('Execute Code', self)
        layout.addWidget(self.button)

        self.mountaincap = QLabel("Mountains")
        layout.addWidget(self.mountaincap)

        self.slider = QSlider(QtCore.Qt.Horizontal)
        layout.addWidget(self.slider)

        self.button.clicked.connect(self.execute_external_code)
        self.slider.valueChanged.connect(self.slider_value_changed)  # Connect valueChanged signal to slot

    def slider_value_changed(self, value):
        self.mountaincap.setText(f"Mountains (Value: {value})")  # Update label with current slider value
        self.run_noisegen(value)  # Call noisegen function with the updated value

    def execute_external_code(self):
        # Run the noisemap.py script using subprocess
        subprocess.Popen(["python", "noisemap.py"])

    def run_noisegen(self, value):
        import pygame  # Import Pygame locally within the function
        from noisemap import noisegen
        noisegen(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
