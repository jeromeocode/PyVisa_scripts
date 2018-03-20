# RigolDM3058ECurrentRecording
This script was created to stream data from a RIGOL DM3058E over USB and output it to a csv file.

# Prerequisites
- Windows 10
- [NI Visa Runtime](http://www.ni.com/download/ni-visa-run-time-engine-15.0/5379/en/)
- Python
- [Pyvisa module](https://pyvisa.readthedocs.io/en/stable/index.html)

# Other Commands
https://www.batronix.com/pdf/Rigol/ProgrammingGuide/DM3058_ProgrammingGuide_EN.pdf

# Quality Control Procedure
## What you need
- DMM with a usb cable plugged into computer
- LED to DMM adapter
- SPR
- LED
- Prerequisite downloads
- Arduino

## Steps
1. Turn on DMM and plug USB to Computer (same with the SPR)
2. Copy the python file into a folder you want the data to be in
3. Complete the circuit in which the DMM, LED, and SPR is in series (using the LED to DMM adapter)
4. Turn LED on using arduino (connect to SPR's COM# and type "TLED ON" into serial monitor while at 115200 baud)
5. Open the python file and let the time run out
6. Once done, the command window will close and a datapoint.csv file will have the current data

# Common problems
The console window immediately closes after starting the program
- unplug and replug the usb to computer
- you have a datapoint.csv file open (make sure it is closed)