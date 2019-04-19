from datetime import datetime
from datetime import date
import string

def write2TextFile(workDone):
    currentDatetime = date.today()
    fileOpen = open("abc.txt", 'a+')
    fileOpen.write("#####################################################\r\n")
    fileOpen.write("%s : " % (datetime.now().strftime("%Y%m%d-%H%M%S")))
    fileOpen.write(str(workDone)+"\n")
    fileOpen.close()

write2TextFile("Hello World.")
