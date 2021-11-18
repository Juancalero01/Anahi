

from Iconos import iconos
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Principal(object):
    def setupUi(self, Principal):
        Principal.setObjectName("Principal")
        Principal.resize(1273, 838)
        Principal.setMinimumSize(QtCore.QSize(1000, 650))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        Principal.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/logo.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Principal.setWindowIcon(icon)
        Principal.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameUno = QtWidgets.QFrame(self.centralwidget)
        self.frameUno.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameUno.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameUno.setObjectName("frameUno")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameUno)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameDos = QtWidgets.QFrame(self.frameUno)
        self.frameDos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameDos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDos.setObjectName("frameDos")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameDos)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frmMenuIzquierdo = QtWidgets.QFrame(self.frameDos)
        self.frmMenuIzquierdo.setMinimumSize(QtCore.QSize(50, 0))
        self.frmMenuIzquierdo.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frmMenuIzquierdo.setStyleSheet("QFrame{\n"
                                            "    background:#004A7C;\n"
                                            "}\n"
                                            "")
        self.frmMenuIzquierdo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmMenuIzquierdo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmMenuIzquierdo.setObjectName("frmMenuIzquierdo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frmMenuIzquierdo)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frmArribaMenu = QtWidgets.QFrame(self.frmMenuIzquierdo)
        self.frmArribaMenu.setMinimumSize(QtCore.QSize(180, 50))
        self.frmArribaMenu.setMaximumSize(QtCore.QSize(50, 50))
        self.frmArribaMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmArribaMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmArribaMenu.setObjectName("frmArribaMenu")
        self.btnMenu = QtWidgets.QPushButton(self.frmArribaMenu)
        self.btnMenu.setGeometry(QtCore.QRect(0, 0, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.btnMenu.setFont(font)
        self.btnMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMenu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnMenu.setStyleSheet("QPushButton{\n"
                                   "    border: none;\n"
                                   "    border-radius: 5px;    \n"
                                   "    background-color: transparent;\n"
                                   "    color: #fff;\n"
                                   "    padding: 10px;\n"
                                   "    text-align: left;\n"
                                   "}\n"
                                   "")
        self.btnMenu.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Iconos/menu.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMenu.setIcon(icon1)
        self.btnMenu.setIconSize(QtCore.QSize(30, 30))
        self.btnMenu.setObjectName("btnMenu")
        self.verticalLayout_2.addWidget(self.frmArribaMenu)
        self.frmCentroMenu = QtWidgets.QFrame(self.frmMenuIzquierdo)
        self.frmCentroMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmCentroMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmCentroMenu.setObjectName("frmCentroMenu")
        self.btnPrincipal = QtWidgets.QPushButton(self.frmCentroMenu)
        self.btnPrincipal.setGeometry(QtCore.QRect(0, 30, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.btnPrincipal.setFont(font)
        self.btnPrincipal.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPrincipal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnPrincipal.setStyleSheet("QPushButton{\n"
                                        "    border: none;\n"
                                        "    border-radius: 5px;    \n"
                                        "    background-color: transparent;\n"
                                        "    color: #fff;\n"
                                        "    padding: 10px;\n"
                                        "    text-align: left;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: #003356;\n"
                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Iconos/apartamento.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrincipal.setIcon(icon2)
        self.btnPrincipal.setIconSize(QtCore.QSize(30, 30))
        self.btnPrincipal.setObjectName("btnPrincipal")
        self.btnClientes = QtWidgets.QPushButton(self.frmCentroMenu)
        self.btnClientes.setGeometry(QtCore.QRect(0, 90, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.btnClientes.setFont(font)
        self.btnClientes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnClientes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnClientes.setStyleSheet("QPushButton{\n"
                                       "    border: none;\n"
                                       "    border-radius: 5px;    \n"
                                       "    background-color: transparent;\n"
                                       "    color: #fff;\n"
                                       "    padding: 10px;\n"
                                       "    text-align: left;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    background-color: #003356;\n"
                                       "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Iconos/usuario.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClientes.setIcon(icon3)
        self.btnClientes.setIconSize(QtCore.QSize(30, 30))
        self.btnClientes.setObjectName("btnClientes")
        self.btnReservas = QtWidgets.QPushButton(self.frmCentroMenu)
        self.btnReservas.setGeometry(QtCore.QRect(0, 150, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.btnReservas.setFont(font)
        self.btnReservas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnReservas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnReservas.setStyleSheet("QPushButton{\n"
                                       "    border: none;\n"
                                       "    border-radius: 5px;    \n"
                                       "    background-color: transparent;\n"
                                       "    color: #fff;\n"
                                       "    padding: 10px;\n"
                                       "    text-align: left;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    background-color: #003356;\n"
                                       "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Iconos/reserva.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReservas.setIcon(icon4)
        self.btnReservas.setIconSize(QtCore.QSize(30, 30))
        self.btnReservas.setObjectName("btnReservas")
        self.verticalLayout_2.addWidget(self.frmCentroMenu)
        self.frmAbajoMenu = QtWidgets.QFrame(self.frmMenuIzquierdo)
        self.frmAbajoMenu.setMinimumSize(QtCore.QSize(180, 50))
        self.frmAbajoMenu.setMaximumSize(QtCore.QSize(50, 50))
        self.frmAbajoMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmAbajoMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmAbajoMenu.setObjectName("frmAbajoMenu")
        self.btnCerrarSesion = QtWidgets.QPushButton(self.frmAbajoMenu)
        self.btnCerrarSesion.setGeometry(QtCore.QRect(0, 0, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.btnCerrarSesion.setFont(font)
        self.btnCerrarSesion.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrarSesion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCerrarSesion.setStyleSheet("QPushButton{\n"
                                           "    border: none;\n"
                                           "    border-radius: 5px;    \n"
                                           "    background-color: transparent;\n"
                                           "    color: #fff;\n"
                                           "    padding: 10px;\n"
                                           "    text-align: left;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "    background-color: #003356;\n"
                                           "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Iconos/cerrar_sesion.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrarSesion.setIcon(icon5)
        self.btnCerrarSesion.setIconSize(QtCore.QSize(30, 30))
        self.btnCerrarSesion.setObjectName("btnCerrarSesion")
        self.verticalLayout_2.addWidget(self.frmAbajoMenu)
        self.horizontalLayout_2.addWidget(self.frmMenuIzquierdo)
        self.frmMenuPrincipal = QtWidgets.QFrame(self.frameDos)
        self.frmMenuPrincipal.setStyleSheet("")
        self.frmMenuPrincipal.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frmMenuPrincipal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmMenuPrincipal.setObjectName("frmMenuPrincipal")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frmMenuPrincipal)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.paginasPrincipales = QtWidgets.QStackedWidget(
            self.frmMenuPrincipal)
        self.paginasPrincipales.setStyleSheet("")
        self.paginasPrincipales.setObjectName("paginasPrincipales")
        self.principal = QtWidgets.QWidget()
        self.principal.setStyleSheet("")
        self.principal.setObjectName("principal")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.principal)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frameCuatro = QtWidgets.QFrame(self.principal)
        self.frameCuatro.setStyleSheet("QWidget{\n"
                                       "    background: #fff;\n"
                                       "}")
        self.frameCuatro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameCuatro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCuatro.setObjectName("frameCuatro")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameCuatro)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.imgPrincipal = QtWidgets.QLabel(self.frameCuatro)
        self.imgPrincipal.setText("")
        self.imgPrincipal.setPixmap(QtGui.QPixmap("Imagenes/principal.png"))
        self.imgPrincipal.setScaledContents(False)
        self.imgPrincipal.setAlignment(QtCore.Qt.AlignCenter)
        self.imgPrincipal.setObjectName("imgPrincipal")
        self.verticalLayout_5.addWidget(self.imgPrincipal)
        self.verticalLayout_4.addWidget(self.frameCuatro)
        self.frameTres = QtWidgets.QFrame(self.principal)
        self.frameTres.setMinimumSize(QtCore.QSize(0, 20))
        self.frameTres.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frameTres.setStyleSheet("QWidget{\n"
                                     "    background: #fff;\n"
                                     "}")
        self.frameTres.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameTres.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTres.setObjectName("frameTres")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameTres)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lblVersion = QtWidgets.QLabel(self.frameTres)
        self.lblVersion.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lblVersion.setObjectName("lblVersion")
        self.verticalLayout_6.addWidget(self.lblVersion)
        self.verticalLayout_4.addWidget(self.frameTres)
        self.paginasPrincipales.addWidget(self.principal)
        self.clientes = QtWidgets.QWidget()
        self.clientes.setObjectName("clientes")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.clientes)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frameArriba = QtWidgets.QFrame(self.clientes)
        self.frameArriba.setMinimumSize(QtCore.QSize(0, 150))
        self.frameArriba.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frameArriba.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameArriba.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameArriba.setObjectName("frameArriba")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frameArriba)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frameCinco = QtWidgets.QFrame(self.frameArriba)
        self.frameCinco.setMinimumSize(QtCore.QSize(0, 80))
        self.frameCinco.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frameCinco.setStyleSheet("QFrame{\n"
                                      "    background-color: #fff;\n"
                                      "}")
        self.frameCinco.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameCinco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCinco.setObjectName("frameCinco")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frameCinco)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.imgTituloClientes = QtWidgets.QLabel(self.frameCinco)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.imgTituloClientes.setFont(font)
        self.imgTituloClientes.setText("")
        self.imgTituloClientes.setPixmap(
            QtGui.QPixmap("Imagenes/cliente.png"))
        self.imgTituloClientes.setScaledContents(False)
        self.imgTituloClientes.setAlignment(QtCore.Qt.AlignCenter)
        self.imgTituloClientes.setObjectName("imgTituloClientes")
        self.verticalLayout_9.addWidget(self.imgTituloClientes)
        self.verticalLayout_8.addWidget(self.frameCinco)
        self.frameSeis = QtWidgets.QFrame(self.frameArriba)
        self.frameSeis.setStyleSheet("QFrame{\n"
                                     "    background-color: #fff;\n"
                                     "}")
        self.frameSeis.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameSeis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSeis.setObjectName("frameSeis")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frameSeis)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.layoutUno = QtWidgets.QHBoxLayout()
        self.layoutUno.setSpacing(0)
        self.layoutUno.setObjectName("layoutUno")
        self.layoutUnoUno = QtWidgets.QHBoxLayout()
        self.layoutUnoUno.setContentsMargins(10, -1, 10, -1)
        self.layoutUnoUno.setSpacing(0)
        self.layoutUnoUno.setObjectName("layoutUnoUno")
        self.txtBuscarCliente = QtWidgets.QLineEdit(self.frameSeis)
        self.txtBuscarCliente.setMinimumSize(QtCore.QSize(0, 40))
        self.txtBuscarCliente.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtBuscarCliente.setFont(font)
        self.txtBuscarCliente.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtBuscarCliente.setStyleSheet("QLineEdit{\n"
                                            "    background-color: #d7d7d7;\n"
                                            "    border: none;\n"
                                            "    border-top-left-radius: 5px;\n"
                                            "    border-bottom-left-radius: 5px;\n"
                                            "    padding: 10px;\n"
                                            "}\n"
                                            "QLineEdit:focus {\n"
                                            "    border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.txtBuscarCliente.setMaxLength(12)
        self.txtBuscarCliente.setClearButtonEnabled(True)
        self.txtBuscarCliente.setObjectName("txtBuscarCliente")
        self.layoutUnoUno.addWidget(self.txtBuscarCliente)
        self.btnBuscarCliente = QtWidgets.QPushButton(self.frameSeis)
        self.btnBuscarCliente.setMinimumSize(QtCore.QSize(55, 40))
        self.btnBuscarCliente.setMaximumSize(QtCore.QSize(55, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnBuscarCliente.setFont(font)
        self.btnBuscarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBuscarCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnBuscarCliente.setStyleSheet("QPushButton{\n"
                                            "    background-color: #004A7C;\n"
                                            "    border:none;\n"
                                            "    border-top-right-radius: 5px;\n"
                                            "    border-bottom-right-radius: 5px;\n"
                                            "    padding-left: 15px;\n"
                                            "    padding-right: 15px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    background-color: #003356;\n"
                                            "}")
        self.btnBuscarCliente.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Iconos/buscar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarCliente.setIcon(icon6)
        self.btnBuscarCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnBuscarCliente.setObjectName("btnBuscarCliente")
        self.layoutUnoUno.addWidget(self.btnBuscarCliente)
        self.layoutUno.addLayout(self.layoutUnoUno)
        self.layoutUnoDos = QtWidgets.QHBoxLayout()
        self.layoutUnoDos.setContentsMargins(10, -1, 10, -1)
        self.layoutUnoDos.setSpacing(10)
        self.layoutUnoDos.setObjectName("layoutUnoDos")
        self.btnRegistrarCliente = QtWidgets.QPushButton(self.frameSeis)
        self.btnRegistrarCliente.setMinimumSize(QtCore.QSize(120, 40))
        self.btnRegistrarCliente.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnRegistrarCliente.setFont(font)
        self.btnRegistrarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegistrarCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnRegistrarCliente.setStyleSheet("QPushButton{\n"
                                               "    background-color: #009929;\n"
                                               "    border:none;\n"
                                               "    border-radius: 5px;\n"
                                               "    color:#fff;\n"
                                               "    padding-left: 15px;\n"
                                               "    padding-right: 15px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #005d16;\n"
                                               "}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Iconos/agregar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegistrarCliente.setIcon(icon7)
        self.btnRegistrarCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnRegistrarCliente.setObjectName("btnRegistrarCliente")
        self.layoutUnoDos.addWidget(self.btnRegistrarCliente)
        self.btnModificarCliente = QtWidgets.QPushButton(self.frameSeis)
        self.btnModificarCliente.setMinimumSize(QtCore.QSize(120, 40))
        self.btnModificarCliente.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnModificarCliente.setFont(font)
        self.btnModificarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnModificarCliente.setStyleSheet("QPushButton{\n"
                                               "    background-color: #2196f3;\n"
                                               "    border:none;\n"
                                               "    border-radius: 5px;\n"
                                               "    color:#fff;\n"
                                               "    padding-left: 15px;\n"
                                               "    padding-right: 15px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #155db1;\n"
                                               "}\n"
                                               "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Iconos/modificar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificarCliente.setIcon(icon8)
        self.btnModificarCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnModificarCliente.setObjectName("btnModificarCliente")
        self.layoutUnoDos.addWidget(self.btnModificarCliente)
        self.btnEliminarCliente = QtWidgets.QPushButton(self.frameSeis)
        self.btnEliminarCliente.setMinimumSize(QtCore.QSize(120, 40))
        self.btnEliminarCliente.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnEliminarCliente.setFont(font)
        self.btnEliminarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEliminarCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnEliminarCliente.setStyleSheet("QPushButton{\n"
                                              "    background-color: #ff0000;\n"
                                              "    border:none;\n"
                                              "    border-radius: 5px;\n"
                                              "    color:#fff;\n"
                                              "    padding-left: 15px;\n"
                                              "    padding-right: 15px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "    background-color: #b10005;\n"
                                              "}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Iconos/eliminar.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminarCliente.setIcon(icon9)
        self.btnEliminarCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnEliminarCliente.setObjectName("btnEliminarCliente")
        self.layoutUnoDos.addWidget(self.btnEliminarCliente)
        self.layoutUno.addLayout(self.layoutUnoDos)
        self.verticalLayout_10.addLayout(self.layoutUno)
        self.verticalLayout_8.addWidget(self.frameSeis)
        self.verticalLayout_7.addWidget(self.frameArriba)
        self.frameAbajo = QtWidgets.QFrame(self.clientes)
        self.frameAbajo.setMinimumSize(QtCore.QSize(0, 0))
        self.frameAbajo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameAbajo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAbajo.setObjectName("frameAbajo")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frameAbajo)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridUno = QtWidgets.QGridLayout()
        self.gridUno.setSpacing(0)
        self.gridUno.setObjectName("gridUno")
        self.frameSiete = QtWidgets.QFrame(self.frameAbajo)
        self.frameSiete.setMinimumSize(QtCore.QSize(0, 30))
        self.frameSiete.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frameSiete.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameSiete.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSiete.setObjectName("frameSiete")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frameSiete)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.lblTotalClientes = QtWidgets.QLabel(self.frameSiete)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lblTotalClientes.setFont(font)
        self.lblTotalClientes.setStyleSheet("QLabel{\n"
                                            "padding: 10px;\n"
                                            "}")
        self.lblTotalClientes.setText("")
        self.lblTotalClientes.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblTotalClientes.setObjectName("lblTotalClientes")
        self.verticalLayout_16.addWidget(self.lblTotalClientes)
        self.gridUno.addWidget(self.frameSiete, 2, 0, 1, 1)
        self.frameOcho = QtWidgets.QFrame(self.frameAbajo)
        self.frameOcho.setStyleSheet("")
        self.frameOcho.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameOcho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOcho.setObjectName("frameOcho")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frameOcho)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.tblClientes = QtWidgets.QTableWidget(self.frameOcho)
        self.tblClientes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tblClientes.setStyleSheet("QTableWidget::item{\n"
                                       "    border-color: rgb(44, 49, 60);\n"
                                       "    gridline-color: rgb(44, 49, 60);\n"
                                       "    padding: 10px\n"
                                       "}\n"
                                       "QTableWidget::item:selected{\n"
                                       "    background-color: #cdcdcd;\n"
                                       "}\n"
                                       "QHeaderView::section{\n"
                                       "    background-color: #fff;\n"
                                       "    border-style: none;\n"
                                       "    border-bottom: 1px solid #000;\n"
                                       "    padding: 5px\n"
                                       "}\n"
                                       "")
        self.tblClientes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblClientes.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblClientes.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblClientes.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblClientes.setRowCount(0)
        self.tblClientes.setColumnCount(9)
        self.tblClientes.setObjectName("tblClientes")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblClientes.setHorizontalHeaderItem(8, item)
        self.tblClientes.horizontalHeader().setCascadingSectionResizes(True)
        self.tblClientes.horizontalHeader().setDefaultSectionSize(200)
        self.tblClientes.horizontalHeader().setMinimumSectionSize(40)
        self.tblClientes.horizontalHeader().setStretchLastSection(True)
        self.tblClientes.verticalHeader().setVisible(False)
        self.tblClientes.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout_15.addWidget(self.tblClientes)
        self.gridUno.addWidget(self.frameOcho, 1, 0, 1, 1)
        self.frameNueve = QtWidgets.QFrame(self.frameAbajo)
        self.frameNueve.setMinimumSize(QtCore.QSize(0, 0))
        self.frameNueve.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frameNueve.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameNueve.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameNueve.setObjectName("frameNueve")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frameNueve)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.paginasCliente = QtWidgets.QStackedWidget(self.frameNueve)
        self.paginasCliente.setObjectName("paginasCliente")
        self.clientesRegistrar = QtWidgets.QWidget()
        self.clientesRegistrar.setObjectName("clientesRegistrar")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.clientesRegistrar)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame = QtWidgets.QFrame(self.clientesRegistrar)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.framesRegistroCliente_2 = QtWidgets.QFrame(self.frame)
        self.framesRegistroCliente_2.setMinimumSize(QtCore.QSize(0, 50))
        self.framesRegistroCliente_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.framesRegistroCliente_2.setStyleSheet(
            "    background-color: #009929;")
        self.framesRegistroCliente_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framesRegistroCliente_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framesRegistroCliente_2.setObjectName("framesRegistroCliente_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(
            self.framesRegistroCliente_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblUno = QtWidgets.QLabel(self.framesRegistroCliente_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.lblUno.setFont(font)
        self.lblUno.setStyleSheet("QLabel{\n"
                                  "    background-color: transparent;\n"
                                  "    color: #fff;\n"
                                  "    padding: 10px;\n"
                                  "}")
        self.lblUno.setObjectName("lblUno")
        self.horizontalLayout_8.addWidget(self.lblUno)
        self.btnCerrarRegistroCliente = QtWidgets.QPushButton(
            self.framesRegistroCliente_2)
        self.btnCerrarRegistroCliente.setMinimumSize(QtCore.QSize(50, 0))
        self.btnCerrarRegistroCliente.setMaximumSize(
            QtCore.QSize(50, 16777215))
        self.btnCerrarRegistroCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrarRegistroCliente.setStyleSheet("QPushButton{\n"
                                                    "    border: none;\n"
                                                    "    background-color: transparent;\n"
                                                    "    padding: 10px;\n"
                                                    "}\n"
                                                    "")
        self.btnCerrarRegistroCliente.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Iconos/cerrar.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCerrarRegistroCliente.setIcon(icon10)
        self.btnCerrarRegistroCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnCerrarRegistroCliente.setObjectName("btnCerrarRegistroCliente")
        self.horizontalLayout_8.addWidget(self.btnCerrarRegistroCliente)
        self.verticalLayout_24.addWidget(self.framesRegistroCliente_2)
        self.framesRegistroCliente = QtWidgets.QFrame(self.frame)
        self.framesRegistroCliente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framesRegistroCliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framesRegistroCliente.setObjectName("framesRegistroCliente")
        self.txtApellidoRegistroCliente = QtWidgets.QLineEdit(
            self.framesRegistroCliente)
        self.txtApellidoRegistroCliente.setGeometry(
            QtCore.QRect(40, 20, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtApellidoRegistroCliente.setFont(font)
        self.txtApellidoRegistroCliente.setStyleSheet("QLineEdit{\n"
                                                      "    background-color: #d7d7d7;\n"
                                                      "    border: none;\n"
                                                      "    border-radius: 5px;\n"
                                                      "    padding: 10px;\n"
                                                      "}\n"
                                                      "QLineEdit:focus {\n"
                                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                                      "}")
        self.txtApellidoRegistroCliente.setMaxLength(120)
        self.txtApellidoRegistroCliente.setClearButtonEnabled(True)
        self.txtApellidoRegistroCliente.setObjectName(
            "txtApellidoRegistroCliente")
        self.cmbTipoDocumentoRegistroCliente = QtWidgets.QComboBox(
            self.framesRegistroCliente)
        self.cmbTipoDocumentoRegistroCliente.setGeometry(
            QtCore.QRect(40, 140, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.cmbTipoDocumentoRegistroCliente.setFont(font)
        self.cmbTipoDocumentoRegistroCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmbTipoDocumentoRegistroCliente.setStyleSheet("QComboBox{\n"
                                                           "    background-color: #d7d7d7;\n"
                                                           "    border-radius: 5px;\n"
                                                           "    padding-left: 10px;\n"
                                                           "}\n"
                                                           "QComboBox:hover  {\n"
                                                           "    border: 2px solid rgb(91, 101, 124);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QComboBox, QAbstractItemView {\n"
                                                           "    color: #000;    \n"
                                                           "    background-color: #d7d7d7;\n"
                                                           "    selection-background-color: #cdcdcd;\n"
                                                           "    selection-color: #000;\n"
                                                           "}\n"
                                                           "QComboBox::drop-down {\n"
                                                           "    width: 30px;\n"
                                                           "    padding: 5px;\n"
                                                           "    image: url(:Iconos/seleccionar.png);\n"
                                                           "}")
        self.cmbTipoDocumentoRegistroCliente.setObjectName(
            "cmbTipoDocumentoRegistroCliente")
        self.cmbTipoDocumentoRegistroCliente.addItem("")
        self.cmbProvinciaRegistroCliente = QtWidgets.QComboBox(
            self.framesRegistroCliente)
        self.cmbProvinciaRegistroCliente.setGeometry(
            QtCore.QRect(40, 200, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.cmbProvinciaRegistroCliente.setFont(font)
        self.cmbProvinciaRegistroCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmbProvinciaRegistroCliente.setStyleSheet("QComboBox{\n"
                                                       "    background-color: #d7d7d7;\n"
                                                       "    border-radius: 5px;\n"
                                                       "    padding-left: 10px;\n"
                                                       "}\n"
                                                       "QComboBox:hover  {\n"
                                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                                       "}\n"
                                                       "\n"
                                                       "QComboBox, QAbstractItemView {\n"
                                                       "    color: #000;    \n"
                                                       "    background-color: #d7d7d7;\n"
                                                       "    selection-background-color: #cdcdcd;\n"
                                                       "    selection-color: #000;\n"
                                                       "}\n"
                                                       "QComboBox::drop-down {\n"
                                                       "    width: 30px;\n"
                                                       "    padding: 5px;\n"
                                                       "    image: url(:Iconos/seleccionar.png);\n"
                                                       "}")
        self.cmbProvinciaRegistroCliente.setPlaceholderText("")
        self.cmbProvinciaRegistroCliente.setObjectName(
            "cmbProvinciaRegistroCliente")
        self.cmbProvinciaRegistroCliente.addItem("")
        self.txtNombreRegistroCliente = QtWidgets.QLineEdit(
            self.framesRegistroCliente)
        self.txtNombreRegistroCliente.setGeometry(
            QtCore.QRect(40, 80, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtNombreRegistroCliente.setFont(font)
        self.txtNombreRegistroCliente.setStyleSheet("QLineEdit{\n"
                                                    "    background-color: #d7d7d7;\n"
                                                    "    border: none;\n"
                                                    "    border-radius: 5px;\n"
                                                    "    padding: 10px;\n"
                                                    "}\n"
                                                    "QLineEdit:focus {\n"
                                                    "    border: 2px solid rgb(91, 101, 124);\n"
                                                    "}")
        self.txtNombreRegistroCliente.setMaxLength(120)
        self.txtNombreRegistroCliente.setClearButtonEnabled(True)
        self.txtNombreRegistroCliente.setObjectName("txtNombreRegistroCliente")
        self.txtDocumentoRegistroCliente = QtWidgets.QLineEdit(
            self.framesRegistroCliente)
        self.txtDocumentoRegistroCliente.setGeometry(
            QtCore.QRect(250, 140, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtDocumentoRegistroCliente.setFont(font)
        self.txtDocumentoRegistroCliente.setStyleSheet("QLineEdit{\n"
                                                       "    background-color: #d7d7d7;\n"
                                                       "    border: none;\n"
                                                       "    border-radius: 5px;\n"
                                                       "    padding: 10px;\n"
                                                       "}\n"
                                                       "QLineEdit:focus {\n"
                                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                                       "}")
        self.txtDocumentoRegistroCliente.setMaxLength(12)
        self.txtDocumentoRegistroCliente.setClearButtonEnabled(True)
        self.txtDocumentoRegistroCliente.setObjectName(
            "txtDocumentoRegistroCliente")
        self.txtCiudadRegistroCliente = QtWidgets.QLineEdit(
            self.framesRegistroCliente)
        self.txtCiudadRegistroCliente.setGeometry(
            QtCore.QRect(250, 200, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCiudadRegistroCliente.setFont(font)
        self.txtCiudadRegistroCliente.setStyleSheet("QLineEdit{\n"
                                                    "    background-color: #d7d7d7;\n"
                                                    "    border: none;\n"
                                                    "    border-radius: 5px;\n"
                                                    "    padding: 10px;\n"
                                                    "}\n"
                                                    "QLineEdit:focus {\n"
                                                    "    border: 2px solid rgb(91, 101, 124);\n"
                                                    "}")
        self.txtCiudadRegistroCliente.setMaxLength(150)
        self.txtCiudadRegistroCliente.setClearButtonEnabled(True)
        self.txtCiudadRegistroCliente.setObjectName("txtCiudadRegistroCliente")
        self.txtCorreoRegistroCliente = QtWidgets.QLineEdit(
            self.framesRegistroCliente)
        self.txtCorreoRegistroCliente.setGeometry(
            QtCore.QRect(40, 260, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCorreoRegistroCliente.setFont(font)
        self.txtCorreoRegistroCliente.setStyleSheet("QLineEdit{\n"
                                                    "    background-color: #d7d7d7;\n"
                                                    "    border: none;\n"
                                                    "    border-radius: 5px;\n"
                                                    "    padding: 10px;\n"
                                                    "}\n"
                                                    "QLineEdit:focus {\n"
                                                    "    border: 2px solid rgb(91, 101, 124);\n"
                                                    "}")
        self.txtCorreoRegistroCliente.setMaxLength(200)
        self.txtCorreoRegistroCliente.setClearButtonEnabled(True)
        self.txtCorreoRegistroCliente.setObjectName("txtCorreoRegistroCliente")
        self.txtCelularRegistroCliente = QtWidgets.QLineEdit(
            self.framesRegistroCliente)
        self.txtCelularRegistroCliente.setGeometry(
            QtCore.QRect(40, 320, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCelularRegistroCliente.setFont(font)
        self.txtCelularRegistroCliente.setStyleSheet("QLineEdit{\n"
                                                     "    background-color: #d7d7d7;\n"
                                                     "    border: none;\n"
                                                     "    border-radius: 5px;\n"
                                                     "    padding: 10px;\n"
                                                     "}\n"
                                                     "QLineEdit:focus {\n"
                                                     "    border: 2px solid rgb(91, 101, 124);\n"
                                                     "}")
        self.txtCelularRegistroCliente.setMaxLength(30)
        self.txtCelularRegistroCliente.setClearButtonEnabled(True)
        self.txtCelularRegistroCliente.setObjectName(
            "txtCelularRegistroCliente")
        self.btnConfirmarRegistroCliente = QtWidgets.QPushButton(
            self.framesRegistroCliente)
        self.btnConfirmarRegistroCliente.setGeometry(
            QtCore.QRect(210, 390, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnConfirmarRegistroCliente.setFont(font)
        self.btnConfirmarRegistroCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConfirmarRegistroCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnConfirmarRegistroCliente.setStyleSheet("QPushButton{\n"
                                                       "    background-color: #1c1c1c;\n"
                                                       "    border:none;\n"
                                                       "    border-radius: 5px;\n"
                                                       "    color:#fff;\n"
                                                       "    padding-left: 15px;\n"
                                                       "    padding-right: 15px;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    background-color: #000000;\n"
                                                       "}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Iconos/confirmar.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConfirmarRegistroCliente.setIcon(icon11)
        self.btnConfirmarRegistroCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnConfirmarRegistroCliente.setObjectName(
            "btnConfirmarRegistroCliente")
        self.btnCancelarRegistroCliente = QtWidgets.QPushButton(
            self.framesRegistroCliente)
        self.btnCancelarRegistroCliente.setGeometry(
            QtCore.QRect(340, 390, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnCancelarRegistroCliente.setFont(font)
        self.btnCancelarRegistroCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelarRegistroCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCancelarRegistroCliente.setStyleSheet("QPushButton{\n"
                                                      "    background-color: #7f7f7f;\n"
                                                      "    border:none;\n"
                                                      "    border-radius: 5px;\n"
                                                      "    color:#fff;\n"
                                                      "    padding-left: 15px;\n"
                                                      "    padding-right: 15px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    background-color: #595959\n"
                                                      "}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Iconos/cancelar.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelarRegistroCliente.setIcon(icon12)
        self.btnCancelarRegistroCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnCancelarRegistroCliente.setObjectName(
            "btnCancelarRegistroCliente")
        self.verticalLayout_24.addWidget(self.framesRegistroCliente)
        self.verticalLayout_23.addWidget(self.frame)
        self.paginasCliente.addWidget(self.clientesRegistrar)
        self.clientesModificar = QtWidgets.QWidget()
        self.clientesModificar.setObjectName("clientesModificar")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.clientesModificar)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.frame_2 = QtWidgets.QFrame(self.clientesModificar)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.framesModificarCliente_2 = QtWidgets.QFrame(self.frame_2)
        self.framesModificarCliente_2.setMinimumSize(QtCore.QSize(0, 50))
        self.framesModificarCliente_2.setMaximumSize(
            QtCore.QSize(16777215, 50))
        self.framesModificarCliente_2.setStyleSheet(
            "background-color: #2196f3;")
        self.framesModificarCliente_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framesModificarCliente_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framesModificarCliente_2.setObjectName("framesModificarCliente_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(
            self.framesModificarCliente_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblDos = QtWidgets.QLabel(self.framesModificarCliente_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.lblDos.setFont(font)
        self.lblDos.setStyleSheet("QLabel{\n"
                                  "    background-color: transparent;\n"
                                  "    color: #fff;\n"
                                  "    padding: 10px;\n"
                                  "}")
        self.lblDos.setObjectName("lblDos")
        self.horizontalLayout_9.addWidget(self.lblDos)
        self.btnCerrarModificarCliente = QtWidgets.QPushButton(
            self.framesModificarCliente_2)
        self.btnCerrarModificarCliente.setMinimumSize(QtCore.QSize(50, 0))
        self.btnCerrarModificarCliente.setMaximumSize(
            QtCore.QSize(50, 16777215))
        self.btnCerrarModificarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrarModificarCliente.setStyleSheet("QPushButton{\n"
                                                     "    border: none;\n"
                                                     "    background-color: transparent;\n"
                                                     "    padding: 10px;\n"
                                                     "}\n"
                                                     "")
        self.btnCerrarModificarCliente.setText("")
        self.btnCerrarModificarCliente.setIcon(icon10)
        self.btnCerrarModificarCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnCerrarModificarCliente.setObjectName(
            "btnCerrarModificarCliente")
        self.horizontalLayout_9.addWidget(self.btnCerrarModificarCliente)
        self.verticalLayout_25.addWidget(self.framesModificarCliente_2)
        self.framesModificarCliente = QtWidgets.QFrame(self.frame_2)
        self.framesModificarCliente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framesModificarCliente.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framesModificarCliente.setObjectName("framesModificarCliente")
        self.txtApellidoModificarCliente = QtWidgets.QLineEdit(
            self.framesModificarCliente)
        self.txtApellidoModificarCliente.setGeometry(
            QtCore.QRect(40, 20, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtApellidoModificarCliente.setFont(font)
        self.txtApellidoModificarCliente.setStyleSheet("QLineEdit{\n"
                                                       "    background-color: #d7d7d7;\n"
                                                       "    border: none;\n"
                                                       "    border-radius: 5px;\n"
                                                       "    padding: 10px;\n"
                                                       "}\n"
                                                       "QLineEdit:focus {\n"
                                                       "    border: 2px solid rgb(91, 101, 124);\n"
                                                       "}")
        self.txtApellidoModificarCliente.setMaxLength(120)
        self.txtApellidoModificarCliente.setClearButtonEnabled(True)
        self.txtApellidoModificarCliente.setObjectName(
            "txtApellidoModificarCliente")
        self.cmbTipoDocumentoModificarCliente = QtWidgets.QComboBox(
            self.framesModificarCliente)
        self.cmbTipoDocumentoModificarCliente.setGeometry(
            QtCore.QRect(40, 140, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.cmbTipoDocumentoModificarCliente.setFont(font)
        self.cmbTipoDocumentoModificarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmbTipoDocumentoModificarCliente.setStyleSheet("QComboBox{\n"
                                                            "    background-color: #d7d7d7;\n"
                                                            "    border-radius: 5px;\n"
                                                            "    padding-left: 10px;\n"
                                                            "}\n"
                                                            "QComboBox:hover  {\n"
                                                            "    border: 2px solid rgb(91, 101, 124);\n"
                                                            "}\n"
                                                            "\n"
                                                            "QComboBox, QAbstractItemView {\n"
                                                            "    color: #000;    \n"
                                                            "    background-color: #d7d7d7;\n"
                                                            "    selection-background-color: #cdcdcd;\n"
                                                            "    selection-color: #000;\n"
                                                            "}\n"
                                                            "QComboBox::drop-down {\n"
                                                            "    width: 30px;\n"
                                                            "    padding: 5px;\n"
                                                            "    image: url(:Iconos/seleccionar.png);\n"
                                                            "}")
        self.cmbTipoDocumentoModificarCliente.setObjectName(
            "cmbTipoDocumentoModificarCliente")
        self.cmbTipoDocumentoModificarCliente.addItem("")
        self.cmbProvinciaModificarCliente = QtWidgets.QComboBox(
            self.framesModificarCliente)
        self.cmbProvinciaModificarCliente.setGeometry(
            QtCore.QRect(40, 200, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.cmbProvinciaModificarCliente.setFont(font)
        self.cmbProvinciaModificarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmbProvinciaModificarCliente.setStyleSheet("QComboBox{\n"
                                                        "    background-color: #d7d7d7;\n"
                                                        "    border-radius: 5px;\n"
                                                        "    padding-left: 10px;\n"
                                                        "}\n"
                                                        "QComboBox:hover  {\n"
                                                        "    border: 2px solid rgb(91, 101, 124);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QComboBox, QAbstractItemView {\n"
                                                        "    color: #000;    \n"
                                                        "    background-color: #d7d7d7;\n"
                                                        "    selection-background-color: #cdcdcd;\n"
                                                        "    selection-color: #000;\n"
                                                        "}\n"
                                                        "QComboBox::drop-down {\n"
                                                        "    width: 30px;\n"
                                                        "    padding: 5px;\n"
                                                        "    image: url(:Iconos/seleccionar.png);\n"
                                                        "}")
        self.cmbProvinciaModificarCliente.setPlaceholderText("")
        self.cmbProvinciaModificarCliente.setObjectName(
            "cmbProvinciaModificarCliente")
        self.cmbProvinciaModificarCliente.addItem("")
        self.txtNombreModificarCliente = QtWidgets.QLineEdit(
            self.framesModificarCliente)
        self.txtNombreModificarCliente.setGeometry(
            QtCore.QRect(40, 80, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtNombreModificarCliente.setFont(font)
        self.txtNombreModificarCliente.setStyleSheet("QLineEdit{\n"
                                                     "    background-color: #d7d7d7;\n"
                                                     "    border: none;\n"
                                                     "    border-radius: 5px;\n"
                                                     "    padding: 10px;\n"
                                                     "}\n"
                                                     "QLineEdit:focus {\n"
                                                     "    border: 2px solid rgb(91, 101, 124);\n"
                                                     "}")
        self.txtNombreModificarCliente.setMaxLength(120)
        self.txtNombreModificarCliente.setClearButtonEnabled(True)
        self.txtNombreModificarCliente.setObjectName(
            "txtNombreModificarCliente")
        self.txtDocumentoModificarCliente = QtWidgets.QLineEdit(
            self.framesModificarCliente)
        self.txtDocumentoModificarCliente.setGeometry(
            QtCore.QRect(250, 140, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtDocumentoModificarCliente.setFont(font)
        self.txtDocumentoModificarCliente.setStyleSheet("QLineEdit{\n"
                                                        "    background-color: #d7d7d7;\n"
                                                        "    border: none;\n"
                                                        "    border-radius: 5px;\n"
                                                        "    padding: 10px;\n"
                                                        "}\n"
                                                        "QLineEdit:focus {\n"
                                                        "    border: 2px solid rgb(91, 101, 124);\n"
                                                        "}")
        self.txtDocumentoModificarCliente.setMaxLength(12)
        self.txtDocumentoModificarCliente.setClearButtonEnabled(True)
        self.txtDocumentoModificarCliente.setObjectName(
            "txtDocumentoModificarCliente")
        self.txtCiudadModificarCliente = QtWidgets.QLineEdit(
            self.framesModificarCliente)
        self.txtCiudadModificarCliente.setGeometry(
            QtCore.QRect(250, 200, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCiudadModificarCliente.setFont(font)
        self.txtCiudadModificarCliente.setStyleSheet("QLineEdit{\n"
                                                     "    background-color: #d7d7d7;\n"
                                                     "    border: none;\n"
                                                     "    border-radius: 5px;\n"
                                                     "    padding: 10px;\n"
                                                     "}\n"
                                                     "QLineEdit:focus {\n"
                                                     "    border: 2px solid rgb(91, 101, 124);\n"
                                                     "}")
        self.txtCiudadModificarCliente.setMaxLength(120)
        self.txtCiudadModificarCliente.setClearButtonEnabled(True)
        self.txtCiudadModificarCliente.setObjectName(
            "txtCiudadModificarCliente")
        self.txtCorreoModificarCliente = QtWidgets.QLineEdit(
            self.framesModificarCliente)
        self.txtCorreoModificarCliente.setGeometry(
            QtCore.QRect(40, 260, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCorreoModificarCliente.setFont(font)
        self.txtCorreoModificarCliente.setStyleSheet("QLineEdit{\n"
                                                     "    background-color: #d7d7d7;\n"
                                                     "    border: none;\n"
                                                     "    border-radius: 5px;\n"
                                                     "    padding: 10px;\n"
                                                     "}\n"
                                                     "QLineEdit:focus {\n"
                                                     "    border: 2px solid rgb(91, 101, 124);\n"
                                                     "}")
        self.txtCorreoModificarCliente.setMaxLength(200)
        self.txtCorreoModificarCliente.setClearButtonEnabled(True)
        self.txtCorreoModificarCliente.setObjectName(
            "txtCorreoModificarCliente")
        self.txtCelularModificarCliente = QtWidgets.QLineEdit(
            self.framesModificarCliente)
        self.txtCelularModificarCliente.setGeometry(
            QtCore.QRect(40, 320, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCelularModificarCliente.setFont(font)
        self.txtCelularModificarCliente.setStyleSheet("QLineEdit{\n"
                                                      "    background-color: #d7d7d7;\n"
                                                      "    border: none;\n"
                                                      "    border-radius: 5px;\n"
                                                      "    padding: 10px;\n"
                                                      "}\n"
                                                      "QLineEdit:focus {\n"
                                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                                      "}")
        self.txtCelularModificarCliente.setMaxLength(30)
        self.txtCelularModificarCliente.setClearButtonEnabled(True)
        self.txtCelularModificarCliente.setObjectName(
            "txtCelularModificarCliente")
        self.btnConfirmarModificarCliente = QtWidgets.QPushButton(
            self.framesModificarCliente)
        self.btnConfirmarModificarCliente.setGeometry(
            QtCore.QRect(210, 390, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnConfirmarModificarCliente.setFont(font)
        self.btnConfirmarModificarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConfirmarModificarCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnConfirmarModificarCliente.setStyleSheet("QPushButton{\n"
                                                        "    background-color: #1c1c1c;\n"
                                                        "    border:none;\n"
                                                        "    border-radius: 5px;\n"
                                                        "    color:#fff;\n"
                                                        "    padding-left: 15px;\n"
                                                        "    padding-right: 15px;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    background-color: #000000;\n"
                                                        "}")
        self.btnConfirmarModificarCliente.setIcon(icon11)
        self.btnConfirmarModificarCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnConfirmarModificarCliente.setObjectName(
            "btnConfirmarModificarCliente")
        self.btnCancelarModificarCliente = QtWidgets.QPushButton(
            self.framesModificarCliente)
        self.btnCancelarModificarCliente.setGeometry(
            QtCore.QRect(340, 390, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnCancelarModificarCliente.setFont(font)
        self.btnCancelarModificarCliente.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelarModificarCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCancelarModificarCliente.setStyleSheet("QPushButton{\n"
                                                       "    background-color: #7f7f7f;\n"
                                                       "    border:none;\n"
                                                       "    border-radius: 5px;\n"
                                                       "    color:#fff;\n"
                                                       "    padding-left: 15px;\n"
                                                       "    padding-right: 15px;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    background-color: #595959\n"
                                                       "}")
        self.btnCancelarModificarCliente.setIcon(icon12)
        self.btnCancelarModificarCliente.setIconSize(QtCore.QSize(20, 20))
        self.btnCancelarModificarCliente.setObjectName(
            "btnCancelarModificarCliente")
        self.verticalLayout_25.addWidget(self.framesModificarCliente)
        self.verticalLayout_26.addWidget(self.frame_2)
        self.paginasCliente.addWidget(self.clientesModificar)
        self.verticalLayout_12.addWidget(self.paginasCliente)
        self.gridUno.addWidget(self.frameNueve, 1, 1, 1, 1)
        self.verticalLayout_11.addLayout(self.gridUno)
        self.verticalLayout_7.addWidget(self.frameAbajo)
        self.paginasPrincipales.addWidget(self.clientes)
        self.alquiler = QtWidgets.QWidget()
        self.alquiler.setObjectName("alquiler")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.alquiler)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frameArriba_2 = QtWidgets.QFrame(self.alquiler)
        self.frameArriba_2.setMinimumSize(QtCore.QSize(0, 150))
        self.frameArriba_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frameArriba_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameArriba_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameArriba_2.setObjectName("frameArriba_2")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frameArriba_2)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frameCinco_2 = QtWidgets.QFrame(self.frameArriba_2)
        self.frameCinco_2.setMinimumSize(QtCore.QSize(0, 80))
        self.frameCinco_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frameCinco_2.setStyleSheet("QFrame{\n"
                                        "    background-color: #fff;\n"
                                        "}")
        self.frameCinco_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameCinco_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCinco_2.setObjectName("frameCinco_2")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frameCinco_2)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.imgTituloAlquiler = QtWidgets.QLabel(self.frameCinco_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        self.imgTituloAlquiler.setFont(font)
        self.imgTituloAlquiler.setText("")
        self.imgTituloAlquiler.setPixmap(
            QtGui.QPixmap("Imagenes/alquiler.png"))
        self.imgTituloAlquiler.setScaledContents(False)
        self.imgTituloAlquiler.setAlignment(QtCore.Qt.AlignCenter)
        self.imgTituloAlquiler.setObjectName("imgTituloAlquiler")
        self.verticalLayout_20.addWidget(self.imgTituloAlquiler)
        self.verticalLayout_19.addWidget(self.frameCinco_2)
        self.frameSeis_2 = QtWidgets.QFrame(self.frameArriba_2)
        self.frameSeis_2.setStyleSheet("QFrame{\n"
                                       "    background-color: #fff;\n"
                                       "}")
        self.frameSeis_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameSeis_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSeis_2.setObjectName("frameSeis_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frameSeis_2)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.layoutUno_2 = QtWidgets.QHBoxLayout()
        self.layoutUno_2.setSpacing(0)
        self.layoutUno_2.setObjectName("layoutUno_2")
        self.layoutUnoUno_2 = QtWidgets.QHBoxLayout()
        self.layoutUnoUno_2.setContentsMargins(10, -1, 10, -1)
        self.layoutUnoUno_2.setSpacing(0)
        self.layoutUnoUno_2.setObjectName("layoutUnoUno_2")
        self.txtBuscarAlquiler = QtWidgets.QLineEdit(self.frameSeis_2)
        self.txtBuscarAlquiler.setMinimumSize(QtCore.QSize(0, 40))
        self.txtBuscarAlquiler.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtBuscarAlquiler.setFont(font)
        self.txtBuscarAlquiler.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.txtBuscarAlquiler.setStyleSheet("QLineEdit{\n"
                                             "    background-color: #d7d7d7;\n"
                                             "    border: none;\n"
                                             "    border-top-left-radius: 5px;\n"
                                             "    border-bottom-left-radius: 5px;\n"
                                             "    padding: 10px;\n"
                                             "}\n"
                                             "QLineEdit:focus {\n"
                                             "    border: 2px solid rgb(91, 101, 124);\n"
                                             "}")
        self.txtBuscarAlquiler.setMaxLength(100)
        self.txtBuscarAlquiler.setClearButtonEnabled(True)
        self.txtBuscarAlquiler.setObjectName("txtBuscarAlquiler")
        self.layoutUnoUno_2.addWidget(self.txtBuscarAlquiler)
        self.btnBuscarAlquiler = QtWidgets.QPushButton(self.frameSeis_2)
        self.btnBuscarAlquiler.setMinimumSize(QtCore.QSize(55, 40))
        self.btnBuscarAlquiler.setMaximumSize(QtCore.QSize(55, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnBuscarAlquiler.setFont(font)
        self.btnBuscarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBuscarAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnBuscarAlquiler.setStyleSheet("QPushButton{\n"
                                             "    background-color: #004A7C;\n"
                                             "    border:none;\n"
                                             "    border-top-right-radius: 5px;\n"
                                             "    border-bottom-right-radius: 5px;\n"
                                             "    padding-left: 15px;\n"
                                             "    padding-right: 15px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    background-color: #003356;\n"
                                             "}")
        self.btnBuscarAlquiler.setText("")
        self.btnBuscarAlquiler.setIcon(icon6)
        self.btnBuscarAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnBuscarAlquiler.setObjectName("btnBuscarAlquiler")
        self.layoutUnoUno_2.addWidget(self.btnBuscarAlquiler)
        self.layoutUno_2.addLayout(self.layoutUnoUno_2)
        self.layoutUnoDos_2 = QtWidgets.QHBoxLayout()
        self.layoutUnoDos_2.setContentsMargins(10, -1, 10, -1)
        self.layoutUnoDos_2.setSpacing(10)
        self.layoutUnoDos_2.setObjectName("layoutUnoDos_2")
        self.btnRegistrarAlquiler = QtWidgets.QPushButton(self.frameSeis_2)
        self.btnRegistrarAlquiler.setMinimumSize(QtCore.QSize(120, 40))
        self.btnRegistrarAlquiler.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnRegistrarAlquiler.setFont(font)
        self.btnRegistrarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRegistrarAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnRegistrarAlquiler.setStyleSheet("QPushButton{\n"
                                                "    background-color: #009929;\n"
                                                "    border:none;\n"
                                                "    border-radius: 5px;\n"
                                                "    color:#fff;\n"
                                                "    padding-left: 15px;\n"
                                                "    padding-right: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color: #005d16;\n"
                                                "}")
        self.btnRegistrarAlquiler.setIcon(icon7)
        self.btnRegistrarAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnRegistrarAlquiler.setObjectName("btnRegistrarAlquiler")
        self.layoutUnoDos_2.addWidget(self.btnRegistrarAlquiler)
        self.btnModificarAlquiler = QtWidgets.QPushButton(self.frameSeis_2)
        self.btnModificarAlquiler.setMinimumSize(QtCore.QSize(120, 40))
        self.btnModificarAlquiler.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnModificarAlquiler.setFont(font)
        self.btnModificarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModificarAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnModificarAlquiler.setStyleSheet("QPushButton{\n"
                                                "    background-color: #2196f3;\n"
                                                "    border:none;\n"
                                                "    border-radius: 5px;\n"
                                                "    color:#fff;\n"
                                                "    padding-left: 15px;\n"
                                                "    padding-right: 15px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    background-color: #155db1;\n"
                                                "}\n"
                                                "")
        self.btnModificarAlquiler.setIcon(icon8)
        self.btnModificarAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnModificarAlquiler.setObjectName("btnModificarAlquiler")
        self.layoutUnoDos_2.addWidget(self.btnModificarAlquiler)
        self.btnEliminarAlquiler = QtWidgets.QPushButton(self.frameSeis_2)
        self.btnEliminarAlquiler.setMinimumSize(QtCore.QSize(120, 40))
        self.btnEliminarAlquiler.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnEliminarAlquiler.setFont(font)
        self.btnEliminarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEliminarAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnEliminarAlquiler.setStyleSheet("QPushButton{\n"
                                               "    background-color: #ff0000;\n"
                                               "    border:none;\n"
                                               "    border-radius: 5px;\n"
                                               "    color:#fff;\n"
                                               "    padding-left: 15px;\n"
                                               "    padding-right: 15px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    background-color: #b10005;\n"
                                               "}")
        self.btnEliminarAlquiler.setIcon(icon9)
        self.btnEliminarAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnEliminarAlquiler.setObjectName("btnEliminarAlquiler")
        self.layoutUnoDos_2.addWidget(self.btnEliminarAlquiler)
        self.layoutUno_2.addLayout(self.layoutUnoDos_2)
        self.verticalLayout_21.addLayout(self.layoutUno_2)
        self.verticalLayout_19.addWidget(self.frameSeis_2)
        self.verticalLayout_22.addWidget(self.frameArriba_2)
        self.frameAbajo_2 = QtWidgets.QFrame(self.alquiler)
        self.frameAbajo_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frameAbajo_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameAbajo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAbajo_2.setObjectName("frameAbajo_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frameAbajo_2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.gridUno_2 = QtWidgets.QGridLayout()
        self.gridUno_2.setSpacing(0)
        self.gridUno_2.setObjectName("gridUno_2")
        self.frameOcho_2 = QtWidgets.QFrame(self.frameAbajo_2)
        self.frameOcho_2.setStyleSheet("")
        self.frameOcho_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameOcho_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOcho_2.setObjectName("frameOcho_2")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frameOcho_2)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.tblAlquiler = QtWidgets.QTableWidget(self.frameOcho_2)
        self.tblAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tblAlquiler.setStyleSheet("QTableWidget::item{\n"
                                       "    border-color: rgb(44, 49, 60);\n"
                                       "    gridline-color: rgb(44, 49, 60);\n"
                                       "    padding: 10px\n"
                                       "}\n"
                                       "QTableWidget::item:selected{\n"
                                       "    background-color: #cdcdcd;\n"
                                       "}\n"
                                       "QHeaderView::section{\n"
                                       "    background-color: #fff;\n"
                                       "    border-style: none;\n"
                                       "    border-bottom: 1px solid #000;\n"
                                       "    padding: 5px\n"
                                       "}\n"
                                       "")
        self.tblAlquiler.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblAlquiler.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblAlquiler.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tblAlquiler.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tblAlquiler.setRowCount(0)
        self.tblAlquiler.setColumnCount(11)
        self.tblAlquiler.setObjectName("tblAlquiler")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        item.setFont(font)
        self.tblAlquiler.setHorizontalHeaderItem(10, item)
        self.tblAlquiler.horizontalHeader().setVisible(True)
        self.tblAlquiler.horizontalHeader().setCascadingSectionResizes(True)
        self.tblAlquiler.horizontalHeader().setDefaultSectionSize(170)
        self.tblAlquiler.horizontalHeader().setHighlightSections(True)
        self.tblAlquiler.horizontalHeader().setMinimumSectionSize(40)
        self.tblAlquiler.horizontalHeader().setStretchLastSection(True)
        self.tblAlquiler.verticalHeader().setVisible(False)
        self.tblAlquiler.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout_17.addWidget(self.tblAlquiler)
        self.gridUno_2.addWidget(self.frameOcho_2, 1, 0, 1, 1)
        self.frameNueve_2 = QtWidgets.QFrame(self.frameAbajo_2)
        self.frameNueve_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frameNueve_2.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frameNueve_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frameNueve_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameNueve_2.setObjectName("frameNueve_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frameNueve_2)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.paginasAlquileres = QtWidgets.QStackedWidget(self.frameNueve_2)
        self.paginasAlquileres.setStyleSheet("")
        self.paginasAlquileres.setObjectName("paginasAlquileres")
        self.alquileresRegistrar = QtWidgets.QWidget()
        self.alquileresRegistrar.setObjectName("alquileresRegistrar")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(
            self.alquileresRegistrar)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.frame_3 = QtWidgets.QFrame(self.alquileresRegistrar)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.framesRegistroAlquiler_2 = QtWidgets.QFrame(self.frame_3)
        self.framesRegistroAlquiler_2.setMinimumSize(QtCore.QSize(0, 50))
        self.framesRegistroAlquiler_2.setMaximumSize(
            QtCore.QSize(16777215, 50))
        self.framesRegistroAlquiler_2.setStyleSheet(
            "background-color: #009929;")
        self.framesRegistroAlquiler_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framesRegistroAlquiler_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framesRegistroAlquiler_2.setObjectName("framesRegistroAlquiler_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(
            self.framesRegistroAlquiler_2)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblTituloRegistroAlquiler = QtWidgets.QLabel(
            self.framesRegistroAlquiler_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.lblTituloRegistroAlquiler.setFont(font)
        self.lblTituloRegistroAlquiler.setStyleSheet("QLabel{\n"
                                                     "    background-color: transparent;\n"
                                                     "    color: #fff;\n"
                                                     "    padding: 10px;\n"
                                                     "}")
        self.lblTituloRegistroAlquiler.setObjectName(
            "lblTituloRegistroAlquiler")
        self.horizontalLayout_11.addWidget(self.lblTituloRegistroAlquiler)
        self.btnCerrarRegistroAlquiler = QtWidgets.QPushButton(
            self.framesRegistroAlquiler_2)
        self.btnCerrarRegistroAlquiler.setMinimumSize(QtCore.QSize(50, 0))
        self.btnCerrarRegistroAlquiler.setMaximumSize(
            QtCore.QSize(50, 16777215))
        self.btnCerrarRegistroAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrarRegistroAlquiler.setStyleSheet("QPushButton{\n"
                                                     "    border: none;\n"
                                                     "    background-color: transparent;\n"
                                                     "    padding: 10px;\n"
                                                     "}\n"
                                                     "")
        self.btnCerrarRegistroAlquiler.setText("")
        self.btnCerrarRegistroAlquiler.setIcon(icon10)
        self.btnCerrarRegistroAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnCerrarRegistroAlquiler.setObjectName(
            "btnCerrarRegistroAlquiler")
        self.horizontalLayout_11.addWidget(self.btnCerrarRegistroAlquiler)
        self.verticalLayout_29.addWidget(self.framesRegistroAlquiler_2)
        self.framesRegistroAlquiler = QtWidgets.QFrame(self.frame_3)
        self.framesRegistroAlquiler.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framesRegistroAlquiler.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framesRegistroAlquiler.setObjectName("framesRegistroAlquiler")
        self.txtDocumentoRegistroAlquiler = QtWidgets.QLineEdit(
            self.framesRegistroAlquiler)
        self.txtDocumentoRegistroAlquiler.setGeometry(
            QtCore.QRect(40, 80, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtDocumentoRegistroAlquiler.setFont(font)
        self.txtDocumentoRegistroAlquiler.setStyleSheet("QLineEdit{\n"
                                                        "    background-color: #d7d7d7;\n"
                                                        "    border: none;\n"
                                                        "    border-radius: 5px;\n"
                                                        "    padding: 10px;\n"
                                                        "}\n"
                                                        "QLineEdit:focus {\n"
                                                        "    border: 2px solid rgb(91, 101, 124);\n"
                                                        "}")
        self.txtDocumentoRegistroAlquiler.setMaxLength(12)
        self.txtDocumentoRegistroAlquiler.setClearButtonEnabled(True)
        self.txtDocumentoRegistroAlquiler.setObjectName(
            "txtDocumentoRegistroAlquiler")
        self.cmbPropiedadRegistroAlquiler = QtWidgets.QComboBox(
            self.framesRegistroAlquiler)
        self.cmbPropiedadRegistroAlquiler.setGeometry(
            QtCore.QRect(40, 140, 421, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.cmbPropiedadRegistroAlquiler.setFont(font)
        self.cmbPropiedadRegistroAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmbPropiedadRegistroAlquiler.setStyleSheet("QComboBox{\n"
                                                        "    background-color: #d7d7d7;\n"
                                                        "    border-radius: 5px;\n"
                                                        "    padding-left: 10px;\n"
                                                        "}\n"
                                                        "QComboBox:hover {\n"
                                                        "    border: 2px solid rgb(91, 101, 124);\n"
                                                        "}\n"
                                                        "\n"
                                                        "QComboBox, QAbstractItemView {\n"
                                                        "    color: #000;    \n"
                                                        "    background-color: #d7d7d7;\n"
                                                        "    selection-background-color: #cdcdcd;\n"
                                                        "    selection-color: #000;\n"
                                                        "}\n"
                                                        "QComboBox::drop-down {\n"
                                                        "    width: 30px;\n"
                                                        "    padding: 5px;\n"
                                                        "    image: url(:Iconos/seleccionar.png);\n"
                                                        "}")
        self.cmbPropiedadRegistroAlquiler.setObjectName(
            "cmbPropiedadRegistroAlquiler")
        self.cmbPropiedadRegistroAlquiler.addItem("")
        self.txtCantidadPersonasRegistroAlquiler = QtWidgets.QLineEdit(
            self.framesRegistroAlquiler)
        self.txtCantidadPersonasRegistroAlquiler.setGeometry(
            QtCore.QRect(40, 200, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCantidadPersonasRegistroAlquiler.setFont(font)
        self.txtCantidadPersonasRegistroAlquiler.setStyleSheet("QLineEdit{\n"
                                                               "    background-color: #d7d7d7;\n"
                                                               "    border: none;\n"
                                                               "    border-radius: 5px;\n"
                                                               "    padding: 10px;\n"
                                                               "}\n"
                                                               "QLineEdit:focus {\n"
                                                               "    border: 2px solid rgb(91, 101, 124);\n"
                                                               "}")
        self.txtCantidadPersonasRegistroAlquiler.setMaxLength(100)
        self.txtCantidadPersonasRegistroAlquiler.setClearButtonEnabled(True)
        self.txtCantidadPersonasRegistroAlquiler.setObjectName(
            "txtCantidadPersonasRegistroAlquiler")
        self.txtCantidadMascotasRegistroAlquiler = QtWidgets.QLineEdit(
            self.framesRegistroAlquiler)
        self.txtCantidadMascotasRegistroAlquiler.setGeometry(
            QtCore.QRect(250, 200, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCantidadMascotasRegistroAlquiler.setFont(font)
        self.txtCantidadMascotasRegistroAlquiler.setStyleSheet("QLineEdit{\n"
                                                               "    background-color: #d7d7d7;\n"
                                                               "    border: none;\n"
                                                               "    border-radius: 5px;\n"
                                                               "    padding: 10px;\n"
                                                               "}\n"
                                                               "QLineEdit:focus {\n"
                                                               "    border: 2px solid rgb(91, 101, 124);\n"
                                                               "}")
        self.txtCantidadMascotasRegistroAlquiler.setMaxLength(100)
        self.txtCantidadMascotasRegistroAlquiler.setClearButtonEnabled(True)
        self.txtCantidadMascotasRegistroAlquiler.setObjectName(
            "txtCantidadMascotasRegistroAlquiler")
        self.txtPrecioRegistroAlquiler = QtWidgets.QLineEdit(
            self.framesRegistroAlquiler)
        self.txtPrecioRegistroAlquiler.setGeometry(
            QtCore.QRect(40, 380, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtPrecioRegistroAlquiler.setFont(font)
        self.txtPrecioRegistroAlquiler.setStyleSheet("QLineEdit{\n"
                                                     "    background-color: #d7d7d7;\n"
                                                     "    border: none;\n"
                                                     "    border-radius: 5px;\n"
                                                     "    padding: 10px;\n"
                                                     "}\n"
                                                     "QLineEdit:focus {\n"
                                                     "    border: 2px solid rgb(91, 101, 124);\n"
                                                     "}")
        self.txtPrecioRegistroAlquiler.setText("")
        self.txtPrecioRegistroAlquiler.setClearButtonEnabled(True)
        self.txtPrecioRegistroAlquiler.setObjectName(
            "txtPrecioRegistroAlquiler")
        self.btnConfirmarRegistroAlquiler = QtWidgets.QPushButton(
            self.framesRegistroAlquiler)
        self.btnConfirmarRegistroAlquiler.setGeometry(
            QtCore.QRect(210, 450, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnConfirmarRegistroAlquiler.setFont(font)
        self.btnConfirmarRegistroAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConfirmarRegistroAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnConfirmarRegistroAlquiler.setStyleSheet("QPushButton{\n"
                                                        "    background-color: #1c1c1c;\n"
                                                        "    border:none;\n"
                                                        "    border-radius: 5px;\n"
                                                        "    color:#fff;\n"
                                                        "    padding-left: 15px;\n"
                                                        "    padding-right: 15px;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    background-color: #000000;\n"
                                                        "}")
        self.btnConfirmarRegistroAlquiler.setIcon(icon11)
        self.btnConfirmarRegistroAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnConfirmarRegistroAlquiler.setObjectName(
            "btnConfirmarRegistroAlquiler")
        self.btnCancelarRegistroAlquiler = QtWidgets.QPushButton(
            self.framesRegistroAlquiler)
        self.btnCancelarRegistroAlquiler.setGeometry(
            QtCore.QRect(340, 450, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnCancelarRegistroAlquiler.setFont(font)
        self.btnCancelarRegistroAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelarRegistroAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCancelarRegistroAlquiler.setStyleSheet("QPushButton{\n"
                                                       "    background-color: #7f7f7f;\n"
                                                       "    border:none;\n"
                                                       "    border-radius: 5px;\n"
                                                       "    color:#fff;\n"
                                                       "    padding-left: 15px;\n"
                                                       "    padding-right: 15px;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    background-color: #595959\n"
                                                       "}")
        self.btnCancelarRegistroAlquiler.setIcon(icon12)
        self.btnCancelarRegistroAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnCancelarRegistroAlquiler.setObjectName(
            "btnCancelarRegistroAlquiler")
        self.txtReservaRegistroAlquiler = QtWidgets.QLineEdit(
            self.framesRegistroAlquiler)
        self.txtReservaRegistroAlquiler.setGeometry(
            QtCore.QRect(40, 20, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtReservaRegistroAlquiler.setFont(font)
        self.txtReservaRegistroAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.txtReservaRegistroAlquiler.setStyleSheet("QLineEdit{\n"
                                                      "    background-color: #d7d7d7;\n"
                                                      "    border: none;\n"
                                                      "    border-radius: 5px;\n"
                                                      "    padding: 10px;\n"
                                                      "}\n"
                                                      "")
        self.txtReservaRegistroAlquiler.setText("")
        self.txtReservaRegistroAlquiler.setMaxLength(100)
        self.txtReservaRegistroAlquiler.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReservaRegistroAlquiler.setReadOnly(True)
        self.txtReservaRegistroAlquiler.setPlaceholderText("")
        self.txtReservaRegistroAlquiler.setClearButtonEnabled(False)
        self.txtReservaRegistroAlquiler.setObjectName(
            "txtReservaRegistroAlquiler")
        self.txtHoraLlegadaRegistroAlquiler = QtWidgets.QLineEdit(
            self.framesRegistroAlquiler)
        self.txtHoraLlegadaRegistroAlquiler.setGeometry(
            QtCore.QRect(250, 260, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtHoraLlegadaRegistroAlquiler.setFont(font)
        self.txtHoraLlegadaRegistroAlquiler.setStyleSheet("QLineEdit{\n"
                                                          "    background-color: #d7d7d7;\n"
                                                          "    border: none;\n"
                                                          "    border-radius: 5px;\n"
                                                          "    padding: 10px;\n"
                                                          "}\n"
                                                          "QLineEdit:focus {\n"
                                                          "    border: 2px solid rgb(91, 101, 124);\n"
                                                          "}")
        self.txtHoraLlegadaRegistroAlquiler.setText("")
        self.txtHoraLlegadaRegistroAlquiler.setMaxLength(5)
        self.txtHoraLlegadaRegistroAlquiler.setClearButtonEnabled(True)
        self.txtHoraLlegadaRegistroAlquiler.setObjectName(
            "txtHoraLlegadaRegistroAlquiler")
        self.dtFechaLlegadaRegistroAlquiler = QtWidgets.QDateEdit(
            self.framesRegistroAlquiler)
        self.dtFechaLlegadaRegistroAlquiler.setGeometry(
            QtCore.QRect(40, 260, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.dtFechaLlegadaRegistroAlquiler.setFont(font)
        self.dtFechaLlegadaRegistroAlquiler.setStyleSheet("QDateEdit{\n"
                                                          "    background-color: #d7d7d7;\n"
                                                          "    border: none;\n"
                                                          "    border-radius: 5px;\n"
                                                          "    padding: 10px;\n"
                                                          "}\n"
                                                          "QDateEdit:focus {\n"
                                                          "    border: 2px solid rgb(91, 101, 124);\n"
                                                          "}\n"
                                                          "\n"
                                                          "QDateEdit::drop-down {\n"
                                                          "    width: 30px;\n"
                                                          "    padding: 5px;\n"
                                                          "    image: url(:Iconos/calendario.png);\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCalendarWidget QToolButton{\n"
                                                          "height: 25px;\n"
                                                          "color: white;\n"
                                                          "font-size: 12px;\n"
                                                          "icon-size: 20px;\n"
                                                          "}\n"
                                                          "\n"
                                                          "\n"
                                                          "QCalendarWidget  QAbstractItemView{\n"
                                                          "font-size: 12px;\n"
                                                          "selection-color: white;\n"
                                                          "selection-background-color: #1597E5;\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCalendarWidget #qt_calendar_prevmonth {\n"
                                                          "   qproperty-icon: url(:Iconos/seleccionar-izquierda.png);\n"
                                                          "}\n"
                                                          "QCalendarWidget #qt_calendar_nextmonth {\n"
                                                          "   qproperty-icon: url(:Iconos/seleccionar-derecha.png);\n"
                                                          "}\n"
                                                          "")
        self.dtFechaLlegadaRegistroAlquiler.setCurrentSection(
            QtWidgets.QDateTimeEdit.DaySection)
        self.dtFechaLlegadaRegistroAlquiler.setCalendarPopup(True)
        self.dtFechaLlegadaRegistroAlquiler.setObjectName(
            "dtFechaLlegadaRegistroAlquiler")
        self.dtFechaSalidaRegistroAlquiler = QtWidgets.QDateEdit(
            self.framesRegistroAlquiler)
        self.dtFechaSalidaRegistroAlquiler.setGeometry(
            QtCore.QRect(40, 320, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.dtFechaSalidaRegistroAlquiler.setFont(font)
        self.dtFechaSalidaRegistroAlquiler.setStyleSheet("QDateEdit{\n"
                                                         "    background-color: #d7d7d7;\n"
                                                         "    border: none;\n"
                                                         "    border-radius: 5px;\n"
                                                         "    padding: 10px;\n"
                                                         "}\n"
                                                         "QDateEdit:focus {\n"
                                                         "    border: 2px solid rgb(91, 101, 124);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QDateEdit::drop-down {\n"
                                                         "    width: 30px;\n"
                                                         "    padding: 5px;\n"
                                                         "    image: url(:Iconos/calendario.png);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QCalendarWidget QToolButton{\n"
                                                         "height: 25px;\n"
                                                         "color: white;\n"
                                                         "font-size: 12px;\n"
                                                         "icon-size: 20px;\n"
                                                         "}\n"
                                                         "\n"
                                                         "\n"
                                                         "QCalendarWidget  QAbstractItemView{\n"
                                                         "font-size: 12px;\n"
                                                         "selection-color: white;\n"
                                                         "selection-background-color: #1597E5;\n"
                                                         "}\n"
                                                         "\n"
                                                         "QCalendarWidget #qt_calendar_prevmonth {\n"
                                                         "   qproperty-icon: url(:Iconos/seleccionar-izquierda.png);\n"
                                                         "}\n"
                                                         "QCalendarWidget #qt_calendar_nextmonth {\n"
                                                         "   qproperty-icon: url(:Iconos/seleccionar-derecha.png);\n"
                                                         "}\n"
                                                         "")
        self.dtFechaSalidaRegistroAlquiler.setCalendarPopup(True)
        self.dtFechaSalidaRegistroAlquiler.setObjectName(
            "dtFechaSalidaRegistroAlquiler")
        self.txtHoraSalidaRegistroAlquiler = QtWidgets.QLineEdit(
            self.framesRegistroAlquiler)
        self.txtHoraSalidaRegistroAlquiler.setGeometry(
            QtCore.QRect(250, 320, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtHoraSalidaRegistroAlquiler.setFont(font)
        self.txtHoraSalidaRegistroAlquiler.setStyleSheet("QLineEdit{\n"
                                                         "    background-color: #d7d7d7;\n"
                                                         "    border: none;\n"
                                                         "    border-radius: 5px;\n"
                                                         "    padding: 10px;\n"
                                                         "}\n"
                                                         "QLineEdit:focus {\n"
                                                         "    border: 2px solid rgb(91, 101, 124);\n"
                                                         "}")
        self.txtHoraSalidaRegistroAlquiler.setText("")
        self.txtHoraSalidaRegistroAlquiler.setMaxLength(5)
        self.txtHoraSalidaRegistroAlquiler.setClearButtonEnabled(True)
        self.txtHoraSalidaRegistroAlquiler.setObjectName(
            "txtHoraSalidaRegistroAlquiler")
        self.verticalLayout_29.addWidget(self.framesRegistroAlquiler)
        self.verticalLayout_30.addWidget(self.frame_3)
        self.paginasAlquileres.addWidget(self.alquileresRegistrar)
        self.alquileresModificar = QtWidgets.QWidget()
        self.alquileresModificar.setObjectName("alquileresModificar")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(
            self.alquileresModificar)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.frame_4 = QtWidgets.QFrame(self.alquileresModificar)
        self.frame_4.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.framesModificarAlquiler_2 = QtWidgets.QFrame(self.frame_4)
        self.framesModificarAlquiler_2.setMinimumSize(QtCore.QSize(0, 50))
        self.framesModificarAlquiler_2.setMaximumSize(
            QtCore.QSize(16777215, 50))
        self.framesModificarAlquiler_2.setStyleSheet(
            "background-color: #2196f3;")
        self.framesModificarAlquiler_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framesModificarAlquiler_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framesModificarAlquiler_2.setObjectName(
            "framesModificarAlquiler_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(
            self.framesModificarAlquiler_2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lblTituloModificarAlquiler = QtWidgets.QLabel(
            self.framesModificarAlquiler_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.lblTituloModificarAlquiler.setFont(font)
        self.lblTituloModificarAlquiler.setStyleSheet("QLabel{\n"
                                                      "    background-color: transparent;\n"
                                                      "    color: #fff;\n"
                                                      "    padding: 10px;\n"
                                                      "}")
        self.lblTituloModificarAlquiler.setObjectName(
            "lblTituloModificarAlquiler")
        self.horizontalLayout_10.addWidget(self.lblTituloModificarAlquiler)
        self.btnCerrarModificarAlquiler = QtWidgets.QPushButton(
            self.framesModificarAlquiler_2)
        self.btnCerrarModificarAlquiler.setMinimumSize(QtCore.QSize(50, 0))
        self.btnCerrarModificarAlquiler.setMaximumSize(
            QtCore.QSize(50, 16777215))
        self.btnCerrarModificarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrarModificarAlquiler.setStyleSheet("QPushButton{\n"
                                                      "    border: none;\n"
                                                      "    background-color: transparent;\n"
                                                      "    padding: 10px;\n"
                                                      "}\n"
                                                      "")
        self.btnCerrarModificarAlquiler.setText("")
        self.btnCerrarModificarAlquiler.setIcon(icon10)
        self.btnCerrarModificarAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnCerrarModificarAlquiler.setObjectName(
            "btnCerrarModificarAlquiler")
        self.horizontalLayout_10.addWidget(self.btnCerrarModificarAlquiler)
        self.verticalLayout_27.addWidget(self.framesModificarAlquiler_2)
        self.framesModificarAlquiler = QtWidgets.QFrame(self.frame_4)
        self.framesModificarAlquiler.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framesModificarAlquiler.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framesModificarAlquiler.setObjectName("framesModificarAlquiler")
        self.txtDocumentoModificarAlquiler = QtWidgets.QLineEdit(
            self.framesModificarAlquiler)
        self.txtDocumentoModificarAlquiler.setGeometry(
            QtCore.QRect(40, 80, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtDocumentoModificarAlquiler.setFont(font)
        self.txtDocumentoModificarAlquiler.setStyleSheet("QLineEdit{\n"
                                                         "    background-color: #d7d7d7;\n"
                                                         "    border: none;\n"
                                                         "    border-radius: 5px;\n"
                                                         "    padding: 10px;\n"
                                                         "}\n"
                                                         "QLineEdit:focus {\n"
                                                         "    border: 2px solid rgb(91, 101, 124);\n"
                                                         "}")
        self.txtDocumentoModificarAlquiler.setMaxLength(12)
        self.txtDocumentoModificarAlquiler.setClearButtonEnabled(True)
        self.txtDocumentoModificarAlquiler.setObjectName(
            "txtDocumentoModificarAlquiler")
        self.cmbPropiedadModificarAlquiler = QtWidgets.QComboBox(
            self.framesModificarAlquiler)
        self.cmbPropiedadModificarAlquiler.setGeometry(
            QtCore.QRect(40, 140, 421, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.cmbPropiedadModificarAlquiler.setFont(font)
        self.cmbPropiedadModificarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cmbPropiedadModificarAlquiler.setStyleSheet("QComboBox{\n"
                                                         "    background-color: #d7d7d7;\n"
                                                         "    border-radius: 5px;\n"
                                                         "    padding-left: 10px;\n"
                                                         "}\n"
                                                         "QComboBox:hover {\n"
                                                         "    border: 2px solid rgb(91, 101, 124);\n"
                                                         "}\n"
                                                         "\n"
                                                         "QComboBox, QAbstractItemView {\n"
                                                         "    color: #000;    \n"
                                                         "    background-color: #d7d7d7;\n"
                                                         "    selection-background-color: #cdcdcd;\n"
                                                         "    selection-color: #000;\n"
                                                         "}\n"
                                                         "QComboBox::drop-down {\n"
                                                         "    width: 30px;\n"
                                                         "    padding: 5px;\n"
                                                         "    image: url(:Iconos/seleccionar.png);\n"
                                                         "}")
        self.cmbPropiedadModificarAlquiler.setObjectName(
            "cmbPropiedadModificarAlquiler")
        self.cmbPropiedadModificarAlquiler.addItem("")
        self.txtCantidadPersonasModificarAlquiler = QtWidgets.QLineEdit(
            self.framesModificarAlquiler)
        self.txtCantidadPersonasModificarAlquiler.setGeometry(
            QtCore.QRect(40, 200, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCantidadPersonasModificarAlquiler.setFont(font)
        self.txtCantidadPersonasModificarAlquiler.setStyleSheet("QLineEdit{\n"
                                                                "    background-color: #d7d7d7;\n"
                                                                "    border: none;\n"
                                                                "    border-radius: 5px;\n"
                                                                "    padding: 10px;\n"
                                                                "}\n"
                                                                "QLineEdit:focus {\n"
                                                                "    border: 2px solid rgb(91, 101, 124);\n"
                                                                "}")
        self.txtCantidadPersonasModificarAlquiler.setMaxLength(100)
        self.txtCantidadPersonasModificarAlquiler.setClearButtonEnabled(True)
        self.txtCantidadPersonasModificarAlquiler.setObjectName(
            "txtCantidadPersonasModificarAlquiler")
        self.txtCantidadMascotasModificarAlquiler = QtWidgets.QLineEdit(
            self.framesModificarAlquiler)
        self.txtCantidadMascotasModificarAlquiler.setGeometry(
            QtCore.QRect(250, 200, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtCantidadMascotasModificarAlquiler.setFont(font)
        self.txtCantidadMascotasModificarAlquiler.setStyleSheet("QLineEdit{\n"
                                                                "    background-color: #d7d7d7;\n"
                                                                "    border: none;\n"
                                                                "    border-radius: 5px;\n"
                                                                "    padding: 10px;\n"
                                                                "}\n"
                                                                "QLineEdit:focus {\n"
                                                                "    border: 2px solid rgb(91, 101, 124);\n"
                                                                "}")
        self.txtCantidadMascotasModificarAlquiler.setMaxLength(100)
        self.txtCantidadMascotasModificarAlquiler.setClearButtonEnabled(True)
        self.txtCantidadMascotasModificarAlquiler.setObjectName(
            "txtCantidadMascotasModificarAlquiler")
        self.txtPrecioModificarAlquiler = QtWidgets.QLineEdit(
            self.framesModificarAlquiler)
        self.txtPrecioModificarAlquiler.setGeometry(
            QtCore.QRect(40, 380, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtPrecioModificarAlquiler.setFont(font)
        self.txtPrecioModificarAlquiler.setStyleSheet("QLineEdit{\n"
                                                      "    background-color: #d7d7d7;\n"
                                                      "    border: none;\n"
                                                      "    border-radius: 5px;\n"
                                                      "    padding: 10px;\n"
                                                      "}\n"
                                                      "QLineEdit:focus {\n"
                                                      "    border: 2px solid rgb(91, 101, 124);\n"
                                                      "}")
        self.txtPrecioModificarAlquiler.setText("")
        self.txtPrecioModificarAlquiler.setClearButtonEnabled(True)
        self.txtPrecioModificarAlquiler.setObjectName(
            "txtPrecioModificarAlquiler")
        self.btnConfirmarModificarAlquiler = QtWidgets.QPushButton(
            self.framesModificarAlquiler)
        self.btnConfirmarModificarAlquiler.setGeometry(
            QtCore.QRect(210, 450, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnConfirmarModificarAlquiler.setFont(font)
        self.btnConfirmarModificarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnConfirmarModificarAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnConfirmarModificarAlquiler.setStyleSheet("QPushButton{\n"
                                                         "    background-color: #1c1c1c;\n"
                                                         "    border:none;\n"
                                                         "    border-radius: 5px;\n"
                                                         "    color:#fff;\n"
                                                         "    padding-left: 15px;\n"
                                                         "    padding-right: 15px;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    background-color: #000000;\n"
                                                         "}")
        self.btnConfirmarModificarAlquiler.setIcon(icon11)
        self.btnConfirmarModificarAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnConfirmarModificarAlquiler.setObjectName(
            "btnConfirmarModificarAlquiler")
        self.btnCancelarModificarAlquiler = QtWidgets.QPushButton(
            self.framesModificarAlquiler)
        self.btnCancelarModificarAlquiler.setGeometry(
            QtCore.QRect(340, 450, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.btnCancelarModificarAlquiler.setFont(font)
        self.btnCancelarModificarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelarModificarAlquiler.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btnCancelarModificarAlquiler.setStyleSheet("QPushButton{\n"
                                                        "    background-color: #7f7f7f;\n"
                                                        "    border:none;\n"
                                                        "    border-radius: 5px;\n"
                                                        "    color:#fff;\n"
                                                        "    padding-left: 15px;\n"
                                                        "    padding-right: 15px;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    background-color: #595959\n"
                                                        "}")
        self.btnCancelarModificarAlquiler.setIcon(icon12)
        self.btnCancelarModificarAlquiler.setIconSize(QtCore.QSize(20, 20))
        self.btnCancelarModificarAlquiler.setObjectName(
            "btnCancelarModificarAlquiler")
        self.txtReservaModificarAlquiler = QtWidgets.QLineEdit(
            self.framesModificarAlquiler)
        self.txtReservaModificarAlquiler.setGeometry(
            QtCore.QRect(40, 20, 420, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtReservaModificarAlquiler.setFont(font)
        self.txtReservaModificarAlquiler.setCursor(
            QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.txtReservaModificarAlquiler.setStyleSheet("QLineEdit{\n"
                                                       "    background-color: #d7d7d7;\n"
                                                       "    border: none;\n"
                                                       "    border-radius: 5px;\n"
                                                       "    padding: 10px;\n"
                                                       "}\n"
                                                       "")
        self.txtReservaModificarAlquiler.setText("")
        self.txtReservaModificarAlquiler.setMaxLength(100)
        self.txtReservaModificarAlquiler.setAlignment(QtCore.Qt.AlignCenter)
        self.txtReservaModificarAlquiler.setReadOnly(True)
        self.txtReservaModificarAlquiler.setPlaceholderText("")
        self.txtReservaModificarAlquiler.setClearButtonEnabled(False)
        self.txtReservaModificarAlquiler.setObjectName(
            "txtReservaModificarAlquiler")
        self.txtHoraLlegadaModificarAlquiler = QtWidgets.QLineEdit(
            self.framesModificarAlquiler)
        self.txtHoraLlegadaModificarAlquiler.setGeometry(
            QtCore.QRect(250, 260, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtHoraLlegadaModificarAlquiler.setFont(font)
        self.txtHoraLlegadaModificarAlquiler.setStyleSheet("QLineEdit{\n"
                                                           "    background-color: #d7d7d7;\n"
                                                           "    border: none;\n"
                                                           "    border-radius: 5px;\n"
                                                           "    padding: 10px;\n"
                                                           "}\n"
                                                           "QLineEdit:focus {\n"
                                                           "    border: 2px solid rgb(91, 101, 124);\n"
                                                           "}")
        self.txtHoraLlegadaModificarAlquiler.setText("")
        self.txtHoraLlegadaModificarAlquiler.setMaxLength(5)
        self.txtHoraLlegadaModificarAlquiler.setClearButtonEnabled(True)
        self.txtHoraLlegadaModificarAlquiler.setObjectName(
            "txtHoraLlegadaModificarAlquiler")
        self.dtFechaLlegadaModificarAlquiler = QtWidgets.QDateEdit(
            self.framesModificarAlquiler)
        self.dtFechaLlegadaModificarAlquiler.setGeometry(
            QtCore.QRect(40, 260, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.dtFechaLlegadaModificarAlquiler.setFont(font)
        self.dtFechaLlegadaModificarAlquiler.setStyleSheet("QDateEdit{\n"
                                                           "    background-color: #d7d7d7;\n"
                                                           "    border: none;\n"
                                                           "    border-radius: 5px;\n"
                                                           "    padding: 10px;\n"
                                                           "}\n"
                                                           "QDateEdit:focus {\n"
                                                           "    border: 2px solid rgb(91, 101, 124);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QDateEdit::drop-down {\n"
                                                           "    width: 30px;\n"
                                                           "    padding: 5px;\n"
                                                           "    image: url(:Iconos/calendario.png);\n"
                                                           "}\n"
                                                           "\n"
                                                           "QCalendarWidget QToolButton{\n"
                                                           "height: 25px;\n"
                                                           "color: white;\n"
                                                           "font-size: 12px;\n"
                                                           "icon-size: 20px;\n"
                                                           "}\n"
                                                           "\n"
                                                           "\n"
                                                           "QCalendarWidget  QAbstractItemView{\n"
                                                           "font-size: 12px;\n"
                                                           "selection-color: white;\n"
                                                           "selection-background-color: #1597E5;\n"
                                                           "}\n"
                                                           "\n"
                                                           "QCalendarWidget #qt_calendar_prevmonth {\n"
                                                           "   qproperty-icon: url(:Iconos/seleccionar-izquierda.png);\n"
                                                           "}\n"
                                                           "QCalendarWidget #qt_calendar_nextmonth {\n"
                                                           "   qproperty-icon: url(:Iconos/seleccionar-derecha.png);\n"
                                                           "}\n"
                                                           "")
        self.dtFechaLlegadaModificarAlquiler.setCurrentSection(
            QtWidgets.QDateTimeEdit.DaySection)
        self.dtFechaLlegadaModificarAlquiler.setCalendarPopup(True)
        self.dtFechaLlegadaModificarAlquiler.setObjectName(
            "dtFechaLlegadaModificarAlquiler")
        self.dtFechaSalidaModificarAlquiler = QtWidgets.QDateEdit(
            self.framesModificarAlquiler)
        self.dtFechaSalidaModificarAlquiler.setGeometry(
            QtCore.QRect(40, 320, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.dtFechaSalidaModificarAlquiler.setFont(font)
        self.dtFechaSalidaModificarAlquiler.setStyleSheet("QDateEdit{\n"
                                                          "    background-color: #d7d7d7;\n"
                                                          "    border: none;\n"
                                                          "    border-radius: 5px;\n"
                                                          "    padding: 10px;\n"
                                                          "}\n"
                                                          "QDateEdit:focus {\n"
                                                          "    border: 2px solid rgb(91, 101, 124);\n"
                                                          "}\n"
                                                          "\n"
                                                          "QDateEdit::drop-down {\n"
                                                          "    width: 30px;\n"
                                                          "    padding: 5px;\n"
                                                          "    image: url(:Iconos/calendario.png);\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCalendarWidget QToolButton{\n"
                                                          "height: 25px;\n"
                                                          "color: white;\n"
                                                          "font-size: 12px;\n"
                                                          "icon-size: 20px;\n"
                                                          "}\n"
                                                          "\n"
                                                          "\n"
                                                          "QCalendarWidget  QAbstractItemView{\n"
                                                          "font-size: 12px;\n"
                                                          "selection-color: white;\n"
                                                          "selection-background-color: #1597E5;\n"
                                                          "}\n"
                                                          "\n"
                                                          "QCalendarWidget #qt_calendar_prevmonth {\n"
                                                          "   qproperty-icon: url(:Iconos/seleccionar-izquierda.png);\n"
                                                          "}\n"
                                                          "QCalendarWidget #qt_calendar_nextmonth {\n"
                                                          "   qproperty-icon: url(:Iconos/seleccionar-derecha.png);\n"
                                                          "}\n"
                                                          "")
        self.dtFechaSalidaModificarAlquiler.setCalendarPopup(True)
        self.dtFechaSalidaModificarAlquiler.setObjectName(
            "dtFechaSalidaModificarAlquiler")
        self.txtHoraSalidaModificarAlquiler = QtWidgets.QLineEdit(
            self.framesModificarAlquiler)
        self.txtHoraSalidaModificarAlquiler.setGeometry(
            QtCore.QRect(250, 320, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txtHoraSalidaModificarAlquiler.setFont(font)
        self.txtHoraSalidaModificarAlquiler.setStyleSheet("QLineEdit{\n"
                                                          "    background-color: #d7d7d7;\n"
                                                          "    border: none;\n"
                                                          "    border-radius: 5px;\n"
                                                          "    padding: 10px;\n"
                                                          "}\n"
                                                          "QLineEdit:focus {\n"
                                                          "    border: 2px solid rgb(91, 101, 124);\n"
                                                          "}")
        self.txtHoraSalidaModificarAlquiler.setText("")
        self.txtHoraSalidaModificarAlquiler.setMaxLength(5)
        self.txtHoraSalidaModificarAlquiler.setClearButtonEnabled(True)
        self.txtHoraSalidaModificarAlquiler.setObjectName(
            "txtHoraSalidaModificarAlquiler")
        self.verticalLayout_27.addWidget(self.framesModificarAlquiler)
        self.verticalLayout_28.addWidget(self.frame_4)
        self.paginasAlquileres.addWidget(self.alquileresModificar)
        self.verticalLayout_14.addWidget(self.paginasAlquileres)
        self.gridUno_2.addWidget(self.frameNueve_2, 1, 1, 1, 1)
        self.verticalLayout_13.addLayout(self.gridUno_2)
        self.verticalLayout_22.addWidget(self.frameAbajo_2)
        self.paginasPrincipales.addWidget(self.alquiler)
        self.verticalLayout_3.addWidget(self.paginasPrincipales)
        self.horizontalLayout_2.addWidget(self.frmMenuPrincipal)
        self.verticalLayout.addWidget(self.frameDos)
        self.horizontalLayout.addWidget(self.frameUno)
        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)
        self.paginasPrincipales.setCurrentIndex(0)
        self.paginasCliente.setCurrentIndex(0)
        self.paginasAlquileres.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "Apartamentos Anahi"))
        self.btnPrincipal.setText(_translate("Principal", "  Principal"))
        self.btnClientes.setText(_translate("Principal", "  Clientes"))
        self.btnReservas.setText(_translate("Principal", "  Alquileres"))
        self.btnCerrarSesion.setText(
            _translate("Principal", "  Cerrar sesion"))
        self.lblVersion.setText(_translate("Principal", "Beta v.23"))
        self.txtBuscarCliente.setPlaceholderText(
            _translate("Principal", "Buscar por documento.."))
        self.btnRegistrarCliente.setText(_translate("Principal", "Registrar"))
        self.btnModificarCliente.setText(_translate("Principal", "Modificar"))
        self.btnEliminarCliente.setText(_translate("Principal", "Eliminar"))
        item = self.tblClientes.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "Id"))
        item = self.tblClientes.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "Apellido"))
        item = self.tblClientes.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "Nombre"))
        item = self.tblClientes.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "Número de documento"))
        item = self.tblClientes.horizontalHeaderItem(4)
        item.setText(_translate("Principal", "Tipo de documento"))
        item = self.tblClientes.horizontalHeaderItem(5)
        item.setText(_translate("Principal", "Provincia"))
        item = self.tblClientes.horizontalHeaderItem(6)
        item.setText(_translate("Principal", "Ciudad"))
        item = self.tblClientes.horizontalHeaderItem(7)
        item.setText(_translate("Principal", "Celular"))
        item = self.tblClientes.horizontalHeaderItem(8)
        item.setText(_translate("Principal", "Correo"))
        self.lblUno.setText(_translate("Principal", "Registrar cliente"))
        self.txtApellidoRegistroCliente.setPlaceholderText(
            _translate("Principal", "Apellido"))
        self.cmbTipoDocumentoRegistroCliente.setItemText(
            0, _translate("Principal", "Tipo documento"))
        self.cmbProvinciaRegistroCliente.setItemText(
            0, _translate("Principal", "Provincia"))
        self.txtNombreRegistroCliente.setPlaceholderText(
            _translate("Principal", "Nombre"))
        self.txtDocumentoRegistroCliente.setPlaceholderText(
            _translate("Principal", "Número de documento"))
        self.txtCiudadRegistroCliente.setPlaceholderText(
            _translate("Principal", "Ciudad de origen"))
        self.txtCorreoRegistroCliente.setPlaceholderText(
            _translate("Principal", "Correo electronico"))
        self.txtCelularRegistroCliente.setPlaceholderText(
            _translate("Principal", "Celular"))
        self.btnConfirmarRegistroCliente.setText(
            _translate("Principal", "Confirmar"))
        self.btnCancelarRegistroCliente.setText(
            _translate("Principal", "Cancelar"))
        self.lblDos.setText(_translate("Principal", "Modificar cliente"))
        self.txtApellidoModificarCliente.setPlaceholderText(
            _translate("Principal", "Apellido"))
        self.cmbTipoDocumentoModificarCliente.setItemText(
            0, _translate("Principal", "Tipo documento"))
        self.cmbProvinciaModificarCliente.setItemText(
            0, _translate("Principal", "Provincia"))
        self.txtNombreModificarCliente.setPlaceholderText(
            _translate("Principal", "Nombre"))
        self.txtDocumentoModificarCliente.setPlaceholderText(
            _translate("Principal", "Número de documento"))
        self.txtCiudadModificarCliente.setPlaceholderText(
            _translate("Principal", "Ciudad de origen"))
        self.txtCorreoModificarCliente.setPlaceholderText(
            _translate("Principal", "Correo electronico"))
        self.txtCelularModificarCliente.setPlaceholderText(
            _translate("Principal", "Celular"))
        self.btnConfirmarModificarCliente.setText(
            _translate("Principal", "Confirmar"))
        self.btnCancelarModificarCliente.setText(
            _translate("Principal", "Cancelar"))
        self.txtBuscarAlquiler.setPlaceholderText(
            _translate("Principal", "Buscar por documento.."))
        self.btnRegistrarAlquiler.setText(_translate("Principal", "Registrar"))
        self.btnModificarAlquiler.setText(_translate("Principal", "Modificar"))
        self.btnEliminarAlquiler.setText(_translate("Principal", "Eliminar"))
        item = self.tblAlquiler.horizontalHeaderItem(0)
        item.setText(_translate("Principal", "Id"))
        item = self.tblAlquiler.horizontalHeaderItem(1)
        item.setText(_translate("Principal", "Cliente"))
        item = self.tblAlquiler.horizontalHeaderItem(2)
        item.setText(_translate("Principal", "Propiedad"))
        item = self.tblAlquiler.horizontalHeaderItem(3)
        item.setText(_translate("Principal", "Fecha de reserva"))
        item = self.tblAlquiler.horizontalHeaderItem(4)
        item.setText(_translate("Principal", "Cantidad de personas"))
        item = self.tblAlquiler.horizontalHeaderItem(5)
        item.setText(_translate("Principal", "Cantidad de mascotas"))
        item = self.tblAlquiler.horizontalHeaderItem(6)
        item.setText(_translate("Principal", "Fecha llegada"))
        item = self.tblAlquiler.horizontalHeaderItem(7)
        item.setText(_translate("Principal", "Hora llegada"))
        item = self.tblAlquiler.horizontalHeaderItem(8)
        item.setText(_translate("Principal", "Fecha salida"))
        item = self.tblAlquiler.horizontalHeaderItem(9)
        item.setText(_translate("Principal", "Hora salida"))
        item = self.tblAlquiler.horizontalHeaderItem(10)
        item.setText(_translate("Principal", "Precio"))
        self.lblTituloRegistroAlquiler.setText(
            _translate("Principal", "Registrar alquiler"))
        self.txtDocumentoRegistroAlquiler.setPlaceholderText(
            _translate("Principal", "Número de documento"))
        self.cmbPropiedadRegistroAlquiler.setItemText(
            0, _translate("Principal", "Propiedad"))
        self.txtCantidadPersonasRegistroAlquiler.setPlaceholderText(
            _translate("Principal", "Cantidad de personas"))
        self.txtCantidadMascotasRegistroAlquiler.setPlaceholderText(
            _translate("Principal", "Cantidad de mascotas"))
        self.txtPrecioRegistroAlquiler.setPlaceholderText(
            _translate("Principal", "Precio"))
        self.btnConfirmarRegistroAlquiler.setText(
            _translate("Principal", "Confirmar"))
        self.btnCancelarRegistroAlquiler.setText(
            _translate("Principal", "Cancelar"))
        self.txtHoraLlegadaRegistroAlquiler.setPlaceholderText(
            _translate("Principal", "Hora de llegada"))
        self.dtFechaLlegadaRegistroAlquiler.setDisplayFormat(
            _translate("Principal", "dd/MM/yyyy"))
        self.txtHoraSalidaRegistroAlquiler.setPlaceholderText(
            _translate("Principal", "Hora de salida"))
        self.lblTituloModificarAlquiler.setText(
            _translate("Principal", "Modificar alquiler"))
        self.txtDocumentoModificarAlquiler.setPlaceholderText(
            _translate("Principal", "Número de documento"))
        self.cmbPropiedadModificarAlquiler.setItemText(
            0, _translate("Principal", "Propiedad"))
        self.txtCantidadPersonasModificarAlquiler.setPlaceholderText(
            _translate("Principal", "Cantidad de personas"))
        self.txtCantidadMascotasModificarAlquiler.setPlaceholderText(
            _translate("Principal", "Cantidad de mascotas"))
        self.txtPrecioModificarAlquiler.setPlaceholderText(
            _translate("Principal", "Precio"))
        self.btnConfirmarModificarAlquiler.setText(
            _translate("Principal", "Confirmar"))
        self.btnCancelarModificarAlquiler.setText(
            _translate("Principal", "Cancelar"))
        self.txtHoraLlegadaModificarAlquiler.setPlaceholderText(
            _translate("Principal", "Hora de llegada"))
        self.dtFechaLlegadaModificarAlquiler.setDisplayFormat(
            _translate("Principal", "dd/MM/yyyy"))
        self.txtHoraSalidaModificarAlquiler.setPlaceholderText(
            _translate("Principal", "Hora de salida"))
