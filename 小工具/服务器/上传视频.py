import sys
import requests
import json

#
#
# filename=r'C:\Users\yl\Desktop\泼墨\ins.mp4'
# post_file_url = "https://api.lightfactorymedia.com/kinect/uploadvideo"
#
# files = {'video': open(filename, 'rb')}
# response = requests.post(post_file_url, files=files)
# jsonw = response.json()
# print(jsonw)



# 查看视频
# type=0是图片 1是视频
# https://api.lightfactorymedia.com/caisi/img?src=static/uploads/jizhi/Kinect_video001/ceshi.mp4&type=1



# abc/uploadimg


import sys
import requests
import json

filename=r"C:\Users\yl\Desktop\步进电机!!377796835.jpg"
post_file_url = "http://175.178.159.67:8855/abc/uploadimg"

files = {'image': open(filename, 'rb')}
response = requests.post(post_file_url, files=files)
jsonw = response.json()
print(jsonw)

#  返回 {'status': 10030, 'msg': 'ok!', 'src': 'static/uploads/mod/mod001/步进电机!!377796835.jpg', 'config': {'name': 'image', 'vali': {'size': 20971520, 'ext': 'png,jpg,jpeg'}, 'module': 'mod', 'dir': 'mod001'}}
# 查看 图片地址  http://175.178.159.67:8855/static/uploads/mod/mod001/步进电机!!377796835.jpg

