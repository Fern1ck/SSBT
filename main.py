import schedule
from funcs import MakeValid, get_TO_PATH, get_FROM_PATH, getTime, MakeBackup

#The execution begins
FROM, TO = MakeValid(get_FROM_PATH(), get_TO_PATH())

Minutes = input(getTime() + "How frequent would you like your backups to be made? Enter the number of minutes: ")

while not Minutes.isnumeric():
    input("Please enter a valid number of minutes.")
    Minutes = input(getTime() + "How frequent would you like your backups to be made? Enter the number of minutes: ")

schedule.every(round(float(Minutes))).minutes.do(MakeBackup, FROM, TO)
MakeBackup(FROM, TO)

while(True):
    schedule.run_pending()
