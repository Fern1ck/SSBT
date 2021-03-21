import os, pathlib, shutil
from datetime import datetime

def getTime():
    return "[" + datetime.now().strftime("%d/%m/%y %H:%M") + "] "

def IsFROMValid(path):
    #Check if the path to backup exists
    if(pathlib.Path(path).is_dir() or pathlib.Path(path).is_file()):
        return True
    else:
        return False

def IsTOValid(path):
    #Check if the path to save the backups in exists and is not a file 
    if(pathlib.Path(path).is_dir() and not pathlib.Path(path).is_file()):
        return True
    else:
        return False

def MakeBackup(FROM, TO):
    try:
        if(pathlib.Path(FROM).is_dir()):
            if pathlib.Path(TO).exists():
                shutil.rmtree(TO)

            shutil.copytree(FROM, TO)
        else:
            filename = os.path.basename(FROM)
            shutil.copyfile(FROM, F"{TO}/{filename}")
        return
    except PermissionError:
        print("The permission to access a directory has been denied. Try running SSBT as an administrator.")
        exit()