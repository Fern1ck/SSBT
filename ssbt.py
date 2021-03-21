import time,argparse, pathlib
from funcs import IsFROMValid, IsTOValid, MakeBackup, getTime

parser = argparse.ArgumentParser("Automated backups at a certain interval.")
parser.add_argument("--src", metavar="", nargs="+", type=str, required=True, help="The path or file to make backups of")
parser.add_argument("--dest", metavar="", type=str, required=True, help="The path the backups are going to be saved in")
timeGroup = parser.add_mutually_exclusive_group(required=True)
timeGroup.add_argument("--minutes", metavar="", type=int, help="The interval in minutes")
timeGroup.add_argument("--seconds", metavar="", type=int, help="The interval in seconds")
args = parser.parse_args()

FROM = args.src #List of paths
TO = args.dest
MINUTES = args.minutes
SECONDS = args.seconds

#Validate the arguments
for path in FROM:
    if(not IsFROMValid(path)):
        print(f"{FROM} is not a valid directory or file.")
        exit()

if(not IsTOValid(pathlib.Path(TO).parent.absolute())):
    print(f"{TO} is not a valid directory.")
    exit()
   
if(MINUTES and MINUTES < 1):
    print("The number of minutes has to be above 0")
    exit()
elif(SECONDS and SECONDS < 1):
    print("The number of seconds has to be above 0")
    exit()

try:
    while(True):
        for path in FROM:
            MakeBackup(path, TO)

        print(getTime() + "Backup done.")
        if(MINUTES):
            time.sleep(60 * MINUTES)
        else:
            time.sleep(int(SECONDS))
except KeyboardInterrupt:
    print(f"Your backups are saved in: {TO}")
    
