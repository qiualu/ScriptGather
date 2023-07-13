import socket
import threading
import ctypes
import time

# 定义键盘按键的虚拟键码
# 定义常量
VK_UP = 0x26
VK_DOWN = 0x28
VK_LEFT = 0x25
VK_RIGHT = 0x27
KEYEVENTF_KEYUP = 0x0002

# 定义结构体
# 定义结构体
# 定义结构体
class KeyboardInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]


class Input(ctypes.Structure):
    class _Input(ctypes.Union):
        _fields_ = [("ki", KeyboardInput)]

    _fields_ = [("type", ctypes.c_ulong), ("input", _Input)]


def press_key(vk_code):
    inputs = (Input * 2)()
    extra_info = ctypes.c_ulong(0)

    # 模拟按下键
    inputs[0].type = ctypes.c_ulong(1)
    inputs[0].input.ki = KeyboardInput(vk_code, 0, 0, 0, ctypes.pointer(extra_info))

    # 模拟释放键
    inputs[1].type = ctypes.c_ulong(1)
    inputs[1].input.ki = KeyboardInput(vk_code, 0, KEYEVENTF_KEYUP, 0, ctypes.pointer(extra_info))

    ctypes.windll.user32.SendInput(2, ctypes.pointer(inputs), ctypes.sizeof(Input))
class UDPReceiver:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((host, port))
        print(f"UDP 服务器已启动，在 {host}:{port} 上监听...")

    def receive_data(self):
        while True:
            data, addr = self.server_socket.recvfrom(1024)
            message = data.decode()
            print(f"接收到来自 {addr} 的消息：{message}")

            # 在此处添加自定义逻辑来处理接收到的数据
            # ... 回复
            return_message = f"Hello from {addr}"
            self.server_socket.sendto(bytes(return_message, encoding='utf-8'), addr)  # 发送回复信息

            ml = str(message[:1])
            print(ml,len(ml))

            if ml == "s":
                press_key(VK_UP)
            elif ml == "x":
                press_key(VK_DOWN)
            elif ml == "z":
                press_key(VK_LEFT)
            elif ml == "y":
                press_key(VK_RIGHT)
    def start(self):
            receive_thread = threading.Thread(target=self.receive_data)
            receive_thread.start()

def main():
    host = '0.0.0.0'  # 服务器主机地址
    port = 12345  # 服务器端口号

    receiver = UDPReceiver(host, port)
    receiver.start()

if __name__ == '__main__':
    main()