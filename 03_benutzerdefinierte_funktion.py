from qgis.core import *
from qgis.gui import *
import os.path
@qgsfunction(args='auto', group='Custom',usesgeometry=False)
def layername_aus_pfad(current_path, feature, parent):
    """
    Layername aus dem Pfad ermitteln
    current_path: an die Funktion uebergebener pfad, wie z.B. layer_by_path
    Bsp: layername_aus_pfad('C:/testdaten/Tektonik.shp')
    """
    path=os.path.normpath(current_path)
    print(path)
    for layer in QgsProject.instance().mapLayers().values():
        print('pfad: '+os.path.normpath(layer.dataProvider().dataSourceUri()).split('|')[0])
        if path in (os.path.normpath(layer.dataProvider().dataSourceUri()).split('|')[0]):
            return(layer.name())