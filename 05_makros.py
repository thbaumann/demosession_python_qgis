# https://gis.stackexchange.com/questions/186309/open-qgis-project-files-in-exclusive-mode-alert-if-project-file-already-in-use

import os
import socket
from qgis.core import QgsProject
from PyQt5.QtWidgets import QMessageBox


### utility functions ###

# get the executing machine and process id #
def _getId():
    return socket.getfqdn()+'.'+str(os.getpid())

# read machine and process id holding lock from lock file #  
def _getLockerId(file):
    try:
        with open(file) as _file:
            return _file.readline()
    except:
        return

# create lock file path #
def _getLockFile():
    _path, _file = __getProjectPath()
    return os.path.join(_path,'.'+_file+'.lock')
    
# create current project file path root and name #
def __getProjectPath():
    return os.path.split(QgsProject.instance().absoluteFilePath())  


### QGIS macros ###

def openProject():
    lockfile = _getLockFile()
    
    try:
        with open(lockfile, "x") as _file:
            _file.write(_getId())
    except OSError:
        _path, _file = __getProjectPath()
        copyfile = os.path.join(_path, _getId() + "__" + _file)
        
        QMessageBox.information(
            None,
            "Project locked",
            "Cannot open project with write access: "+
              "the following user (user.PID)\n\n"+_getLockerId(lockfile)+
              "\n\nhas already aquired a lock on the project!"+
              "\nCopying project and switching context to\n\n"+copyfile
        )

        QgsProject.instance().write(copyfile)
        QgsProject.instance().read()
        QgsProject.instance().setDirty()

def saveProject():
    pass

def closeProject():
    lockfile = _getLockFile()
    
    if _getId() == _getLockerId(lockfile):
        os.remove(lockfile)