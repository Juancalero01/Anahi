from BaseDatos.conexion import DataBase

db = DataBase()


class DatosCliente:

    # REGISTRAR MODIFICAR ELIMINAR

    def registrarCliente(self, apellido, nombre, numeroDocumento, tipoDocumento, provincia, ciudad, celular, correo):
        sql = f"""INSERT INTO Cliente(Apellido,Nombre,NroDocumento,IDTipoDocumento,IDProvincia,Ciudad,Celular,Correo)
        VALUES ('{apellido}','{nombre}','{numeroDocumento}',{tipoDocumento},{provincia},'{ciudad}','{celular}','{correo}')"""
        db.consulta(sql)

    def modificarCliente(self, id, apellido, nombre, numeroDocumento, tipoDocumento, provincia, ciudad, celular, correo):
        sql = f"""UPDATE cliente SET Apellido='{apellido}',Nombre='{nombre}',NroDocumento='{numeroDocumento}',IDTipoDocumento={tipoDocumento},IDProvincia={provincia},Ciudad='{ciudad}',Celular='{celular}',Correo='{correo}'
        WHERE IDCliente={id}"""
        db.consulta(sql)

    def eliminarCliente(self, id):
        sql = f"""DELETE FROM Cliente WHERE IDCliente = {id}"""
        db.consulta(sql)

    # BUSCAR Y MOSTRAR TABLA

    def buscarClienteId(self, id):
        sql = f"""SELECT * FROM Cliente WHERE IDCliente = {id}"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def buscarClienteDocumento(self, documento):
        sql = f"""SELECT c.IDCliente,c.Apellido,c.Nombre,c.NroDocumento,td.Nombre,p.Provincia,c.Ciudad,c.Celular,c.Correo
        FROM Cliente c, TipoDocumento td, Provincia p
        WHERE c.IDTipoDocumento=td.IDTipoDocumento AND c.IDProvincia=p.IDProvincia AND c.NroDocumento = '{documento}'"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def mostrarCliente(self):
        sql = """SELECT c.IDCliente,c.Apellido,c.Nombre,c.NroDocumento,td.Nombre,p.Provincia,c.Ciudad,c.Celular,c.Correo
        FROM Cliente c, TipoDocumento td, Provincia p WHERE c.IDTipoDocumento = td.IDTipoDocumento AND c.IDProvincia = p.IDProvincia"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def contadorCliente(self):
        sql = """SELECT COUNT(IDCliente) from Cliente"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def buscarIdClienteAlquiler(self, documento):
        sql = f"""SELECT IDCliente FROM Cliente WHERE NroDocumento = '{documento}'"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def comprobarDocumentoCliente(self, numeroDocumento):
        sql = f"""SELECT * FROM Cliente WHERE NroDocumento = '{numeroDocumento}'"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos
