
import configparser


config = configparser.ConfigParser()
config.read("调用浏览器配置文件55.ini",encoding="utf-8")

# liulanqi = config.get("socket","浏览器路径")
# url = int(config.get("socket","打开网页链接"))
#
#
# mlj = liulanqi + "  " + url
#
# import os
# os.system(mlj)

liulanqi = config.get("kkk", "fk")
print(liulanqi)