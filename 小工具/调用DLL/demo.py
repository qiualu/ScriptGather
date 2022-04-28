


import ctypes,ctypes.util

def find_dll(dll_name):
    return ctypes.util.find_library(dll_name) # 查找DLl

def load_dll(dll_path):
    try:
        vc_dll = ctypes.CDLL(dll_path) # 加载动态库
        print("第一步,加载动态库成功")

        vc_func = vc_dll.convert_array # 获取动态库的函数

        # C++ <-> ctypes <-> python 数据类型的适配
        vc_func.argtypes = [ctypes.POINTER(ctypes.c_int),ctypes.c_int] # 函数输入值
        vc_func.restype = ctypes.c_int # 函数返回值

        my_list = [3,1,6,8,5]
        array_len = len(my_list)

        # 把列表转换成C++动态库函数所需要的参数数组 ,my_list 不是C++的数组
        my_array = (ctypes.c_int * array_len)(*my_list)

        ret = vc_func(my_array,array_len) # 调用动态库的函数

        print("函数返回值:",ret)

    except OSError as e:
        print(e,"加载dll失败") # // [WinError 193] %1 不是有效的 Win32 应用程序。 加载dll失败 python 是 64 位的  DLL是 32位的


if __name__ == '__main__':
    # dll_path = find_dll("MouseHookDll.dll")
    dll_path = find_dll("DemoDll.dll")
    if dll_path:
        load_dll(dll_path)





