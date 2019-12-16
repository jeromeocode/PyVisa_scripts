import serial
import time

ser = serial.Serial('COM12', 115200) #TODO: figure out com port for BOLT

while True:
    s = ser.read_until()
    print(s.decode('utf-8'))
    time.sleep(1)