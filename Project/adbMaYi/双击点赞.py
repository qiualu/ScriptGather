
import os
import time
import subprocess

import asyncio
import os
import subprocess

# os.popen("adb shell input tap 1300 550")
# time.sleep(0.3)
# os.popen("adb shell input tap 1300 550")

import os

# 定义点击屏幕的坐标
x = 250
y = 1300

def whilecmd():

    # 构造ADB命令
    # adb_command = f"adb shell input tap {x} {y}"
    adb_command = f"adb shell input tap {x} {y}  {x} {y}"

    addc = 20

    while addc:
        addc -= 1
        print(addc)
        time.sleep(0.01)
        # 在Python中执行ADB命令
        os.system(adb_command)
        os.system(adb_command)




async def adb_command(x, y):
    adb_command = f"adb shell input tap {x} {y}"
    os.system(adb_command)


async def run_commands():
    tasks = []
    for i in range(1000):
        task = asyncio.create_task(adb_command(x, y))
        tasks.append(task)
    await asyncio.gather(*tasks)

def yibu():
    # 定义要执行的命令列表，每个命令包含x和y坐标
    # commands = [((500, 500), (1000, 1000)), ((2000, 2000), (3000, 3000))]

    # 运行命令
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_commands())

whilecmd()
# yibu()

