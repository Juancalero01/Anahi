from Usuario.datosUsuario import DatosUsuario
dbUsuario = DatosUsuario()


class Usuario:
    def __init__(self):
        self.usuario = None
        self.contrasena = None

    def comprobarLogin(self, usuario, contrasena):
        datos = dbUsuario.comprobarLogin(usuario, contrasena)
        return datos
