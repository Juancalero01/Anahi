from Iconos import iconos
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 600)
        Login.setMinimumSize(QtCore.QSize(400, 600))
        Login.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        Login.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/logo.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        self.widget_central = QtWidgets.QWidget(Login)
        self.widget_central.setObjectName("widget_central")
        self.img_fondo = QtWidgets.QLabel(self.widget_central)
        self.img_fondo.setGeometry(QtCore.QRect(0, 0, 421, 600))
        self.img_fondo.setStyleSheet("QLineEdit{\n"
                                     "    background-color: transparent;\n"
                                     "    border: none;\n"
                                     "    border-bottom: 1px solid #fff;\n"
                                     "    color: #fff;\n"
                                     "    padding-bottom: 5px;\n"
                                     "}\n"
                                     "QLineEdit:focus {\n"
                                     "        border-bottom: 1px solid #b5b5b5;\n"
                                     "}\n"
                                     "")
        self.img_fondo.setText("")
        self.img_fondo.setPixmap(QtGui.QPixmap("Imagenes/fondoLogin.PNG"))
        self.img_fondo.setScaledContents(False)
        self.img_fondo.setObjectName("img_fondo")
        self.btnPagina = QtWidgets.QPushButton(self.widget_central)
        self.btnPagina.setGeometry(QtCore.QRect(100, 30, 191, 121))
        self.btnPagina.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPagina.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPagina.setStyleSheet("QPushButton{\n"
                                     "background-color: transparent;\n"
                                     "border: none;\n"
                                     "}\n"
                                     "")
        self.btnPagina.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagenes/login.PNG"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPagina.setIcon(icon1)
        self.btnPagina.setIconSize(QtCore.QSize(200, 200))
        self.btnPagina.setAutoRepeat(False)
        self.btnPagina.setAutoExclusive(False)
        self.btnPagina.setObjectName("btnPagina")
        self.txtUsuario = QtWidgets.QLineEdit(self.widget_central)
        self.txtUsuario.setGeometry(QtCore.QRect(80, 239, 240, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setStyleSheet("QLineEdit{\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "    border-bottom: 1px solid #fff;\n"
                                      "    color: #fff;\n"
                                      "    padding-bottom: 5px;\n"
                                      "}\n"
                                      "QLineEdit:focus {\n"
                                      "        border-bottom: 1px solid #b5b5b5;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "")
        self.txtUsuario.setMaxLength(15)
        self.txtUsuario.setFrame(True)
        self.txtUsuario.setClearButtonEnabled(True)
        self.txtUsuario.setObjectName("txtUsuario")
        self.btnIngresar = QtWidgets.QPushButton(self.widget_central)
        self.btnIngresar.setGeometry(QtCore.QRect(80, 450, 240, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnIngresar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnIngresar.setStyleSheet("QPushButton{\n"
                                       "border:none;\n"
                                       "border-radius: 5px;\n"
                                       "background-color: #004A7C;\n"
                                       "color:#fff;\n"
                                       "padding-left: 15px;\n"
                                       "padding-right: 15px;\n"
                                       "height: 40px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: #1C4C96;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.btnIngresar.setObjectName("btnIngresar")
        self.txtClave = QtWidgets.QLineEdit(self.widget_central)
        self.txtClave.setGeometry(QtCore.QRect(80, 330, 240, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtClave.setFont(font)
        self.txtClave.setStyleSheet("QLineEdit{\n"
                                    "    background-color: transparent;\n"
                                    "    border: none;\n"
                                    "    border-bottom: 1px solid #fff;\n"
                                    "    color: #fff;\n"
                                    "    padding-bottom: 5px;\n"
                                    "}\n"
                                    "QLineEdit:focus {\n"
                                    "        border-bottom: 1px solid #b5b5b5;\n"
                                    "}\n"
                                    "")
        self.txtClave.setMaxLength(20)
        self.txtClave.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtClave.setClearButtonEnabled(True)
        self.txtClave.setObjectName("txtClave")
        Login.setCentralWidget(self.widget_central)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.txtUsuario.setPlaceholderText(_translate("Login", "Usuario"))
        self.btnIngresar.setText(_translate("Login", "Ingresar"))
        self.txtClave.setPlaceholderText(_translate("Login", "Contraseña"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
