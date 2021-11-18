from Cliente.datosCliente import DatosCliente
from Auxiliares.tipoDocumento import TipoDocumento
from Auxiliares.tipoProvincias import TipoProvincia
from Otros.tipoConversion import TipoConversion
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
dbCliente = DatosCliente()
convertir = TipoConversion()
tipoDoc = TipoDocumento()
tipoProv = TipoProvincia()


class Cliente:
    def __init__(self):
        self.apellido = None
        self.nombre = None
        self.numeroDocumento = None
        self.tipoDocumento = None
        self.tipoProvincia = None
        self.ciudadOrigen = None
        self.celular = None
        self.correo = None
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Alerta")
        self.mensaje.setWindowIcon(QtGui.QIcon(":Iconos/logo.png"))

    def registrarCliente(self, apellido, nombre, numeroDocumento, tipoDocumento, provincia, ciudad, celular, correo):
        tipoDocumento = tipoDoc.buscarIdTipoDocumento(tipoDocumento)
        provincia = tipoProv.buscarIdProvincia(provincia)
        tipoDocumento = convertir.convertirLista(tipoDocumento)
        provincia = convertir.convertirLista(provincia)
        retorno = self.comprobarDatosCliente(
            apellido, nombre, numeroDocumento, tipoDocumento, provincia, celular)
        if retorno == True:
            retorno = self.comprobarDocumentoCliente(numeroDocumento)
            if retorno == True:
                dbCliente.registrarCliente(
                    apellido, nombre, numeroDocumento, tipoDocumento, provincia, ciudad, celular, correo)
                self.mensaje.setText("¡Registro exitoso!")
                self.mensaje.setIcon(QMessageBox.Warning)
                x = self.mensaje.exec_()
            elif retorno == False:
                self.mensaje.setText(
                    "¡Ya existe un cliente con ese documento!")
                self.mensaje.setIcon(QMessageBox.Warning)
                x = self.mensaje.exec_()
        return retorno

    def modificarCliente(self, id, apellido, nombre, numeroDocumento, tipoDocumento, provincia, ciudad, celular, correo):
        tipoDocumento = tipoDoc.buscarIdTipoDocumento(tipoDocumento)
        provincia = tipoProv.buscarIdProvincia(provincia)
        tipoDocumento = convertir.convertirLista(tipoDocumento)
        provincia = convertir.convertirLista(provincia)
        retorno = self.comprobarDatosCliente(
            apellido, nombre, numeroDocumento, tipoDocumento, provincia, celular)
        if retorno == True:
            dbCliente.modificarCliente(
                id, apellido, nombre, numeroDocumento, tipoDocumento, provincia, ciudad, celular, correo)
            self.mensaje.setText("¡Actualizacion exitosa!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        elif retorno == False:
            self.mensaje.setText(
                "¡Ya existe un cliente con ese documento!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        return retorno

    def eliminarCliente(self, id):
        dbCliente.eliminarCliente(id)

    def buscarClienteDocumento(self, documento):
        datos = dbCliente.buscarClienteDocumento(documento)
        return datos

    def buscarClienteId(self, id):
        datos = dbCliente.buscarClienteId(id)
        datos = convertir.convertirListaTupla(datos)
        return datos

    def mostrarCliente(self):
        datos = dbCliente.mostrarCliente()
        return datos

    def contadorCliente(self):
        datos = dbCliente.contadorCliente()
        datos = convertir.convertirLista(datos)
        return datos

    def comprobarDocumentoCliente(self, numeroDocumento):
        datos = dbCliente.comprobarDocumentoCliente(numeroDocumento)
        if datos != []:
            paso = False
        elif datos == []:
            paso = True
        return paso

    def comprobarDatosCliente(self, apellido, nombre, numeroDocumento, tipoDocumento, provincia, celular):
        if apellido != "" and nombre != "" and numeroDocumento != "" and tipoDocumento != 0 and provincia != "Provincia" and celular != "":
            paso = True
        else:
            self.mensaje.setText(
                "¡Debe ingresar los datos necesarios (Apellido, Nombre, Número de documento, Tipo de documento, Provincia y Celular!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
            paso = False
        return paso
