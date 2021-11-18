from BaseDatos.conexion import DataBase

db = DataBase()


class TipoInmueble:

    def listarTipoInmueble(self):
        sql = """SELECT Nombre FROM Inmueble"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def buscarIdInmueble(self, nombre):
        sql = f"""SELECT IDInmueble FROM Inmueble WHERE Nombre = '{nombre}'"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos
