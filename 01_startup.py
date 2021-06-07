# einfaches Grundgeruest einer startup.py
from qgis.gui import QgsMessageBar
from qgis.utils import iface
from qgis.PyQt.QtCore import QSettings


settings=QSettings()

def settingsfunktion():
    # ---------------------- Settings --------------------
    settings.setValue("/Projections/showDatumTransformDialog", True)
    # siehe QGIS3.ini fuer korrekte Schreibweise einzelner Settings

iface.initializationCompleted.connect(settingsfunktion)    
    
iface.messageBar().pushMessage("Error", "Achtung: XXX nicht korrekt", level=2, duration=60) #2 steht fuer Qgis.CRITICAL

