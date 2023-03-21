import time
from pynput.mouse import Listener, Controller

start_time = time.time()
run_time = 10  # 设置程序运行时间为10秒

def on_click(x, y, button, pressed):
    # 鼠标点击事件处理函数
    mouse = Controller()
    mouse.position = (x, y)  # 设置鼠标位置为当前位置
    mouse.press(button)  # 按下鼠标键
    mouse.release(button)  # 释放鼠标键
    return False  # 返回 False 表示拦截鼠标事件

# 监听鼠标点击事件
with Listener(on_click=on_click) as listener:
    while time.time() - start_time < run_time:
        pass  # 程序运行期间不断循环
    listener.stop()  # 定时结束监听器

# 恢复鼠标控制
mouse = Controller()
mouse.position = (0, 0)

