#this script just takes current data from the RIGOL DM3058E over an allotted time
import visa
import time
import csv
from visa import constants


#modify test time in seconds
testTime = 200

#setting up dmm conection
rm = visa.ResourceManager()

#you can receive the instrument's ID if you use print(rm.list_resources())
print(rm.list_resources())

dmm = rm.open_resource('USB0::0x1AB1::0x09C4::DM3R194201991::INSTR')

#writes data in a csv
f = open('datapoint.csv','w')

#timed loop
timeEnd = time.time() + testTime

print('Experiment has started. DO NOT CLOSE THIS WINDOW.')
flag = 0;
count = 0;
inject = []
timeStart = time.time()
while time.time()<timeEnd:
	if round(time.time()-timeStart)==200:
		f.write("\n")
	f.write(dmm.query(":MEASure:CURRent:DC?"))
	print(timeEnd - time.time())
	print(count)
	count = count+1

f.close()

