#this script just takes current data from the RIGOL DM3058E over an allotted time
import visa
import time
import csv
import serial
from visa import constants

#setting up GPI-B/RS232 conection
rm = visa.ResourceManager()

#Print all devices' data that are attached to computer
print(rm.list_resources())


#wait for keypress to start the timer
start = input("Enter a key to start the program")

#Open device, the input is taken from output of line 12
dmm = rm.open_resource('GPIB0::16::INSTR')

#open Serial comms to Bolt Board
ser = serial.Serial('COM15', 115200) #TODO: figure out com port for BOLT


print('Experiment has started. DO NOT CLOSE THIS WINDOW.')

count = 0

timeStart = time.time()

#writes data in a csv
with open('results.csv', 'w', newline='') as csvfile:
  fields = ['Time (s)', 'Temp (C)', 'Sensor Data' ]
  writer = csv.DictWriter(csvfile, fieldnames=fields)

  #outputs headers
  writer.writeheader()

  #loops until time runs out
  while True:
    
    currTime = float(time.time())

    s = ser.read_until()
    s = s.decode('utf-8')

    tempReading = dmm.query("TEMP?")

    writer.writerow({'Time (s)': currTime, 'Temp (C)': tempReading, 'Sensor Data': s})

    #console printouts so that the user has a visible timer
    print(time.time())
    print(count)
    print(s)
    print(tempReading)
    count = count+1
    csvfile.flush()
