import serial
import time

ser = serial.Serial()

def initSerial():
    global ser
    ser.baudrate = 115200
    #ser.port = '/dev/ttyUSB0'  ///for Linux
    ser.port = 'COM9'
    #ser.timeout =0
    ser.stopbits = serial.STOPBITS_ONE
    ser.bytesize = 8
    ser.parity = serial.PARITY_NONE
    ser.rtscts = 0
          
    

def main():
    initSerial()
    global ser
    ser.open()                          #open serial port
    global mHex
    while True:
        mHex = ser.read()               #read from serial
        #mHex = mHex.rstrip()            #strip return carriage and garbage
        mHex = mHex.decode("utf-8", "ignore")     #byte to utf-8 conversion
        if len(mHex)!= 0:
                print(mHex, end = '', flush = True)
                #time.sleep(0.1)             #match with arduino/serial write delay/write cycle clock



if __name__ == "__main__":
    main()
