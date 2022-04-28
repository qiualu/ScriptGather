import qrcode


from MyQR import myqr
import os

daoshu  = []
for arg in sys.argv:
    # print(arg)
    if arg:
        imgname = arg
    # print(type(arg))
    daoshu.append(arg)

# print(" --------- ")
print(daoshu)

# img = qrcode.make('simpleqrcode')
# img.save(r'C:\Users\yl\Desktop\simpleqrcode.jpg')

# 可用字符：数字0到9，大小写英文字母，常用英文标点符号和空格。注意不能使用中文！
word = 'https://beeeeee.herokuapp.com'

# version, level, qr_name = myqr.run(
#     word,  # 必要参数是二维码的内容，是一个str，其他参数可选
#     version=10,  # int,1~40，边长
#     level='H',  # str,'L','M','Q','H'，就错等级
#     picture=None,  # 图片path，用于制作艺术二维码，建议选择正方形的照片
#     colorized=Fasle,  # 上色
#     contrast=1.0,  # 对比度
#     brightness=1.0,  # 亮度
#     save_name=None,  # 输出文件名。默认：输入图片文件名_qrcode.png
#     save_dir=os.getcwd()  # 输出文件存储目录
# )

# version, level, qr_name = myqr.run(
#     word,  # 必要参数是二维码的内容，是一个str，其他参数可选
#     version=10,  # int,1~40，边长
#     level='H',  # str,'L','M','Q','H'，就错等级
#     picture=None,  # 图片path，用于制作艺术二维码，建议选择正方形的照片
#     colorized=False,  # 上色
#     contrast=1.0,  # 对比度
#     brightness=1.0,  # 亮度
#     save_name=r"img.png",  # 输出文件名。默认：输入图片文件名_qrcode.png
#     save_dir=  r"C:\Users\yl\Desktop\img"   # os.getcwd()  # 输出文件存储目录
# )
version, level, qr_name = myqr.run(
    word,  # 必要参数是二维码的内容，是一个str，其他参数可选
    version=10,  # int,1~40，边长
    level='H',  # str,'L','M','Q','H'，就错等级
    picture=None,  # 图片path，用于制作艺术二维码，建议选择正方形的照片
    colorized=False,  # 上色
    contrast=1.0,  # 对比度
    brightness=1.0,  # 亮度
    save_name= daoshu[2],  # 输出文件名。默认：输入图片文件名_qrcode.png
    save_dir= daoshu[3]   # os.getcwd()  # 输出文件存储目录
)
print(version, level, qr_name)




