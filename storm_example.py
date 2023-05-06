import serial
import time
import struct

X25_INIT_CRC = 0xffff
def crc_accumulate(data, crcAccum):
        tmp=data ^ (crcAccum & 0xff)
        tmp^= (tmp<<4)
        return (crcAccum>>8) ^ (tmp<<8) ^ (tmp <<3) ^ (tmp>>4)

def crc_calculate(buf):
        crcTmp = X25_INIT_CRC
        for i in range(len(buf)):
                crcTmp = crc_accumulate(buf[i], crcTmp)
        return(crcTmp)

def send_message(command, buf):
    out = bytearray()
    out += bytearray([0xFA])
    out += bytearray([len(buf)])
    out += bytearray([command])
    out += buf
    crc = crc_calculate(out[1:])
    out += bytearray([crc & 0xFF, (crc >> 8) & 0xFF])
    ser.write(out)
    ser.read(1)
    length = ser.read(1)[0]
    ser.read(1)
    res = ser.read(length)
    ser.read(2)
    print(f"command:", " ".join(hex(b) for b in out))
    print(f"response:", " ".join(hex(b) for b in res))

ser = serial.Serial("/dev/ttyACM0")


# http://www.olliw.eu/storm32bgc-wiki/Serial_Communication

send_message(13, bytearray([3])) # set it to pan on all axes (Making it follow the base board)
# send_message(13, bytearray([2])) # set it to hold on all axes (making it independent of the baseboard)
send_message(1, bytearray()) # get version
send_message(2, bytearray()) # get version string
send_message(18, struct.pack("<HHH", 700, 0, 700)) # set pitch roll yaw
time.sleep(4)
send_message(18, struct.pack("<HHH", 2300, 0, 2300))
time.sleep(6)
send_message(18, struct.pack("<HHH", 0, 0, 0))
