#https://courses.spatialthoughts.com/pyqgis-in-a-day.html#creating-custom-python-actions
#Testdaten/Projekt: sf.gpkg / sf.qgz (Download über: https://courses.spatialthoughts.com/pyqgis-in-a-day.html#get-the-data-package )

layer = QgsProject.instance().mapLayer('[% @layer_id %]')
layer.selectByExpression('"block_num"=\'[% block_num %]\'')

# Beispiel: Weitere Aktionen durch Plugins: https://github.com/opengisch/qgis-actions-for-relations 
