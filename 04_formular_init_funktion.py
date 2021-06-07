from qgis.PyQt.QtWidgets import QWidget

def kontrolle(dialog, layer, feature):
    #geom = feature.geometry()
    control = dialog.findChild(QWidget, "TEKTYP")
    #print(control)
    control.setStyleSheet("background-color: rgba(0, 107, 107, 150);color: rgba(255, 05, 05, 150);")

