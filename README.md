# RigolDM3058ECurrentRecording

This script was created to stream data from a RIGOL DM3058E over USB and output it to a csv file.

## Prerequisites

- Windows 10
- [NI Visa Runtime](http://www.ni.com/download/ni-visa-run-time-engine-15.0/5379/en/)
- Python
- [Pyvisa module](https://pyvisa.readthedocs.io/en/stable/index.html)

## Other Commands

[Rigol Programming Guide](https://www.batronix.com/pdf/Rigol/ProgrammingGuide/DM3058_ProgrammingGuide_EN.pdf)

## How to use it

- Place the python file in a folder of choice. (It will produce a csv file in the folder it's in)

- Make sure the DMM is open and plugged in to your computer

- Make sure the program is working with your system

    - Open the Python file and make sure it works. (The terminal output should be counting down)

    - If it worked then it should have created a file called "datapoint.csv" (you may also here a click sound coming from the Rigol DMM)

- To change length of time in whcih the program will run, just modify this part of the code:

```python
#modify test time in seconds
testTime = 15*60
```

- The program will start recording data once it starts counting down

- The program outputs the amount of points it has collected so far, and the amount of time left until the program is finished

- the csv will contain two columns. The first column has the time in seconds and the second columns has the current in Amperes.
