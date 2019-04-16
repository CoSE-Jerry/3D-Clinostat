#RPi Pinouts

#I2C Pins 
#GPIO2 -> SDA
#GPIO3 -> SCL

#Import the Library Requreid 
import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
#Slave Address 1
address = 0x08
i2c_cmd = 0x7E

#Slave Address 2
#address_2 = 0x05

def writeBlock(bytesToSend):
    bus.write_i2c_block_data(address, i2c_cmd, bytesToSend)
    #bus.write_byte(address, value)
    #bus.write_byte(address_2, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def ConvertStringToBytes(src):
    converted = []
    for b in src:
        converted.append(ord(b))
    return converted
    
while True:
	#Receives the data from the User
    data = input("Enter the data to be sent : ")
    tosend = ConvertStringToBytes(data)
    writeBlock(tosend)
#End of the Script

