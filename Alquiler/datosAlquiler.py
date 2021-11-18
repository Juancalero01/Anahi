from BaseDatos.conexion import DataBase

db = DataBase()


class DatosAlquiler:

    def registrarAlquiler(self, idCliente, idInmueble, fechaAlquiler, cantidadPersona, cantidadMascota, fechaLlegada, horaLlegada, fechaSalida, horaSalida, precio):
        sql = f"""INSERT INTO Alquiler(IDCliente,IDInmueble,FechaAlquiler,CantidadPersona,CantidadMascota,FechaLlegada,HoraLlegada,FechaSalida,HoraSalida,Precio)
        VALUES({idCliente},{idInmueble},'{fechaAlquiler}','{cantidadPersona}','{cantidadMascota}','{fechaLlegada}','{horaLlegada}','{fechaSalida}','{horaSalida}','{precio}')"""
        db.consulta(sql)

    def modificarAlquiler(self, id, idCliente, idInmueble, fechaAlquiler, cantidadPersona, cantidadMascota, fechaLlegada, horaLlegada, fechaSalida, horaSalida, precio):
        sql = f"""UPDATE Alquiler SET IDCliente={idCliente},IDInmueble={idInmueble},FechaAlquiler='{fechaAlquiler}',CantidadPersona='{cantidadPersona}',CantidadMascota='{cantidadMascota}',FechaLlegada='{fechaLlegada}',HoraLlegada='{horaLlegada}',FechaSalida='{fechaSalida}',HoraSalida='{horaSalida}',Precio='{precio}'
        WHERE IDAlquiler = {id}"""
        db.consulta(sql)

    def eliminarAlquiler(self, id):
        sql = f"""DELETE FROM Alquiler WHERE IDAlquiler = {id}"""
        db.consulta(sql)

    def buscarAlquilerDocumento(self, documento):
        sql = f"""SELECT a.IDAlquiler,c.Nombre,c.Apellido,i.Nombre,a.FechaAlquiler,a.CantidadPersona,a.CantidadMascota,a.FechaLlegada,a.HoraLlegada,a.FechaSalida,a.HoraSalida,a.Precio
        FROM Cliente c, Alquiler a, Inmueble i
        WHERE c.IDCliente = a.IDCliente AND i.IDInmueble= a.IDInmueble AND c.NroDocumento = '{documento}'"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def mostrarAlquiler(self):
        sql = """SELECT a.IDAlquiler,c.Nombre,c.Apellido,i.Nombre,a.FechaAlquiler,a.CantidadPersona,a.CantidadMascota,a.FechaLlegada,a.HoraLlegada,a.FechaSalida,a.HoraSalida,a.Precio
        FROM Cliente c, Alquiler a, Inmueble i WHERE c.IDCliente = a.IDCliente AND i.IDInmueble= a.IDInmueble"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def buscarAlquiler(self, id):
        sql = f"""SELECT a.IDAlquiler,c.NroDocumento, a.IDInmueble, a.FechaAlquiler,a.CantidadPersona,a.CantidadMascota,a.FechaLlegada,a.HoraLlegada,a.FechaSalida,a.HoraSalida,a.Precio
        FROM Cliente c, Alquiler a WHERE c.IDCliente = a.IDCliente AND a.IDAlquiler = {id}"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def comprobarFechaIngreso(self, fechaLlegada, inmueble):
        sql = f"""SELECT * FROM Alquiler WHERE FechaLlegada = '{fechaLlegada}' and IDInmueble = {inmueble}"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def comprobarIdClienteAlquiler(self, id):
        sql = f"""SELECT * FROM Cliente WHERE IDCliente = {id}"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def comprobarFechaRango(self, fechaLlegada, fechaSalida, inmueble):
        sql = f"""SELECT * FROM Alquiler WHERE FechaSalida >= '{fechaLlegada}' AND FechaLlegada <= '{fechaSalida}' AND IDInmueble = {inmueble}"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos
