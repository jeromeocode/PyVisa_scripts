#this script just takes current data from the RIGOL DM3058E over an allotted time
import visa
import time
import csv
from visa import constants


#modify test time in seconds
testTime = 90*60

#setting up dmm conection
rm = visa.ResourceManager()

#you can receive the instrument's ID if you use print(rm.list_resources())
print(rm.list_resources())

#wait for keypress to start the timer
start = input("Enter a key to start the program")
print('Experiment has started. DO NOT CLOSE THIS WINDOW.')

# dmm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R194201991::INSTR') #TODO: Figure this out
dmm = rm.open_resource('GPIB0::12::INSTR')

load = rm.open_resource('GPIB1::4::INSTR')

#timed loop
timeEnd = time.time() + testTime
timeStart = time.time()

#start counter
count = 0

load.write("OUTput ON")

#writes data in a csv
with open('results_1.csv', 'w', newline='') as csvfile:
  fields = ['time', 'Voltage (V)', 'Current (A)']
  writer = csv.DictWriter(csvfile, fieldnames=fields)

  #outputs headers
  writer.writeheader()

  dmmReading = 999999

  #loops until time runs out
  while dmmReading>2.5:
    currTime = float(time.time())
    dmmReading = float(dmm.query(":MEASure:VOLTage:DC?"))
    currReading = float(load.query(":MEASure:CURRent:DC?"))

    writer.writerow({'time': currTime, 'Voltage (V)': dmmReading, 'Current (A)': currReading})

    #console printouts so that the user has a visible timer
    print(time.time())
    print(count)
    print(dmmReading)
    print(currReading)
    count = count+1
    csvfile.flush()
    time.sleep(1)
  load.write("OUTput OFF")