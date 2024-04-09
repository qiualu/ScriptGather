
data = "aa550028e14b2b51f828000000000000000000000000000000000000000000000000000000004c4f00004859a859cc59cc59000054570000c0540000585268510000000000000000000000000000f83298324c320432c8317031"

byte_data = bytes.fromhex(data)

print(byte_data)

value = int.from_bytes(byte_data[:2], byteorder='little')
print(value,hex(value))

index = 2
PH = hex(int.from_bytes(byte_data[:2], byteorder='little'))
CT = hex(int.from_bytes(byte_data[2:3], byteorder='little'))
LSN = int.from_bytes(byte_data[3:4], byteorder='little')

FSA = int.from_bytes(byte_data[4:6], byteorder='little')
LSA = int.from_bytes(byte_data[6:8], byteorder='little')
CS = int.from_bytes(byte_data[8:10], byteorder='little')

Si = int.from_bytes(byte_data[10:12], byteorder='little')

print(PH,CT,LSN,hex(FSA),hex(LSA),hex(CS),hex(Si))
print(" FSA, LSA ",FSA, LSA)
FSA_value = FSA >> 1
LSA_value = LSA >> 1
print("FSA_value ",FSA_value, LSA_value)
print(FSA_value/64, LSA_value/64)


# 起始角解算公式：𝐴𝑛𝑔𝑙𝑒𝐹𝑆𝐴 =𝑅𝑠ℎ𝑖𝑓𝑡𝑏𝑖𝑡(𝐹𝑆𝐴,1)/64
#
# 结束角解算公式：𝐴𝑛𝑔𝑙𝑒𝐿𝑆𝐴 =𝑅𝑠ℎ𝑖𝑓𝑡𝑏𝑖𝑡(𝐿𝑆𝐴,1)/64
# 𝑅𝑠ℎ𝑖𝑓𝑡𝑏𝑖𝑡(𝑑𝑎𝑡𝑎, 1)表示将数据 data 右移一位
# FSA = 0x6FE5，LSA = 0x79BD，带入上面公式， 得 :


import math


FSA = 0x6FE5
LSA = 0x79BD

# 计算起始角度
angleFSA = (FSA / 32768) * 360
print(angleFSA)  # 223.785400390625

# 计算结束角度
angleLSA = (LSA / 32768) * 360
print(angleLSA)  # 243.47412109375

FSA_value = FSA >> 1
LSA_value = LSA >> 1

print(FSA_value/64,LSA_value/64)  # 223.785400390625

FSA_Angle = FSA_value / 64  # 起始角度
LSA_Angle = LSA_value / 64  # 结束角度

diff_Angle = LSA_Angle - FSA_Angle
print(FSA_Angle,LSA_Angle,diff_Angle)
i = 0
# AngleI =

length = 0x28
diff_Angleii = diff_Angle / (length-1)
print("length : ", length,diff_Angleii,diff_Angle)
# for i in range(0x28):
    # jd = FSA_Angle + diff_Angleii * i
    # print(i,"  ",jd,"   ",diff_Angleii)

Distance1 = 1000
Distancelsn = 8000

Angle1 = FSA_Angle + diff_Angleii * 1  # 中间角度


AngCorrect1 = math.atan(21.8 * ( (155.3- Distance1) / (155.3 * Distance1) ))
print("AngCorrect1 : ",AngCorrect1)
import math

Distance1 = 1000.0

def AngCorrectDistance(Distance1):  # 偏差角度

    # 计算 AngCorrect1
    # 计算 AngCorrect1
    AngCorrect1 = math.atan(21.8 * (155.3 - Distance1) / (155.3 * Distance1)) # 弧度制的角度值
    AngCorrect1_deg = math.degrees(AngCorrect1) #  弧度制 转 角度值
    return AngCorrect1_deg

AngCorrect1 = AngCorrectDistance(1000)
AngCorrectLSN = AngCorrectDistance(8000)

print(AngCorrect1)  # 输出结果为 -6.7622
print(AngCorrectLSN)  # 输出结果为

AngleFSA = FSA_Angle + AngCorrect1
AngleLSA = LSA_Angle + AngCorrectLSN

print(FSA_Angle, AngleFSA)  # 输出结果为 -6.7622
print(LSA_Angle, AngleLSA)  # 输出结果为



# 校验码验证#
print(len(byte_data),byte_data)
ll = len(byte_data)/2
XOR1 = 0
for i in range(int(ll)):

    data = int.from_bytes(byte_data[i*2:i*2+2], byteorder='big')
    if i == 4:
        continue
    XOR1 ^= data
    print(i, "  ", data , XOR1)

i = 4
data = int.from_bytes(byte_data[i*2:i*2+2], byteorder='big')

print( 'sffsf : ' , data ,XOR1 )

