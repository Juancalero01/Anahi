from Alquiler.datosAlquiler import DatosAlquiler
from Auxiliares.tipoDocumento import TipoDocumento
from Auxiliares.tipoInmueble import TipoInmueble
from Otros.tipoConversion import TipoConversion
from Cliente.datosCliente import DatosCliente
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
dbAlquiler = DatosAlquiler()
convertir = TipoConversion()
tipoDoc = TipoDocumento()
tipoInm = TipoInmueble()
cliente = DatosCliente()


class Alquiler:
    def __init__(self):
        self.cliente = None
        self.propiedad = None
        self.fechaAlquiler = None
        self.cantidadPersona = None
        self.cantidadMascota = None
        self.fechaLlegada = None
        self.horaLlegada = None
        self.fechaSalida = None
        self.horaSalida = None
        self.precio = None
        self.mensaje = QMessageBox()
        self.mensaje.setWindowTitle("Alerta")
        self.mensaje.setWindowIcon(QtGui.QIcon(":Iconos/logo.png"))

    def registrarAlquiler(self, idCliente, idInmueble, fechaAlquiler, cantidadPersona, cantidadMascota, fechaLlegada, horaLlegada, fechaSalida, horaSalida, precio):
        idInmueble = tipoInm.buscarIdInmueble(idInmueble)
        idInmueble = convertir.convertirLista(idInmueble)
        idCliente = cliente.buscarIdClienteAlquiler(idCliente)
        idCliente = convertir.convertirLista(idCliente)
        retorno = self.comprobarDatosAlquiler(
            idCliente, idInmueble, fechaAlquiler, cantidadPersona, cantidadMascota, fechaLlegada, fechaSalida)
        if retorno == True:
            retorno = self.comprobarIdClienteAlquiler(idCliente)
            if retorno == True:
                retorno = self.comprobarRangoAlquiler(
                    fechaLlegada, fechaSalida, idInmueble)
                if retorno == True:
                    dbAlquiler.registrarAlquiler(idCliente, idInmueble, fechaAlquiler, cantidadPersona,
                                                 cantidadMascota, fechaLlegada, horaLlegada, fechaSalida, horaSalida, precio)
                    self.mensaje.setText("¡Registro exitoso!")
                    self.mensaje.setIcon(QMessageBox.Warning)
                    x = self.mensaje.exec_()
                elif retorno == False:
                    self.mensaje.setText(
                        "¡Ya existe un alquiler en esas fechas o en esa propiedad!")
                    self.mensaje.setIcon(QMessageBox.Warning)
                    x = self.mensaje.exec_()
        return retorno

    def modificarAlquiler(self, id, idCliente, idInmueble, fechaAlquiler, cantidadPersona, cantidadMascota, fechaLlegada, horaLlegada, fechaSalida, horaSalida, precio):
        idInmueble = tipoInm.buscarIdInmueble(idInmueble)
        idInmueble = convertir.convertirLista(idInmueble)
        idCliente = cliente.buscarIdClienteAlquiler(idCliente)
        idCliente = convertir.convertirLista(idCliente)
        retorno = self.comprobarDatosAlquiler(
            idCliente, idInmueble, fechaAlquiler, cantidadPersona, cantidadMascota, fechaLlegada, fechaSalida)
        if retorno == True:
            retorno = self.comprobarIdClienteAlquiler(idCliente)
            if retorno == True:
                retorno = self.comprobarRangoAlquiler(
                    fechaLlegada, fechaSalida, idInmueble)
                if retorno == True:
                    dbAlquiler.modificarAlquiler(id, idCliente, idInmueble, fechaAlquiler, cantidadPersona,
                                                 cantidadMascota, fechaLlegada, horaLlegada, fechaSalida, horaSalida, precio)
                    self.mensaje.setText("¡Modificación exitosa!")
                    self.mensaje.setIcon(QMessageBox.Warning)
                    x = self.mensaje.exec_()
                elif retorno == False:
                    self.mensaje.setText(
                        "¡Ya existe un alquiler en esas fechas o en esa propiedad!")
                    self.mensaje.setIcon(QMessageBox.Warning)
                    x = self.mensaje.exec_()
        return retorno

    def eliminarAlquiler(self, id):
        dbAlquiler.eliminarAlquiler(id)

    def buscarAlquilerDocumento(self, documento):
        datos = dbAlquiler.buscarAlquilerDocumento(documento)
        return datos

    def buscarAlquilerId(self, id):
        datos = dbAlquiler.buscarAlquilerId(id)
        datos = convertir.convertirListaTupla(datos)
        return datos

    def mostrarAlquiler(self):
        datos = dbAlquiler.mostrarAlquiler()
        return datos

    def buscarAlquiler(self, id):
        datos = dbAlquiler.buscarAlquiler(id)
        datos = convertir.convertirListaTupla(datos)
        return datos

    def comprobarDatosAlquiler(self, idCliente, idInmueble, fechaAlquiler, cantidadPersona, cantidadMascota, fechaLlegada, fechaSalida):
        if (idCliente != 0 or idCliente == 0) and idInmueble != 0 and fechaAlquiler != "" and cantidadPersona != "" and cantidadMascota != "" and fechaLlegada != "" and fechaSalida != "":
            paso = True
        else:
            self.mensaje.setText(
                "¡Debe ingresar los datos necesarios (Número de documento, Propiedad, Cantidad de personas y mascotas y las Fechas de Llegada y Salida!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
            paso = False
        return paso

    def comprobarIdClienteAlquiler(self, id):
        datos = dbAlquiler.comprobarIdClienteAlquiler(id)
        if datos != []:
            paso = True
        elif datos == []:
            paso = False
            self.mensaje.setText(
                "¡No existe ese documento!")
            self.mensaje.setIcon(QMessageBox.Warning)
            x = self.mensaje.exec_()
        return paso

    def comprobarRangoAlquiler(self, fechaLlegada, fechaSalida, idInmueble):
        datos = dbAlquiler.comprobarFechaRango(
            fechaLlegada, fechaSalida, idInmueble)
        if datos != []:
            paso = False
        elif datos == []:
            paso = True
        return paso
