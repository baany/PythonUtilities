import re
stringVal = "abc 234 down 234 up up down".lower()
indexUp = [m.start() for m in re.finditer('up', stringVal)]
indexDown = [n.start() for n in re.finditer('down', stringVal)]
print (indexUp)
print (indexDown)

