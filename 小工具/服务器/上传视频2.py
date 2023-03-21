import requests

# sp wx1664445987083870130 1
fp = r"C:\Users\yl\Desktop\星月湾\视频合成模版\输出压缩\求婚主题\wx1664445987083870130_640x360.mp4"

url = "https://www.xinyuewandasha.com/api/cus/uploadvideo"

# form-data参数要写成如下格式，注意有None


# form-data参数要写成如下格式，注意有None
data = {
    "uploadtoken": "NOIwnhh5689KJiwhPj",
    "out_trade_no": "wx1665200600247180350",
}

files = {
    'file': ('wx1664445987083870130_640x360.mp4', open(fp, 'rb'), 'video/mp4')
}

req = requests.post(url=url, data=data, files=files)

#
print('上传返回', req.json())