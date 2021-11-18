from BaseDatos.conexion import DataBase

db = DataBase()


class DatosUsuario:
    def comprobarLogin(self, usuario, contrasena):
        sql = f"""SELECT * FROM Usuario WHERE Usuario = '{usuario}' AND Contraseña = '{contrasena}'"""
        datos = db.consulta(sql)
        datos = datos.fetchall()
        return datos
