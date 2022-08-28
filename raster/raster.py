from krita import *
from PyQt5.QtWidgets import QWidget, QAction, QMessageBox
from .funkcje import szachownica, rasteryzacja, losowanie

class Raster(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    # Krita.instance() exists, so do any setup work
    def setup(self):
        pass

    def system_check(self):
        # QMessageBox creates quick popup with information
        messageBox = QMessageBox()
        messageBox.setInformativeText(Application.version())
        messageBox.setWindowTitle('System Check')
        messageBox.setText("Hello! Here is the version of Krita you are using.");
        messageBox.setStandardButtons(QMessageBox.Close)
        messageBox.setIcon(QMessageBox.Information)
        messageBox.exec()

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



    # called after setup(self)
    def createActions(self, window):
        #action = window.createAction("", "System Check")
        #action.triggered.connect(self.system_check)

        action2 = window.createAction("", "Raster")
        action2.triggered.connect(self.raster)

        #action3 = window.createAction("", "Szachownica")
        #action3.triggered.connect(self.szach)

        #action4 = window.createAction("", "Losowanie")
        #action4.triggered.connect(self.losowanie)
