import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QVBoxLayout, QLabel
from PyQt5 import QtCore
import noisemap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('Execute Code Example')

        layout = QVBoxLayout(self)

        self.button = QPushButton('Execute Code', self)
        layout.addWidget(self.button)

        self.mountainlabel = QLabel("Mountains")
        layout.addWidget(self.mountainlabel)

        # Create a slider for mountaincap
        self.slider = QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        layout.addWidget(self.slider)

        # Create a slider for thickforest
        self.thickforestlabel = QLabel("Thick Forest")
        layout.addWidget(self.thickforestlabel)

        self.thickForestSlider = QSlider(QtCore.Qt.Horizontal)
        self.thickForestSlider.setMinimum(0)
        self.thickForestSlider.setMaximum(100)
        layout.addWidget(self.thickForestSlider)

        # Connect signals to slots
        self.button.clicked.connect(self.execute_external_code)
        self.slider.valueChanged.connect(self.slider_value_changed)
        self.thickForestSlider.valueChanged.connect(self.thickforestSliderValue)

    def slider_value_changed(self, value):
        normalized_mountaincap = value / 100.0  # Map slider value (0-100) to mountaincap range (0.0-1.0)
        noisemap.terrain_parameters["mountaincap"] = normalized_mountaincap
        self.mountainlabel.setText(f"Mountains (Value: {normalized_mountaincap * 100})")

    def thickforestSliderValue(self, value):
        changed_thickforest = value / 100.0
        noisemap.terrain_parameters["thickforest"] = changed_thickforest
        self.thickforestlabel.setText(f"Thick Forests (Value: {changed_thickforest})")

    def execute_external_code(self):
        noisemap.noisegen(self.slider.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
