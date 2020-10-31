import os
from PIL import Image

def clean(w=7,h=11):

    path = os.path.join(os.getcwd(),"datanum")
    save_path = os.path.join(os.getcwd(),"datanum2")

    if not os.path.exists(save_path):
        os.mkdir(save_path)
    file_names = os.listdir(path) # 获取路径下所有文件的名字
    for file_name in file_names:

        原图片路径=path+"/"+str(file_name) # 原图片路径
        新图片保存路径=save_path+"/"+str(file_name)
        # if not os.path.exists(save_ds):
        #     os.mkdir(save_ds)
        # lower_directory_names=os.listdir(原图片路径)
        try:
            pic = Image.open(原图片路径)
            pic = pic.resize((w, h))
            pic.save(新图片保存路径)
        except:
            print("fail")
        # for lower_directory_name in lower_directory_names:
        #     photo_path= 原图片路径 +"/"+str(lower_directory_name)
        #    # print(photo_path)
        #     save_name = save_path + "/" +str(file_name) +"/"+str(lower_directory_name)
        #     #print(save_name)
        #
        #
        #     try:
        #         pic = Image.open(photo_path)
        #         pic = pic.resize((w, h))
        #         pic.save(save_name)
        #         print("成功")
        #     except:
        #         print("fail")

def clean2(w=7,h=11):
    path = os.path.join(os.getcwd(),"datanum10")
    save_path = os.path.join(os.getcwd(),"datanum3")

    if not os.path.exists(save_path):
        os.mkdir(save_path)
    file_names = os.listdir(path) # 获取路径下所有文件的名字
    for file_name in file_names:

        原图片路径文件夹=path+"/"+str(file_name) # 原图片路径
        新保存路径文件夹=save_path+"/"+str(file_name)
        if not os.path.exists(新保存路径文件夹):
            os.mkdir(新保存路径文件夹)
        图片名字=os.listdir(原图片路径文件夹)
        index = 0
        for lower_directory_name in 图片名字:
            photo_path= 原图片路径文件夹 +"/"+str(lower_directory_name)
            # print(photo_path)
            save_name = save_path + "/" +str(file_name) +"/"+str(index) + ".png"
            #print(save_name)
            index += 1
            if index > 400:
                continue

            try:
                pic = Image.open(photo_path)
                pic = pic.resize((w, h))
                pic.save(save_name)
                print("成功")
            except:
                print("fail")

if __name__ == '__main__':
    clean2()