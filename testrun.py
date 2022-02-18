import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    while True:
        ser.write(b"on/n")
        time.sleep(1)
        ser.write(b"off/n")
        time.sleep(1)
