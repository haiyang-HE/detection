import cv2
import numpy as  np
import glob
import json


import os

file_pathname = "./data"

for file_name in os.listdir(file_pathname):
    print(file_name)
    img = cv2.imread(file_pathname + '/' + str(file_name))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将图片变为灰度图片
    kernel = np.ones((2, 2), np.uint8)  # 进行腐蚀膨胀操作
    erosion = cv2.erode(gray, kernel, iterations=5)  # 膨胀
    dilation = cv2.dilate(erosion, kernel, iterations=5)  # 腐蚀
    ret, thresh = cv2.threshold(dilation, 5, 255, cv2.THRESH_BINARY)  # 阈值处理 二值法
    thresh1 = cv2.GaussianBlur(thresh, (3, 3), 0)  # 高斯滤波
    # cv2.imshow("ret", thresh1)
    # cv2.waitKey()
    contours, hirearchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE, offset=(-5, -5))  # 找出连通域
    #print(hirearchy)
    print(contours[0])
    # 对连通域面积进行比较
    area = []  # 建立空数组，放连通域面积
    contours1 = []  # 建立空数组，放减去最小面积的数
    contours2 = []
    for i in contours:
        if cv2.contourArea(i) > 50:  # 计算面积 去除面积小的 连通域
            contours1.append(i)
            area.append(cv2.contourArea(i))
    for i in contours1:
        if cv2.contourArea(i) < 1000:  # 计算面积 去除面积小的 连通域
            contours2.append(i)
            area.append(cv2.contourArea(i))

    # print(area[0])
    real_area = [i * 0.9 for i in area]
    # print(real_area[0])
    # print(contours2)  # 计算连通域个数
    draw = cv2.drawContours(img, contours2, -1, (0, 255, 0),
                            1)  # 描绘连通域 它的第一个参数是原始图像，第二个参数是轮廓，一个Python 列表。第三个参数是轮廓的索引（在绘制独立轮廓是很有用，当设置为-1 时绘制所有轮廓）。接下来的参数是轮廓的颜色和厚度等。
    # 求连通域重心 以及 在重心坐标点描绘数字
    # for i, j in zip(contours2, range(len(contours2))):
    #     M = cv2.moments(i)
    #     j = j + 1
    #     cX = int(M["m10"] / M["m00"])
    #     cY = int(M["m01"] / M["m00"])
    #     draw1 = cv2.putText(draw, str(j), (cX, cY), 1, 1, (0, 0, 255), 2)  # 在中心坐标点上描绘数字

    # 展示图片
    cv2.imshow("draw", draw)
    cv2.waitKey()
    print("Done")
    cv2.imwrite("./count"+ "/"+ os.path.splitext(file_name)[0] + '.png', draw)


    json_save = dict()
    json_save["version"] = "5.4.1"
    json_save["flags"] = {}
    shapes = []
    # np.savetxt("./count" + "/" + os.path.splitext(file_name)[0] + '.txt', area, fmt="%.2f", delimiter=" ")
    for i,count in enumerate(contours2):
        shape = dict()
        shape["label"] = "Neg-EPcell"
        points=[]
        arr = np.squeeze(count, axis=1)
        for t,point in enumerate(arr):
            if t%2==0:              #减少轮廓点的数量
                point = point.tolist()
                points.append(point)
        shape["points"] = points
        shapes.append(shape)
        shape["group_id"] = None
        shape["description"] = ""
        shape["shape_type"] = "polygon"
        shape["flags"] = {}
        shape["mask"] = None
    json_save["shapes"]=shapes
    json_save["imagePath"] = "{}.jpg".format(os.path.splitext(file_name)[0])
    json_save["imageData"] = None
    json_save["imageHeight"] = 1024
    json_save["imageWidth"] = 1024
    # 将数据保存为JSON文件
    file_path = "{}.json".format(os.path.splitext(file_name)[0])
    with open(file_path, "w") as file:
        json.dump(json_save, file, indent=4)
    print(f"数据已保存为JSON文件: {file_path}")
    # np.savetxt("./count" + "/" + os.path.splitext(file_name)[0] + '.txt', contours2, fmt="%.2f", delimiter=" ")

