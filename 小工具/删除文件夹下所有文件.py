

import os
import shutil

def delete_contents(path):
    print("path: ",path)
    for root, dirs, files in os.walk(path, topdown=False):
        print("path: ", root, dirs)
        for name in files:
            file_path = os.path.join(root, name)
            os.remove(file_path)
            print("文件",file_path)
        for name in dirs:
            dir_path = os.path.join(root, name)
            shutil.rmtree(dir_path)
            print("文件夹",dir_path)

path = r"E:\ProgramFiles\ComfyUI_windows_portable"

if os.path.exists(path):
    delete_contents(path)
    print("目录已清空！")
else:
    print("路径不存在，请重新输入有效路径。")
