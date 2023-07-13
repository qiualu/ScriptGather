

# https://www.bilibili.com/video/BV19T411C7U8/?spm_id_from=333.788&vd_source=4bfde864e528fd92926834fbf73fe575
# 3 you-get使用方法
# 3.1 直接下载视频
#
# you-get+url（url为视频链接）
# 3.2 显示视频可供选择的清晰度、大小与格式等信息
#
# you-get -i+url（url为视频链接）
# 3.3 批量下载视频列表
#
# you-get  --playlist++url（url为视频链接）
# 3.4 指定下载视频的清晰度与格式，可以使用you-get -i查看
#
# you-get --format=dash-flv720+url（url为视频链接）
# 3.5 指定下载视频的保存目录，若不指定则保存在当前的工作目录
#
# you-get -o+文件目录+url（url为视频链接）
# 3.6 指定下载视频的文件名，若不指定则为默认视频名称
#
# you-get -O+文件名称+url（url为视频链接）
# 3.7 使用cookies，适用于需要使用会员下载的视频
#
# you-get --cookies=cookies路径+url（url为视频链接）
# 火狐浏览器的cookies文件路径
#
# C:\Users\users_name\AppData\Roaming\Mozilla\Firefox\Profiles\dln2mhmn.default\cookies.
#

import os
# path = input("请输入下载网址 : ")
# zl = "you-get" + path + "-o ./"
# os.system(zl)
print("下载完成")





