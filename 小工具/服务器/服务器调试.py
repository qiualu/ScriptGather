
import requests,os


def upload_image(file_path):
    url = "https://api.lightfactorymedia.com/web_api/shenlan2024/uploadimgportrait"
    # files = {'image': open(file_path, 'rb')}
    files = {'file': ('image.jpg', open(file_path, 'rb'), 'image/jpeg')}  # 将'image.jpg'替换为你要上传的图片路径
    response = requests.post(url, files=files)


    # 直接上传
    url = "https://www.xinyuewandasha.com/api/cus/uploadvideo"
    # url = mod.WEB.hosturl + "/cus/uploadvideo"
    # data = {
    #     "uploadtoken": mod.WEB.uploadtoken,
    #     "out_trade_no": out_trade_no
    # }

    with open(file_path, 'rb') as f:
        files = {
            'image': (file_path, f, 'image/jpeg')
        }
        # 禁用SSL证书验证
        response = requests.request(url, files=files, verify=False)
        print("上传图片 -> ", response.json())

def UploadVideoTest(file,urls):
    """ 上传视频接 """
    # form-data参数要写成如下格式，注意有None
    data = {
        # "token": HttpConfig.TOKEN,
        # "out_trade_no":  out_trade_no,
    }
    filename = os.path.basename(file)
    files = {
        'image': (filename, open(file, 'rb'), 'image/jpeg') #  file
    }
    req = requests.post(url=urls, data=data, files=files)
    body = req.json()
    print(type(req),body)

urls = "https://api.lightfactorymedia.com/web_api/shenlan2024/uploadimgportrait"
file = r"C:\Users\yl\Desktop\image\高启强2.jpg"
UploadVideoTest(file,urls)