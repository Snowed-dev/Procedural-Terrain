import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSlider, QVBoxLayout, QLabel
from PyQt5 import QtCore
import noisemap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 300, 600)  
        self.setWindowTitle('Execute Code Example')

        layout = QVBoxLayout(self)

        self.button = QPushButton('Execute Code', self)
        layout.addWidget(self.button)

        self.parameter_sliders = {}  
        self.parameter_labels = {}  

        
        for param, value in noisemap.terrain_parameters.items():
            label = QLabel(f"{param.capitalize()} ({value * 100:.0f})")
            layout.addWidget(label)

            slider = QSlider(QtCore.Qt.Horizontal)
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setValue(int(value * 100))  
            layout.addWidget(slider)

            self.parameter_sliders[param] = slider
            self.parameter_labels[param] = label

            
            slider.valueChanged.connect(lambda value, param=param: self.slider_value_changed(param, value))

        
        self.button.clicked.connect(self.execute_external_code)
    
    def slider_value_changed(self, param, value):
        normalized_value = value / 100.0
        noisemap.terrain_parameters[param] = normalized_value
        self.parameter_labels[param].setText(f"{param.capitalize()} ({normalized_value * 100:.0f})")
        self.parameter_sliders[param].setToolTip(f"{param.capitalize()} (Value: {normalized_value * 100:.0f})")

    def execute_external_code(self):
        slider_values = {param: slider.value() / 100.0 for param, slider in self.parameter_sliders.items()}
        noisemap.noisegen(slider_values)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
