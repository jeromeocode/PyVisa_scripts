#this script just takes current data from the RIGOL DM3058E over an allotted time
import visa
import time
import csv
from visa import constants


#modify test time in seconds
testTime = 30

#setting up dmm conection
rm = visa.ResourceManager()

#you can receive the instrument's ID if you use print(rm.list_resources())
print(rm.list_resources())

#wait for keypress to start the timer
start = input("Enter a key to start the program")

# dmm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R194201991::INSTR') #TODO: Figure this out
dmm = rm.open_resource('GPIB0::11::INSTR')

#timed loop
timeEnd = time.time() + testTime

print('Experiment has started. DO NOT CLOSE THIS WINDOW.')

count = 0

timeStart = time.time()
#writes data in a csv
with open('results.csv', 'w', newline='') as csvfile:
  fields = ['time', 'current']
  writer = csv.DictWriter(csvfile, fieldnames=fields)

  #outputs headers
  writer.writeheader()

  #loops until time runs out
  while time.time()<timeEnd:
    currTime = float(time.time() - timeStart)
    dmmCurrent = float(dmm.query(":MEASure:CURRent:DC?"))

    writer.writerow({'time': currTime, 'current': dmmCurrent})

    #console printouts so that the user has a visible timer
    print(timeEnd - time.time())
    print(count)
    print(dmmCurrent)
    count = count+1
    csvfile.flush()
    time.sleep(0.1)