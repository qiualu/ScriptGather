import math
print(" 8位无符号正弦波(0-255)的PROGMEM (flash mem)表。")
for x in range(256):
    print("{:3},".format(int((math.sin(x/128.0*math.pi)+1.0)*127.5+0.5)),end=""),
    if x&15 == 15: print("hello")

print(" ------------ ")
print("但用于8位伽马校正表。")
gamma=2.6
for x in range(256):
    print("{:3},".format(int(math.pow((x)/255.0,gamma)*255.0+0.5)),end=""),
    if x&15 == 15: print("hello")
