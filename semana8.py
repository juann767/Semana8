import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit 
# Importación de librerías

class ControlGastos(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.total = 0  # variable para almacenar el total de los gastos

    def initUI(self):
        # Etiqueta de título
        self.titulo = QLabel("Registro de Gastos Personales", self)

        # Campo para ingresar nombre del gasto
        self.lbl_gasto = QLabel("Nombre del gasto:")
        self.txt_gasto = QLineEdit(self)

        # Campo para ingresar monto del gasto
        self.lbl_monto = QLabel("Monto del gasto:")
        self.txt_monto = QLineEdit(self)

        # Botón para agregar gasto
        self.btn_agregar = QPushButton("Agregar Gasto", self)
        self.btn_agregar.clicked.connect(self.agregar_gasto)

        # Área para mostrar lista de gastos
        self.lista_gastos = QTextEdit(self)
        self.lista_gastos.setReadOnly(True)

        # Etiqueta para mostrar el total acumulado
        self.lbl_total = QLabel("Total acumulado: $0")

        # Layout vertical para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.titulo)
        layout.addWidget(self.lbl_gasto)
        layout.addWidget(self.txt_gasto)
        layout.addWidget(self.lbl_monto)
        layout.addWidget(self.txt_monto)
        layout.addWidget(self.btn_agregar)
        layout.addWidget(self.lista_gastos)
        layout.addWidget(self.lbl_total)

        # Se aplica el layout a la ventana
        self.setLayout(layout)
        self.setWindowTitle("Control de Gastos - PyQt5")
        self.setGeometry(200, 200, 400, 400)

    def agregar_gasto(self): # Función que agrega un gasto a la lista y actualiza el total
        gasto = self.txt_gasto.text()
        monto = self.txt_monto.text()

        # Validación para que no estén vacíos y que el monto sea número
        if gasto != "" and monto.isnumeric():
            monto = float(monto)
            self.total += monto
            self.lista_gastos.append(f"{gasto}: ${monto}")
            self.lbl_total.setText(f"Total acumulado: ${self.total}")

            # Limpiar campos de entrada
            self.txt_gasto.clear()
            self.txt_monto.clear()
        else:
            self.lista_gastos.append("Ingrese un nombre válido y un monto numérico.")

# Ejecución del programa principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ControlGastos()
    ventana.show()
    sys.exit(app.exec_())
