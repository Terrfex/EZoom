#this script is to ensure the servos are working and moving correctly
import serial
port = serial.Serial('COM7',9600)
while 1:
    tt = input("X: ")
    ll = input("Y: ")
    fnlstr = "X"+str(tt)+"Y"+str(ll)
    port.write(fnlstr.encode())
