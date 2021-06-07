with open(r"C:\testdaten\layer_am_start.csv", 'r', encoding='utf-8') as infile:
    for line in infile:
        #print(line)
        array = line.split(';')
        layerpfad=array[0]
        layername=array[1]

        vlayer = QgsVectorLayer(layerpfad, layername, "ogr")
        if not vlayer.isValid():
            print("Layer failed to load!")
        else:
            QgsProject.instance().addMapLayer(vlayer)