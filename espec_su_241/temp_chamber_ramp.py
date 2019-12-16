#this script just takes current data from the RIGOL DM3058E over an allotted time
import visa
import time
import csv
import serial
from visa import constants

def ramp_2_temp(tmp_1, tmp_2, t_sample, t_ramp, t_start):
    set_temp = tmp_1
    #loops until time runs out
    while (time.time()-t_start) < t_ramp:
    
        currTime = float(time.time())

        set_temp_string = "TEMP, S" + set_temp + " H80 L-40"
        dmm.write(set_temp_string)
        
        tempReading = dmm.query("TEMP?")

        writer.writerow({'Time (s)': currTime, 'Temp (C)': tempReading})

        #console printouts so that the user has a visible timer
        print(time.time()-timeStart)
        print(tempReading)
        csvfile.flush()

        set_temp = set_temp - dt1

        time.sleep(sample_time)



#setting up GPI-B/RS232 conection
rm = visa.ResourceManager()

#Print all devices' data that are attached to computer
print(rm.list_resources())


#wait for keypress to start the timer
start = input("Enter a key to start the program")

#Open device, the input is taken from output of line 12
dmm = rm.open_resource('GPIB0::16::INSTR')


print('Experiment has started. DO NOT CLOSE THIS WINDOW.')

sample_time = 9*60
ramp_time = 3*60*60

#modifiable temps
temp0 = 25
temp1 = -30
temp2 = 70
settle_time = 1*60*60
dt1 = (temp2 - temp1) * sample_time / ramp_time #5 degree increments



#writes data in a csv
with open('results.csv', 'w', newline='') as csvfile:
    fields = ['Time (s)', 'Temp (C)']
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    #outputs headers
    writer.writeheader()

    set_temp = temp0
    timeStart = time.time()
    #loops until time runs out
    while (time.time()-timeStart) < (temp0-temp1)*sample_time/dt1:
    
        currTime = float(time.time())

        set_temp_string = "TEMP, S" + str(set_temp) + " H80 L-40"
        dmm.write(set_temp_string)
        
        tempReading = dmm.query("TEMP?")

        writer.writerow({'Time (s)': currTime, 'Temp (C)': tempReading})

        #console printouts so that the user has a visible timer
        print(time.time()-timeStart)
        print(tempReading)
        csvfile.flush()

        set_temp = set_temp - dt1

        time.sleep(sample_time)

    timeStart = time.time()
    while (time.time()-timeStart) < settle_time:
        currTime = float(time.time())

        set_temp_string = "TEMP, S" + str(temp1) + " H80 L-40"
        dmm.write(set_temp_string)
        
        tempReading = dmm.query("TEMP?")

        writer.writerow({'Time (s)': currTime, 'Temp (C)': tempReading})

        #console printouts so that the user has a visible timer
        print(time.time()-timeStart)
        print(tempReading)
        csvfile.flush()

        time.sleep(sample_time)
    
    
    while True:
        timeStart = time.time()
        #loops until time runs out
        while (time.time()-timeStart) < ramp_time:
        
            currTime = float(time.time())

            set_temp_string = "TEMP, S" + str(set_temp) + " H80 L-40"
            dmm.write(set_temp_string)

            tempReading = dmm.query("TEMP?")

            writer.writerow({'Time (s)': currTime, 'Temp (C)': tempReading})

            #console printouts so that the user has a visible timer
            print(time.time()-timeStart)
            print(tempReading)
            csvfile.flush()

            set_temp = set_temp + dt1

            time.sleep(sample_time)

        timeStart = time.time()
        while (time.time()-timeStart) < settle_time:
            currTime = float(time.time())

            set_temp_string = "TEMP, S" + str(temp2) + " H80 L-40"
            dmm.write(set_temp_string)
            
            tempReading = dmm.query("TEMP?")

            writer.writerow({'Time (s)': currTime, 'Temp (C)': tempReading})

            #console printouts so that the user has a visible timer
            print(time.time()-timeStart)
            print(tempReading)
            csvfile.flush()

            time.sleep(sample_time)

        timeStart = time.time()
        #loops until time runs out
        while (time.time()-timeStart) < ramp_time:
        
            currTime = float(time.time())

            set_temp_string = "TEMP, S" + str(set_temp) + " H80 L-40"

            dmm.write(set_temp_string)
            tempReading = dmm.query("TEMP?")

            writer.writerow({'Time (s)': currTime, 'Temp (C)': tempReading})

            #console printouts so that the user has a visible timer
            print(time.time()-timeStart)
            print(tempReading)
            csvfile.flush()

            set_temp = set_temp - dt1

            time.sleep(sample_time)

        timeStart = time.time()
        while (time.time()-timeStart) < settle_time:
            currTime = float(time.time())

            set_temp_string = "TEMP, S" + str(temp1) + " H80 L-40"
            dmm.write(set_temp_string)
            
            tempReading = dmm.query("TEMP?")

            writer.writerow({'Time (s)': currTime, 'Temp (C)': tempReading})

            #console printouts so that the user has a visible timer
            print(time.time()-timeStart)
            print(tempReading)
            csvfile.flush()

            time.sleep(sample_time)


