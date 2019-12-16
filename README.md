# PyVisa Scripts

These scripts were created to stream data from various lab equipment over (GPI-B/Serial) and output it to a csv file.

## Prerequisites

Install these:
- Windows 10
- [NI Visa Runtime](http://www.ni.com/download/ni-visa-run-time-engine-15.0/5379/en/)
- Python3
- [Pyvisa module](https://pyvisa.readthedocs.io/en/stable/index.html)

## Other Commands

[Rigol Programming Guide](https://www.batronix.com/pdf/Rigol/ProgrammingGuide/DM3058_ProgrammingGuide_EN.pdf)

## How to use it

- Place the python file in a folder of choice. (It will produce a csv file in the folder it's in)

- Make sure the Lab equipment and plugged in to your computer

- Make sure the program is working with your system

    - Double click the Python file and make sure it works. (The terminal output should be counting down)

    - If it worked then it should have created a csv file (You may also hear clicking or LCD refreshing on you lab equipment)

- To change length of time in which the program will run, just modify this part of the code:

```python
#modify test time in seconds
testTime = 15*60
```

- The program will start recording data once it starts counting down
