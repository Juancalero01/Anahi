from BaseDatos.conexion import DataBase

db = DataBase()


class TipoDocumento:

    def listarTipoDocumento(self):
        sql = """SELECT Nombre FROM TipoDocumento"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def buscarIdTipoDocumento(self, tipoDocumento):
        sql = f"""SELECT IDTipoDocumento FROM TipoDocumento WHERE Nombre = '{tipoDocumento}'"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

