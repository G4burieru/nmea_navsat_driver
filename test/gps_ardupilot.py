import serial
import time

serial_sitl = serial.Serial("/dev/ttyVSP0", 115200)
f = open("logs/nmea_messages.log", "r")

# print only GPS sentences
for line in f:
    if line[0:4] == "$GPG":
        # joga dados na serial
        serial_sitl.write(line.encode())
        print(line)
        time.sleep(0.2)