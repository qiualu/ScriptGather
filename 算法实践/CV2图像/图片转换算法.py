import cv2
import numpy as np
print("Hello 132")

import cv2

img1 = 'img/TDMESOut.0.jpg'
img2 = 'img/TDMESOut.0.png'


def parse_rectangle_rotation(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 灰度化图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 边缘检测
    edges = cv2.Canny(gray, 50, 150)

    # 执行霍夫变换来检测直线
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

    # 提取最长的直线
    longest_line = None
    longest_length = 0

    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if length > longest_length:
                longest_length = length
                longest_line = ((x1, y1), (x2, y2))

    # 计算旋转角度
    dx = longest_line[1][0] - longest_line[0][0]
    dy = longest_line[1][1] - longest_line[0][1]
    angle = np.arctan2(dy, dx) * 180 / np.pi

    # 检测翻转
    flip_horizontal = False
    flip_vertical = False

    if angle < -45:
        angle += 90
        flip_horizontal = True
    elif angle > 45:
        angle -= 90
        flip_horizontal = True
    elif angle < 0:
        flip_vertical = True

    return angle, flip_horizontal, flip_vertical



def reverse_texture_transformation(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 提取红色和绿色通道数据
    r_channel = image[:,:,2]
    g_channel = image[:,:,1]

    # 反推位移量
    tx = int(np.mean(r_channel) - image.shape[1] / 2)
    ty = int(np.mean(g_channel) - image.shape[0] / 2)

    # 反推缩放比例
    scale_x = np.mean(r_channel) / image.shape[1]
    scale_y = np.mean(g_channel) / image.shape[0]

    # 反推旋转角度
    angle = np.arctan2(np.mean(g_channel) - image.shape[0] / 2, np.mean(r_channel) - image.shape[1] / 2) * 180 / np.pi

    # 反推水平翻转和垂直翻转
    flip_horizontal = True if np.mean(r_channel) > image.shape[1] / 2 else False
    flip_vertical = True if np.mean(g_channel) > image.shape[0] / 2 else False

    # 返回反推结果
    return {'tx': tx, 'ty': ty, 'scale_x': scale_x, 'scale_y': scale_y, 'angle': angle, 'flip_horizontal': flip_horizontal, 'flip_vertical': flip_vertical}

data = reverse_texture_transformation(img2)

print(data)

"""
有一张图片用下面代码生成,命名为1.png
out vec4 fragColor;
void main()
{
	//vec4 color = texture(sTD2DInputs[0], vUV.st);
	vec4 color = vec4(vUV.st,0,1.0);
	fragColor = TDOutputSwizzle(color);
}
2.png 由 1.png 位移,缩放,旋转,反转


现在需要一个函数,输入2.png, 根据图片里 rg 通道的数据 反推出 1.png 变 2.png 的 位移,缩放,旋转,反转

代码用python 来写


uniform  float tx;// x轴方向移动
uniform  float ty;// y轴方向移动
uniform  float scale; //  整体缩放 
uniform  float anglex; // 旋转
uniform  float angley; // 反转


out vec4 fragColor;
void main()
{
	vec2 uv = vUV.st;
	
	...//  补充代码   计算 移动 缩放 旋转 反转 
	
	vec4 color = texture(sTD2DInputs[0], uv);
	fragColor = TDOutputSwizzle(color);
}

要在GLSL着色器中旋转图片，可以使用以下代码：

glsl
uniform float angle; // 旋转角度（以度为单位）

void main()
{
    vec2 uv = vUV.st;

   
    // 旋转 
    


    vec4 color = texture(sTD2DInputs[0], uv);
    fragColor = TDOutputSwizzle(color);
}


"""

angle, flip_horizontal, flip_vertical = parse_rectangle_rotation(img1)
print(" ----------------------- ")
print(angle, flip_horizontal, flip_vertical)











