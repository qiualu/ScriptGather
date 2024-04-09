import cv2
import numpy as np


img1 = 'img/TDMESOut.0.jpg'
img2 = 'img/TDMovieOut.2.png'
img3 = 'img/TDMESOut.0.png'

# 读取原始图像
image = cv2.imread(img2)


# 灰度化处理
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 霍夫变换检测直线
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

# 输出检测到的直线
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 查找直线的交点作为角点
corners = []
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        rho1, theta1 = lines[i][0]
        rho2, theta2 = lines[j][0]
        A = np.array([
            [np.cos(theta1), np.sin(theta1)],
            [np.cos(theta2), np.sin(theta2)]
        ])
        b = np.array([[rho1], [rho2]])
        corner = np.round(np.linalg.solve(A, b))
        if corner[0] >= 0 and corner[0] <= image.shape[1] and corner[1] >= 0 and corner[1] <= image.shape[0]:
            corners.append(corner.ravel())

# 绘制角点
for corner in corners:
    x, y = corner
    cv2.circle(image, (int(x), int(y)), 5, (0, 255, 0), -1)
    print(f'Corner: ({x}, {y})')

# 显示图像
cv2.imshow('corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()