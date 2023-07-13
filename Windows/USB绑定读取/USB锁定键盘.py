import usb.core
import usb.util

# 定义 USB 设备的 Vendor ID 和 Product ID
VENDOR_ID = 0x093A  # 示例：Microsoft Corp.
PRODUCT_ID = 0x2510  # 示例：Microsoft Basic Optical Mouse v2.0 093A&PID_2510

# 找到并打开指定的 USB 设备
device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
if device is None:
    raise ValueError("USB 设备未找到。")

try:
    # 配置设备
    device.set_configuration()

    # 找到鼠标接口和端点
    interface = device[0][(0, 0)]
    endpoint = interface[0]

    # 循环读取鼠标数据
    while True:
        try:
            data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
            # 解析鼠标数据
            # 例如，data[0] 表示按钮状态，data[1] 表示 X 方向移动的相对值，data[2] 表示 Y 方向移动的相对值
            print(f"鼠标数据：{data}")
        except usb.core.USBError as e:
            if e.args[0] == 'Operation timed out':
                continue

except KeyboardInterrupt:
    pass

finally:
    # 释放设备
    usb.util.release_interface(device, interface)
    usb.util.dispose_resources(device)