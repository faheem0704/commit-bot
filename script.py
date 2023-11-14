from datetime import datetime
  
now = datetime.now()
nowString = now.strftime("%m/%d/%Y, %H:%M:%S")

dateandtime = nowString + "\n"

with open("output.txt", "a") as myfile:
    myfile.write(dateandtime)