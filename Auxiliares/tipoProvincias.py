from BaseDatos.conexion import DataBase

db = DataBase()


class TipoProvincia:

    def listarProvincias(self):
        sql = """SELECT Provincia FROM Provincia"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos

    def buscarIdProvincia(self, provincia):
        sql = f"""SELECT IDProvincia FROM Provincia WHERE Provincia = '{provincia}'"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos
