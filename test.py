from time import sleep
import serial
ser = serial.Serial('COM3', 9600, timeout=1) # Establish the connection on a specific port

sleep(3)

ser.write(b'f')
ser.write(b'g')

sleep(1)
print(ser.in_waiting)

while ser.in_waiting > 0:
    print(ser.read())
    sleep(1)