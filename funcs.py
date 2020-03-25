import os, pathlib, shutil
from datetime import datetime

FILE_NAME_TO = "backupTO.txt"
FILE_NAME_FROM = "backupFROM.txt"

def getTime():
    return "[" + datetime.now().strftime("%d/%m/%y %H:%M") + "] "

def readFile(filePATH):
    try:
        file = open(filePATH, "r+") #Open with read and write permission
    except FileNotFoundError:
        file = open(filePATH, "w") #It creates the file to store the path
        file.close()
        file = open(filePATH, "r+") #Open with read and write permission
    return file

def get_FROM_PATH():
    #Get the source paths
    file = readFile(FILE_NAME_FROM)
    fileContents = file.read().splitlines()

    if(len(fileContents) == 0):
        file.seek(0)
        file.truncate()
        THINGS = []
        CONFIRMATION = True

        while(CONFIRMATION):
            THING= input(getTime() + "Enter the path of the thing you'd like to make a backup of: ")
            THINGS.append(THING)
            if(input(getTime() + "Would you like to make backups of something else? (Y/N): ").upper != "Y"):
                CONFIRMATION = False
  
        file.writelines(THINGS)
        file.close()
        return THINGS
    else:
        THINGS = fileContents
        file.close()
        return THINGS

def get_TO_PATH():
    #Get the destination paths
    file = readFile(FILE_NAME_TO)
    fileContents = file.read()

    if(fileContents == ""):
        file.seek(0)
        file.truncate()
        PATH= input(getTime() + "Enter the path of the directory where you'd like to save your backup: ")
        file.write(PATH)
        file.writelines(PATH)
        file.close()
        return PATH
    else:
        PATH = fileContents
        file.close()
        return PATH

def MakeValid(FROM_THINGS, TO_PATH):
    #Check if the paths exist in the system
    DOESNOTEXIST= []
    FROM = []
    for path in FROM_THINGS:
        FROM_line = pathlib.Path(path)
        if not FROM_line.exists():
            DOESNOTEXIST.append(FROM_line)
        else:
            FROM.append(FROM_line)
        
    if len(DOESNOTEXIST) > 0:
        print(getTime() + "The following paths of the things you'd like to backup don't exist:")
        for i in DOESNOTEXIST:
            print(i)
        input("\nPlease enter again the paths of the things you'd like to backup") #REVIEW
        os.remove(FILE_NAME_TO)
        TO = pathlib.Path(get_TO_PATH())

    TO = pathlib.Path(TO_PATH)
    while not (TO.exists() and TO.is_dir()):
        input(getTime() + "The path of the directory where you'd like to save your backup doesn't exist.")
        print("")
        os.remove(FILE_NAME_TO)
        TO = pathlib.Path(get_TO_PATH())

    #Check if the source and the destination path are not equal
    return [FROM, TO]

def MakeBackup(FROM, TO):
    print(getTime() + "Starting to make the backup...")
    #Create the directories based on the date and the time

    DAY_DATE_NAME = pathlib.Path(str(datetime.now().strftime("%d-%m-%y")))
    DATE_DIR_NAME = TO/DAY_DATE_NAME

    TIME_DATE_NAME = pathlib.Path(str(datetime.now().strftime("%H.%M")))
    TIME_DIR_NAME = DATE_DIR_NAME/TIME_DATE_NAME

    if TIME_DIR_NAME.exists():
        shutil.rmtree(DATE_DIR_NAME)

    for ITEM in FROM:
        if pathlib.Path(ITEM).is_dir():
            BACKUP_DIR_NAME = TIME_DIR_NAME/os.path.basename(os.path.normpath(ITEM))
            try:
                shutil.copytree(ITEM, BACKUP_DIR_NAME)
                print(getTime() + "The backup has been successful. It's saved in " + str(TIME_DIR_NAME))
            except Exception as e:
                input("There was an error when creating the backup: " + str(e))
        else:
            try:
                os.makedirs(TIME_DIR_NAME)
                shutil.copy2(ITEM, TIME_DIR_NAME) #shutil.copy2 preserves metadata
                print(getTime() + "The backup has been successful. It's saved in " + str(TIME_DIR_NAME))
            except Exception as e:
                input("There was an error when creating the backup: " + str(e))