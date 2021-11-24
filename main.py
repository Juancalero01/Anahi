import sys
from datetime import datetime
from Vistas.principal import Ui_Principal
from Vistas.login import Ui_Login
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, QDate
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from Auxiliares.tipoDocumento import TipoDocumento
from Auxiliares.tipoProvincias import TipoProvincia
from Auxiliares.tipoInmueble import TipoInmueble
from Otros.tipoConversion import TipoConversion
from Alquiler.alquiler import Alquiler
from Cliente.cliente import Cliente
from Usuario.usuario import Usuario


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.principal = Main()
        self.usuario = Usuario()
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Alerta")
        self.mensaje.setWindowIcon(QtGui.QIcon(":Iconos/logo.png"))
        self.ui.btnIngresar.clicked.connect(self.obtenerUsuario)

    def abrirPrincipal(self):
        self.principal.show()
        self.close()

    def obtenerUsuario(self):
        self.usuario.usuario = self.ui.txtUsuario.text()
        self.usuario.contrasena = self.ui.txtClave.text()
        if self.usuario.usuario == "" or self.usuario.contrasena == "":
            self.mensaje.setText("¡Debe ingresar un usuario y una contraseña!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif self.usuario.usuario != "" and self.usuario.contrasena != "":
            datos = self.usuario.comprobarLogin(
                self.usuario.usuario, self.usuario.contrasena)
            if datos != []:
                self.abrirPrincipal()
            else:
                self.mensaje.setText("¡Usuario o Contraseña incorrecto!")
                self.mensaje.setIcon(QMessageBox.Warning)
                x = self.mensaje.exec_()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.cliente = Cliente()
        self.alquiler = Alquiler()
        self.auxiliarDocumento = TipoDocumento()
        self.auxiliarProvincia = TipoProvincia()
        self.auxiliarInmueble = TipoInmueble()
        self.auxiliarConvertir = TipoConversion()
        self.auxiliarId = None
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Alerta")
        self.mensaje.setWindowIcon(QtGui.QIcon(":Iconos/logo.png"))

        # BOTONES MENU IZQUIERDO
        ############################################################################
        self.ui.btnMenu.clicked.connect(self.menuIzquierdo)
        self.ui.btnPrincipal.clicked.connect(
            lambda: self.ui.paginasPrincipales.setCurrentWidget(self.ui.principal))
        self.ui.btnClientes.clicked.connect(
            lambda: self.ui.paginasPrincipales.setCurrentWidget(self.ui.clientes))
        self.ui.btnReservas.clicked.connect(
            lambda: self.ui.paginasPrincipales.setCurrentWidget(self.ui.alquiler))
        self.ui.btnCerrarSesion.clicked.connect(self.cerrarSesion)
        ############################################################################

        # FUNCIONES INICIALES
        ############################################################################
        self.mostrarTablaCliente()
        self.contadorCliente()
        self.mostrarProvincias()
        self.mostrarTipoDocumento()
        self.mostrarFechaActual()
        self.mostrarInmueble()
        self.mostrarTablaAlquiler()
        ############################################################################

        # BOTONES CLIENTE (REGISTRAR - MODIFICAR - ELIMINAR - BUSCAR)
        ############################################################################
        self.ui.btnRegistrarCliente.clicked.connect(self.menuRegistrarCliente)
        self.ui.btnCerrarRegistroCliente.clicked.connect(
            self.cerrarMenuRegistrarCliente)
        self.ui.btnConfirmarRegistroCliente.clicked.connect(
            self.formularioRegistroCliente)
        self.ui.btnCancelarRegistroCliente.clicked.connect(
            self.cerrarMenuRegistrarCliente)
        self.ui.btnModificarCliente.clicked.connect(self.menuModificarCliente)
        self.ui.btnCerrarModificarCliente.clicked.connect(
            self.cerrarMenuModiciarCliente)
        self.ui.btnConfirmarModificarCliente.clicked.connect(
            self.formularioModificarCliente)
        self.ui.btnCancelarModificarCliente.clicked.connect(
            self.cerrarMenuModiciarCliente)
        self.ui.btnEliminarCliente.clicked.connect(self.eliminarCliente)
        self.ui.btnBuscarCliente.clicked.connect(self.buscarClienteDocumento)
        ############################################################################

        # BOTONES RESERVA (REGISTRAR - MODIFICAR - ELIMINAR - BUSCAR)
        ############################################################################
        self.ui.btnRegistrarAlquiler.clicked.connect(
            self.menuRegistrarAlquiler)
        self.ui.btnCerrarRegistroAlquiler.clicked.connect(
            self.cerrarMenuRegistrarAlquiler)
        self.ui.btnConfirmarRegistroAlquiler.clicked.connect(
            self.formularioRegistroAlquiler)
        self.ui.btnCancelarRegistroAlquiler.clicked.connect(
            self.cerrarMenuRegistrarAlquiler)
        self.ui.btnModificarAlquiler.clicked.connect(
            self.menuModificarAlquiler)
        self.ui.btnCerrarModificarAlquiler.clicked.connect(
            self.cerrarMenuModificarAlquiler)
        self.ui.btnConfirmarModificarAlquiler.clicked.connect(
            self.formularioModificarAlquiler)
        self.ui.btnCancelarModificarAlquiler.clicked.connect(
            self.cerrarMenuModificarAlquiler)
        self.ui.btnEliminarAlquiler.clicked.connect(self.eliminarAlquiler)
        self.ui.btnBuscarAlquiler.clicked.connect(self.buscarAlquilerDocumento)
        ##############################################################################

    # ALQUILER
    ############################################################################
    def formularioRegistroAlquiler(self):
        self.alquiler.cliente = self.ui.txtDocumentoRegistroAlquiler.text()
        self.alquiler.propiedad = self.ui.cmbPropiedadRegistroAlquiler.currentText()
        self.alquiler.fechaAlquiler = self.ui.txtReservaRegistroAlquiler.text()
        self.alquiler.cantidadPersona = self.ui.txtCantidadPersonasRegistroAlquiler.text()
        self.alquiler.cantidadMascota = self.ui.txtCantidadMascotasRegistroAlquiler.text()
        self.alquiler.fechaLlegada = self.ui.dtFechaLlegadaRegistroAlquiler.text()
        self.alquiler.horaLlegada = self.ui.txtHoraLlegadaRegistroAlquiler.text()
        self.alquiler.fechaSalida = self.ui.dtFechaSalidaRegistroAlquiler.text()
        self.alquiler.horaSalida = self.ui.txtHoraSalidaRegistroAlquiler.text()
        self.alquiler.precio = self.ui.txtPrecioRegistroAlquiler.text()
        retorno = self.alquiler.registrarAlquiler(self.alquiler.cliente, self.alquiler.propiedad, self.alquiler.fechaAlquiler, self.alquiler.cantidadPersona, self.alquiler.cantidadMascota,
                                                  self.alquiler.fechaLlegada, self.alquiler.horaLlegada, self.alquiler.fechaSalida, self.alquiler.horaSalida, self.alquiler.precio)
        if retorno == True:
            self.mostrarTablaAlquiler()
            self.cerrarMenuRegistrarAlquiler()

    def formularioModificarAlquiler(self):
        self.alquiler.cliente = self.ui.txtDocumentoModificarAlquiler.text()
        self.alquiler.propiedad = self.ui.cmbPropiedadModificarAlquiler.currentText()
        self.alquiler.fechaAlquiler = self.ui.txtReservaModificarAlquiler.text()
        self.alquiler.cantidadPersona = self.ui.txtCantidadPersonasModificarAlquiler.text()
        self.alquiler.cantidadMascota = self.ui.txtCantidadMascotasModificarAlquiler.text()
        self.alquiler.fechaLlegada = self.ui.dtFechaLlegadaModificarAlquiler.text()
        self.alquiler.horaLlegada = self.ui.txtHoraLlegadaModificarAlquiler.text()
        self.alquiler.fechaSalida = self.ui.dtFechaSalidaModificarAlquiler.text()
        self.alquiler.horaSalida = self.ui.txtHoraSalidaModificarAlquiler.text()
        self.alquiler.precio = self.ui.txtPrecioModificarAlquiler.text()
        # AUXILIARES TEST X1 = "" , X2 = "", X3 = 0
        retorno = self.alquiler.modificarAlquiler(self.auxiliarId, self.alquiler.cliente, self.alquiler.propiedad, self.alquiler.fechaAlquiler, self.alquiler.cantidadPersona, self.alquiler.cantidadMascota,
                                                  self.alquiler.fechaLlegada, self.alquiler.horaLlegada, self.alquiler.fechaSalida, self.alquiler.horaSalida, self.alquiler.precio)
        if retorno == True:
            self.mostrarTablaAlquiler()
            self.cerrarMenuRegistrarAlquiler()

    def eliminarAlquiler(self):
        seleccion = self.ui.tblAlquiler.selectedItems()
        if seleccion == []:
            self.mensaje.setText("¡Selecciona una fila para eliminar!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif seleccion != []:
            seleccion = [dato.text() for dato in seleccion]
            self.ui.tblAlquiler.clearSelection()
            test = QMessageBox.question(
                self, "Alerta", f"¿Está seguro de eliminar la reserva de {seleccion[1]}?", QMessageBox.Yes | QMessageBox.No)
            if test == QMessageBox.Yes:
                self.alquiler.eliminarAlquiler(seleccion[0])
                self.mostrarTablaAlquiler()
            elif test == QMessageBox.No:
                pass

    def buscarAlquilerDocumento(self):
        documento = self.ui.txtBuscarAlquiler.text()
        if documento != "":
            datos = self.alquiler.buscarAlquilerDocumento(documento)
            if datos == []:
                self.mensaje.setText(
                    "No se encontro ninguna reserva con ese documento")
                self.mensaje.setIcon(QMessageBox.Warning)
                x = self.mensaje.exec_()
                self.resetearBusquedaAlquiler()
                self.mostrarTablaAlquiler()
            else:
                i = len(datos)
                self.ui.tblAlquiler.setRowCount(i)
                filaTabla = 0
                for fila in datos:
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 0, QtWidgets.QTableWidgetItem(str(fila[0])))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 1, QtWidgets.QTableWidgetItem(f"{fila[1]} {fila[2]}"))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 2, QtWidgets.QTableWidgetItem(fila[3]))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 3, QtWidgets.QTableWidgetItem(fila[4]))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 4, QtWidgets.QTableWidgetItem(fila[5]))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 5, QtWidgets.QTableWidgetItem(fila[6]))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 6, QtWidgets.QTableWidgetItem(fila[7]))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 7, QtWidgets.QTableWidgetItem(fila[8]))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 8, QtWidgets.QTableWidgetItem(fila[9]))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 9, QtWidgets.QTableWidgetItem(fila[10]))
                    self.ui.tblAlquiler.setItem(
                        filaTabla, 10, QtWidgets.QTableWidgetItem(str(fila[11])))
                    filaTabla += 1
        elif documento == "":
            self.mensaje.setText("¡Debe ingresar un documento!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
            self.mostrarTablaAlquiler()

    # ALQUILER AUXILIARES

    def mostrarTablaAlquiler(self):
        datos = self.alquiler.mostrarAlquiler()
        i = len(datos)
        self.ui.tblAlquiler.setRowCount(i)
        filaTabla = 0
        for fila in datos:
            self.ui.tblAlquiler.setItem(
                filaTabla, 0, QtWidgets.QTableWidgetItem(str(fila[0])))
            self.ui.tblAlquiler.setItem(
                filaTabla, 1, QtWidgets.QTableWidgetItem(f"{fila[1]} {fila[2]}"))
            self.ui.tblAlquiler.setItem(
                filaTabla, 2, QtWidgets.QTableWidgetItem(fila[3]))
            self.ui.tblAlquiler.setItem(
                filaTabla, 3, QtWidgets.QTableWidgetItem(fila[4]))
            self.ui.tblAlquiler.setItem(
                filaTabla, 4, QtWidgets.QTableWidgetItem(fila[5]))
            self.ui.tblAlquiler.setItem(
                filaTabla, 5, QtWidgets.QTableWidgetItem(fila[6]))
            self.ui.tblAlquiler.setItem(
                filaTabla, 6, QtWidgets.QTableWidgetItem(fila[7]))
            self.ui.tblAlquiler.setItem(
                filaTabla, 7, QtWidgets.QTableWidgetItem(fila[8]))
            self.ui.tblAlquiler.setItem(
                filaTabla, 8, QtWidgets.QTableWidgetItem(fila[9]))
            self.ui.tblAlquiler.setItem(
                filaTabla, 9, QtWidgets.QTableWidgetItem(fila[10]))
            self.ui.tblAlquiler.setItem(
                filaTabla, 10, QtWidgets.QTableWidgetItem(str(fila[11])))
            filaTabla += 1

    def menuRegistrarAlquiler(self):
        self.mostrarFechaActual()
        ancho = self.ui.frameNueve_2.width()
        if ancho == 0:
            nuevoAncho = 500
            self.ui.paginasAlquileres.setCurrentWidget(
                self.ui.alquileresRegistrar)
            self.ui.btnModificarAlquiler.setEnabled(False)
            self.ui.btnEliminarAlquiler.setEnabled(False)
            self.ui.btnRegistrarAlquiler.setEnabled(False)
        elif ancho == 500:
            nuevoAncho = 0
        try:
            self.animacion = QPropertyAnimation(
                self.ui.frameNueve_2, b"minimumWidth")
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(nuevoAncho)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()
        except:
            self.animacion.setStartValue(0)
            self.animacion.setEndValue(0)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()

    def menuModificarAlquiler(self):
        seleccion = self.ui.tblAlquiler.selectedItems()
        if seleccion == []:
            self.mensaje.setText("¡Selecciona una fila para modificar!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif seleccion != []:
            seleccion = [dato.text() for dato in seleccion]
            datos = self.alquiler.buscarAlquiler(int(seleccion[0]))
            self.auxiliarId = int(seleccion[0])
            self.traerDatosAlquiler(datos)
            self.ui.tblAlquiler.clearSelection()
            ancho = self.ui.frameNueve_2.width()
            if ancho == 0:
                nuevoAncho = 500
                self.ui.paginasAlquileres.setCurrentWidget(
                    self.ui.alquileresModificar)
                self.ui.btnModificarAlquiler.setEnabled(False)
                self.ui.btnEliminarAlquiler.setEnabled(False)
                self.ui.btnRegistrarAlquiler.setEnabled(False)
            elif ancho == 500:
                nuevoAncho = 0
            try:
                self.animacion = QPropertyAnimation(
                    self.ui.frameNueve_2, b"minimumWidth")
                self.animacion.setStartValue(ancho)
                self.animacion.setEndValue(nuevoAncho)
                self.animacion.setDuration(350)
                self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
                self.animacion.start()
            except:
                self.animacion.setStartValue(0)
                self.animacion.setEndValue(0)
                self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
                self.animacion.start()

    def traerDatosAlquiler(self, datos):
        self.ui.txtDocumentoModificarAlquiler.setText(datos[1])
        self.ui.cmbPropiedadModificarAlquiler.setCurrentIndex(datos[2])
        self.ui.txtReservaModificarAlquiler.setText(datos[3])
        self.ui.txtCantidadPersonasModificarAlquiler.setText(datos[4])
        self.ui.txtCantidadMascotasModificarAlquiler.setText(datos[5])
        fechaLlegada = self.auxiliarConvertir.convertirListaFecha(datos[6])
        self.ui.dtFechaLlegadaModificarAlquiler.setDate(
            QDate(int(fechaLlegada[2]), int(fechaLlegada[1]), int(fechaLlegada[0])))
        self.ui.txtHoraLlegadaModificarAlquiler.setText(datos[7])
        fechaSalida = self.auxiliarConvertir.convertirListaFecha(datos[8])
        self.ui.dtFechaSalidaModificarAlquiler.setDate(
            QDate(int(fechaSalida[2]), int(fechaSalida[1]), int(fechaSalida[0])))
        self.ui.txtHoraSalidaModificarAlquiler.setText(datos[9])
        self.ui.txtPrecioModificarAlquiler.setText(str(datos[10]))

    def cerrarMenuRegistrarAlquiler(self):
        self.animacion = QPropertyAnimation(
            self.ui.frameNueve_2, b"minimumWidth")
        self.animacion.setStartValue(500)
        self.animacion.setEndValue(0)
        self.animacion.setDuration(350)
        self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
        self.animacion.start()
        self.ui.btnModificarAlquiler.setEnabled(True)
        self.ui.btnEliminarAlquiler.setEnabled(True)
        self.ui.btnRegistrarAlquiler.setEnabled(True)
        self.resetearMenuRegistrarAlquiler()

    def cerrarMenuModificarAlquiler(self):
        self.animacion = QPropertyAnimation(
            self.ui.frameNueve_2, b"minimumWidth")
        self.animacion.setStartValue(500)
        self.animacion.setEndValue(0)
        self.animacion.setDuration(350)
        self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
        self.animacion.start()
        self.ui.btnModificarAlquiler.setEnabled(True)
        self.ui.btnEliminarAlquiler.setEnabled(True)
        self.ui.btnRegistrarAlquiler.setEnabled(True)
        self.resetearMenuModificarAlquiler()

    def resetearMenuRegistrarAlquiler(self):
        self.ui.txtDocumentoRegistroAlquiler.clear()
        self.ui.cmbPropiedadRegistroAlquiler.setCurrentIndex(0)
        self.ui.txtReservaRegistroAlquiler.clear()
        self.ui.txtCantidadPersonasRegistroAlquiler.clear()
        self.ui.txtCantidadMascotasRegistroAlquiler.clear()
        self.ui.dtFechaLlegadaRegistroAlquiler.setDate(QDate(2000, 1, 1))
        self.ui.txtHoraLlegadaRegistroAlquiler.clear()
        self.ui.dtFechaSalidaRegistroAlquiler.setDate(QDate(2000, 1, 1))
        self.ui.txtHoraSalidaRegistroAlquiler.clear()
        self.ui.txtPrecioRegistroAlquiler.clear()
        self.ui.txtDocumentoRegistroAlquiler.clearFocus()
        self.ui.cmbPropiedadRegistroAlquiler.clearFocus()
        self.ui.txtReservaRegistroAlquiler.clearFocus()
        self.ui.txtCantidadPersonasRegistroAlquiler.clearFocus()
        self.ui.txtCantidadMascotasRegistroAlquiler.clearFocus()
        self.ui.dtFechaLlegadaRegistroAlquiler.clearFocus()
        self.ui.txtHoraLlegadaRegistroAlquiler.clearFocus()
        self.ui.dtFechaSalidaRegistroAlquiler.clearFocus()
        self.ui.txtHoraSalidaRegistroAlquiler.clearFocus()
        self.ui.txtPrecioRegistroAlquiler.clearFocus()

    def resetearMenuModificarAlquiler(self):
        self.ui.txtDocumentoModificarAlquiler.clear()
        self.ui.cmbPropiedadModificarAlquiler.setCurrentIndex(0)
        self.ui.txtReservaModificarAlquiler.clear()
        self.ui.txtCantidadPersonasModificarAlquiler.clear()
        self.ui.txtCantidadMascotasModificarAlquiler.clear()
        self.ui.dtFechaLlegadaModificarAlquiler.setDate(QDate(2000, 1, 1))
        self.ui.txtHoraLlegadaModificarAlquiler.clear()
        self.ui.dtFechaSalidaModificarAlquiler.setDate(QDate(2000, 1, 1))
        self.ui.txtHoraSalidaModificarAlquiler.clear()
        self.ui.txtPrecioModificarAlquiler.clear()
        self.ui.txtDocumentoModificarAlquiler.clearFocus()
        self.ui.cmbPropiedadModificarAlquiler.clearFocus()
        self.ui.txtReservaModificarAlquiler.clearFocus()
        self.ui.txtCantidadPersonasModificarAlquiler.clearFocus()
        self.ui.txtCantidadMascotasModificarAlquiler.clearFocus()
        self.ui.dtFechaLlegadaModificarAlquiler.clearFocus()
        self.ui.txtHoraLlegadaModificarAlquiler.clearFocus()
        self.ui.dtFechaSalidaModificarAlquiler.clearFocus()
        self.ui.txtHoraSalidaModificarAlquiler.clearFocus()
        self.ui.txtPrecioModificarAlquiler.clearFocus()
    ############################################################################

    # CLIENTE
    ############################################################################

    def formularioRegistroCliente(self):
        self.cliente.apellido = self.ui.txtApellidoRegistroCliente.text()
        self.cliente.nombre = self.ui.txtNombreRegistroCliente.text()
        self.cliente.numeroDocumento = self.ui.txtDocumentoRegistroCliente.text()
        self.cliente.tipoDocumento = self.ui.cmbTipoDocumentoRegistroCliente.currentText()
        self.cliente.tipoProvincia = self.ui.cmbProvinciaRegistroCliente.currentText()
        self.cliente.ciudadOrigen = self.ui.txtCiudadRegistroCliente.text()
        self.cliente.celular = self.ui.txtCelularRegistroCliente.text()
        self.cliente.correo = self.ui.txtCorreoRegistroCliente.text()
        retorno = self.cliente.registrarCliente(self.cliente.apellido, self.cliente.nombre, self.cliente.numeroDocumento, self.cliente.tipoDocumento,
                                                self.cliente.tipoProvincia, self.cliente.ciudadOrigen, self.cliente.celular, self.cliente.correo)
        if retorno == True:
            self.mostrarTablaCliente()
            self.contadorCliente()
            self.cerrarMenuRegistrarCliente()

    def formularioModificarCliente(self):
        self.cliente.apellido = self.ui.txtApellidoModificarCliente.text()
        self.cliente.nombre = self.ui.txtNombreModificarCliente.text()
        self.cliente.numeroDocumento = self.ui.txtDocumentoModificarCliente.text()
        self.cliente.tipoDocumento = self.ui.cmbTipoDocumentoModificarCliente.currentText()
        self.cliente.tipoProvincia = self.ui.cmbProvinciaModificarCliente.currentText()
        self.cliente.ciudadOrigen = self.ui.txtCiudadModificarCliente.text()
        self.cliente.celular = self.ui.txtCelularModificarCliente.text()
        self.cliente.correo = self.ui.txtCorreoModificarCliente.text()
        retorno = self.cliente.modificarCliente(self.auxiliarId, self.cliente.apellido, self.cliente.nombre, self.cliente.numeroDocumento,
                                                self.cliente.tipoDocumento, self.cliente.tipoProvincia, self.cliente.ciudadOrigen, self.cliente.celular, self.cliente.correo)
        if retorno == True:
            self.mostrarTablaCliente()
            self.contadorCliente()
            self.cerrarMenuModiciarCliente()
            self.mostrarTablaAlquiler()

    def eliminarCliente(self):
        seleccion = self.ui.tblClientes.selectedItems()
        if seleccion == []:
            self.mensaje.setText("¡Selecciona una fila para eliminar!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif seleccion != []:
            seleccion = [dato.text() for dato in seleccion]
            self.ui.tblClientes.clearSelection()
            test = QMessageBox.question(
                self, "Alerta", f"¿Está seguro de eliminar a {seleccion[2]} {seleccion[1]}?", QMessageBox.Yes | QMessageBox.No)
            if test == QMessageBox.Yes:
                self.cliente.eliminarCliente(seleccion[0])
                self.mostrarTablaCliente()
                self.contadorCliente()
            elif test == QMessageBox.No:
                pass

    def buscarClienteDocumento(self):
        documento = self.ui.txtBuscarCliente.text()
        if documento != "":
            datos = self.cliente.buscarClienteDocumento(documento)
            if datos == []:
                self.mensaje.setText(
                    "No se encontro ningun cliente con ese documento")
                self.mensaje.setIcon(QMessageBox.Warning)
                x = self.mensaje.exec_()
                self.resetearBusquedaCliente()
                self.mostrarTablaCliente()
            else:
                i = len(datos)
                self.ui.tblClientes.setRowCount(i)
                filaTabla = 0
                for fila in datos:
                    self.ui.tblClientes.setItem(
                        filaTabla, 0, QtWidgets.QTableWidgetItem(str(fila[0])))
                    self.ui.tblClientes.setItem(
                        filaTabla, 1, QtWidgets.QTableWidgetItem(fila[1]))
                    self.ui.tblClientes.setItem(
                        filaTabla, 2, QtWidgets.QTableWidgetItem(fila[2]))
                    self.ui.tblClientes.setItem(
                        filaTabla, 3, QtWidgets.QTableWidgetItem(fila[3]))
                    self.ui.tblClientes.setItem(
                        filaTabla, 4, QtWidgets.QTableWidgetItem(fila[4]))
                    self.ui.tblClientes.setItem(
                        filaTabla, 5, QtWidgets.QTableWidgetItem(fila[5]))
                    self.ui.tblClientes.setItem(
                        filaTabla, 6, QtWidgets.QTableWidgetItem(fila[6]))
                    self.ui.tblClientes.setItem(
                        filaTabla, 7, QtWidgets.QTableWidgetItem(fila[7]))
                    self.ui.tblClientes.setItem(
                        filaTabla, 8, QtWidgets.QTableWidgetItem(fila[8]))
                filaTabla += 1
        elif documento == "":
            self.mensaje.setText("¡Debe ingresar un documento!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
            self.mostrarTablaCliente()

    # CLIENTE AUXILIARES

    def mostrarTablaCliente(self):
        datos = self.cliente.mostrarCliente()
        i = len(datos)
        self.ui.tblClientes.setRowCount(i)
        filaTabla = 0
        for fila in datos:
            self.ui.tblClientes.setItem(
                filaTabla, 0, QtWidgets.QTableWidgetItem(str(fila[0])))
            self.ui.tblClientes.setItem(
                filaTabla, 1, QtWidgets.QTableWidgetItem(fila[1]))
            self.ui.tblClientes.setItem(
                filaTabla, 2, QtWidgets.QTableWidgetItem(fila[2]))
            self.ui.tblClientes.setItem(
                filaTabla, 3, QtWidgets.QTableWidgetItem(fila[3]))
            self.ui.tblClientes.setItem(
                filaTabla, 4, QtWidgets.QTableWidgetItem(fila[4]))
            self.ui.tblClientes.setItem(
                filaTabla, 5, QtWidgets.QTableWidgetItem(fila[5]))
            self.ui.tblClientes.setItem(
                filaTabla, 6, QtWidgets.QTableWidgetItem(fila[6]))
            self.ui.tblClientes.setItem(
                filaTabla, 7, QtWidgets.QTableWidgetItem(fila[7]))
            self.ui.tblClientes.setItem(
                filaTabla, 8, QtWidgets.QTableWidgetItem(fila[8]))
            filaTabla += 1

    def menuRegistrarCliente(self):
        ancho = self.ui.frameNueve.width()
        if ancho == 0:
            nuevoAncho = 500
            self.ui.paginasCliente.setCurrentWidget(self.ui.clientesRegistrar)
            self.ui.btnModificarCliente.setEnabled(False)
            self.ui.btnEliminarCliente.setEnabled(False)
            self.ui.btnRegistrarCliente.setEnabled(False)
        elif ancho == 500:
            nuevoAncho = 0
        try:
            self.animacion = QPropertyAnimation(
                self.ui.frameNueve, b"minimumWidth")
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(nuevoAncho)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()
        except:
            self.animacion.setStartValue(0)
            self.animacion.setEndValue(0)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()

    def menuModificarCliente(self):
        seleccion = self.ui.tblClientes.selectedItems()
        if seleccion == []:
            self.mensaje.setText("¡Selecciona una fila para modificar!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif seleccion != []:
            seleccion = [dato.text() for dato in seleccion]
            datos = self.cliente.buscarClienteId(int(seleccion[0]))
            self.auxiliarId = int(seleccion[0])
            self.traerDatosCliente(datos)
            self.ui.tblClientes.clearSelection()
            ancho = self.ui.frameNueve.width()
            if ancho == 0:
                nuevoAncho = 500
                self.ui.paginasCliente.setCurrentWidget(
                    self.ui.clientesModificar)
                self.ui.btnModificarCliente.setEnabled(False)
                self.ui.btnEliminarCliente.setEnabled(False)
                self.ui.btnRegistrarCliente.setEnabled(False)
            elif ancho == 500:
                nuevoAncho = 0
            try:
                self.animacion = QPropertyAnimation(
                    self.ui.frameNueve, b"minimumWidth")
                self.animacion.setStartValue(ancho)
                self.animacion.setEndValue(nuevoAncho)
                self.animacion.setDuration(350)
                self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
                self.animacion.start()
            except:
                self.animacion.setStartValue(0)
                self.animacion.setEndValue(0)
                self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
                self.animacion.start()

    def traerDatosCliente(self, datos):
        self.ui.txtApellidoModificarCliente.setText(datos[1])
        self.ui.txtNombreModificarCliente.setText(datos[2])
        self.ui.txtDocumentoModificarCliente.setText(datos[3])
        self.ui.cmbTipoDocumentoModificarCliente.setCurrentIndex(datos[4])
        self.ui.cmbProvinciaModificarCliente.setCurrentIndex(datos[5])
        self.ui.txtCiudadModificarCliente.setText(datos[6])
        self.ui.txtCelularModificarCliente.setText(datos[7])
        self.ui.txtCorreoModificarCliente.setText(datos[8])

    def cerrarMenuRegistrarCliente(self):
        self.animacion = QPropertyAnimation(
            self.ui.frameNueve, b"minimumWidth")
        self.animacion.setStartValue(500)
        self.animacion.setEndValue(0)
        self.animacion.setDuration(350)
        self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
        self.animacion.start()
        self.ui.btnModificarCliente.setEnabled(True)
        self.ui.btnEliminarCliente.setEnabled(True)
        self.ui.btnRegistrarCliente.setEnabled(True)
        self.resetearMenuRegistrarCliente()

    def cerrarMenuModiciarCliente(self):
        self.animacion = QPropertyAnimation(
            self.ui.frameNueve, b"minimumWidth")
        self.animacion.setStartValue(500)
        self.animacion.setEndValue(0)
        self.animacion.setDuration(350)
        self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
        self.animacion.start()
        self.ui.btnModificarCliente.setEnabled(True)
        self.ui.btnEliminarCliente.setEnabled(True)
        self.ui.btnRegistrarCliente.setEnabled(True)
        self.resetearMenuModificarCliente()

    def resetearMenuRegistrarCliente(self):
        self.ui.txtApellidoRegistroCliente.clear()
        self.ui.txtNombreRegistroCliente.clear()
        self.ui.cmbTipoDocumentoRegistroCliente.setCurrentIndex(0)
        self.ui.txtDocumentoRegistroCliente.clear()
        self.ui.cmbProvinciaRegistroCliente.setCurrentIndex(0)
        self.ui.txtCiudadRegistroCliente.clear()
        self.ui.txtCorreoRegistroCliente.clear()
        self.ui.txtCelularRegistroCliente.clear()
        self.ui.txtApellidoRegistroCliente.clearFocus()
        self.ui.txtNombreRegistroCliente.clearFocus()
        self.ui.cmbTipoDocumentoRegistroCliente.clearFocus()
        self.ui.txtDocumentoRegistroCliente.clearFocus()
        self.ui.cmbProvinciaRegistroCliente.clearFocus()
        self.ui.txtCiudadRegistroCliente.clearFocus()
        self.ui.txtCorreoRegistroCliente.clearFocus()
        self.ui.txtCelularRegistroCliente.clearFocus()

    def resetearMenuModificarCliente(self):
        self.ui.txtApellidoModificarCliente.clear()
        self.ui.txtNombreModificarCliente.clear()
        self.ui.txtDocumentoModificarCliente.clear()
        self.ui.cmbTipoDocumentoModificarCliente.setCurrentIndex(0)
        self.ui.cmbProvinciaModificarCliente.setCurrentIndex(0)
        self.ui.txtCiudadModificarCliente.clear()
        self.ui.txtCelularModificarCliente.clear()
        self.ui.txtCorreoModificarCliente.clear()
        self.ui.txtApellidoModificarCliente.clearFocus()
        self.ui.txtNombreModificarCliente.clearFocus()
        self.ui.txtDocumentoModificarCliente.clearFocus()
        self.ui.cmbTipoDocumentoModificarCliente.clearFocus()
        self.ui.cmbProvinciaModificarCliente.clearFocus()
        self.ui.txtCiudadModificarCliente.clearFocus()
        self.ui.txtCelularModificarCliente.clearFocus()
        self.ui.txtCorreoModificarCliente.clearFocus()
    ############################################################################

    # AUXILIARES EN GENERAL
    ############################################################################
    def menuIzquierdo(self):
        ancho = self.ui.frmMenuIzquierdo.width()
        if ancho == 50:
            nuevoAncho = 180
            self.ui.btnMenu.setIcon(QtGui.QIcon(":Iconos/anterior.png"))
        elif ancho == 180:
            nuevoAncho = 50
            self.ui.btnMenu.setIcon(QtGui.QIcon(":Iconos/menu.png"))
        try:
            self.animacion = QPropertyAnimation(
                self.ui.frmMenuIzquierdo, b"minimumWidth")
            self.animacion.setStartValue(ancho)
            self.animacion.setEndValue(nuevoAncho)
            self.animacion.setDuration(350)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()
        except:
            self.ui.btnMenu.setIcon(QtGui.QIcon(":Iconos/menu.png"))
            self.animacion.setStartValue(50)
            self.animacion.setEndValue(50)
            self.animacion.setEasingCurve(QEasingCurve.InOutCirc)
            self.animacion.start()

    def mostrarProvincias(self):
        datos = self.auxiliarProvincia.listarProvincias()
        for i in datos:
            self.ui.cmbProvinciaRegistroCliente.addItem(i[0])
            self.ui.cmbProvinciaModificarCliente.addItem(i[0])

    def mostrarTipoDocumento(self):
        datos = self.auxiliarDocumento.listarTipoDocumento()
        for i in datos:
            self.ui.cmbTipoDocumentoRegistroCliente.addItem(i[0])
            self.ui.cmbTipoDocumentoModificarCliente.addItem(i[0])

    def mostrarInmueble(self):
        datos = self.auxiliarInmueble.listarTipoInmueble()
        for i in datos:
            self.ui.cmbPropiedadRegistroAlquiler.addItem(i[0])
            self.ui.cmbPropiedadModificarAlquiler.addItem(i[0])

    def mostrarFechaActual(self):
        self.ui.txtReservaRegistroAlquiler.setText(
            datetime.today().strftime('%d/%m/%Y'))

    def contadorCliente(self):
        contador = self.cliente.contadorCliente()
        self.ui.lblTotalClientes.setText(
            f"Total de clientes registrados: {contador}")

    def cerrarSesion(self):
        self.login = Login()
        self.login.show()
        self.close()

    def resetearBusquedaAlquiler(self):
        self.ui.txtBuscarAlquiler.clear()
        self.ui.txtBuscarAlquiler.clearFocus()

    def resetearBusquedaCliente(self):
        self.ui.txtBuscarCliente.clear()
        self.ui.txtBuscarCliente.clearFocus()

    ############################################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
