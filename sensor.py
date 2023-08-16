
import serial
from time import sleep
from struct import unpack

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # open serial port

while True:
    try:
       #coding ambil data sensor
      dataRaw = ser.read(4) #4 ===> 2 x 2 of short data types (2 Bytes)
      data1, data2 = unpack("hh", dataRaw) #hh for short ===> int (in arduino [atmel microprocessors]) = short in python, they have same size, 2 Bytes
      print(f"co2: {data1} | tvo2: {data2}")
    except:
       print("tidak ada data sensor")


    sleep(0.1)

