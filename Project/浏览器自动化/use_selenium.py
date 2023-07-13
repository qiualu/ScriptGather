from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # 添加这行 import
# 打开 Google 搜索页
# 创建 Chrome 浏览器对象
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:7860/")

# 找到输入框并输入内容 //*[@id="txt2img_prompt"]/label/textarea
data = "best quality, masterpiece,(looking at viewer),cute pose,1girl,solo,(silver hair:1.4),(double_bun:1.6),(light_smile),long legs,narrow waist,(slim),(white_skin),blush,shy,tight shirt,miniskirt, (short necktie),earrings,beautiful scenery,(flower field),pureerosface_v1, <lora:mix2_2:1>, <lora:EkiaRuRinh_v10:0.8:faceL>"
input_box = driver.find_element(By.ID, 'txt2img_prompt')

# 提交表单
input_box.submit()

