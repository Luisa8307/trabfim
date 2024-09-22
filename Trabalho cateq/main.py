from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox
from PyQt6.QtGui import QPixmap
import sys
import qrcode

def gerar_qrcode(numero_mesa):
    url = f"http://localhost:5000/mesa/{numero_mesa}"
    qr = qrcode.make(url)
    qr.save(f"qrcode_mesa_{numero_mesa}.png")

class SistemaRestaurante(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Restaurante")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.combo_mesas = QComboBox()
        self.combo_mesas.addItems([str(i) for i in range(1, 21)])  # Mesas 1 a 20
        self.layout.addWidget(self.combo_mesas)

        self.btn_gerar_qrcode = QPushButton("Gerar QR Code")
        self.btn_gerar_qrcode.clicked.connect(self.gerar_qrcode)
        self.layout.addWidget(self.btn_gerar_qrcode)

        self.label_qrcode = QLabel(self)
        self.layout.addWidget(self.label_qrcode)

        self.setLayout(self.layout)

    def gerar_qrcode(self):
        numero_mesa = self.combo_mesas.currentText()
        gerar_qrcode(numero_mesa)  # Chama a função para gerar QR code
        pixmap = QPixmap(f"qrcode_mesa_{numero_mesa}.png")
        self.label_qrcode.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SistemaRestaurante()
    window.show()
    sys.exit(app.exec())
