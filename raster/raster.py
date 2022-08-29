from PyQt5.QtWidgets import *
from krita import *
from .funkcje import szachownica, rasteryzacja, losowanie

class DockerExample(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raster i PixelArt")
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)

        popupButton = QPushButton("PopUp", mainWidget)
        popupButton.clicked.connect(self.popup)

        szachPrzycisk = QPushButton("Szachownica", mainWidget)
        szachPrzycisk.clicked.connect(self.szach)

        rastrPrzycisk = QPushButton("Rasteryzacja", mainWidget)
        rastrPrzycisk.clicked.connect(self.raster)

        losPrzycisk = QPushButton("Losowanie", mainWidget)
        losPrzycisk.clicked.connect(self.losowanie)

        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(popupButton)
        mainWidget.layout().addWidget(szachPrzycisk)
        mainWidget.layout().addWidget(rastrPrzycisk)
        mainWidget.layout().addWidget(losPrzycisk)

    def popup(self):

        QMessageBox.information(QWidget(), "Nazwa okna", "To dziala!")

##--------------------------------------------------------------
    def raster(self):
        width = Krita.instance().activeDocument().width()
        height = Krita.instance().activeDocument().height()

        l = Krita.instance().activeDocument().activeNode()  # get current layer
        data = l.pixelData(0, 0, width, height)  # get pixels as QByteArray

        rasteryzacja(width, height, data, 6)
        l.setPixelData(data, 0, 0, width, height)  # copy back to image
        Krita.instance().activeDocument().refreshProjection()  # refresh

    def losowanie(self):
        width = Krita.instance().activeDocument().width()
        height = Krita.instance().activeDocument().height()

        l = Krita.instance().activeDocument().activeNode()  # get current layer
        data = l.pixelData(0, 0, width, height)  # get pixels as QByteArray

        losowanie(width, height, data, 6)
        l.setPixelData(data, 0, 0, width, height)  # copy back to image
        Krita.instance().activeDocument().refreshProjection()  # refresh

    def szach(self):
        width = Krita.instance().activeDocument().width()
        height = Krita.instance().activeDocument().height()

        l = Krita.instance().activeDocument().activeNode()  # get current layer
        data = l.pixelData(0, 0, width, height)  # get pixels as QByteArray

        szachownica(width, height, data, 0, 0, 0, 255)
        l.setPixelData(data, 0, 0, width, height)  # copy back to image
        Krita.instance().activeDocument().refreshProjection()  # refresh
##-----------------------------------------------------------------------

    def canvasChanged(self, canvas):
        pass

Krita.instance().addDockWidgetFactory(DockWidgetFactory("Rasteryzacja", DockWidgetFactoryBase.DockRight, DockerExample))