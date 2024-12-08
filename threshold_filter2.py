# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt

path2img = r"D:\00000\cellcount_ultis\atest\YOLODataset\images"         # jpg图片和对应的生成结果的txt标注文件，放在一起
path2txt = r"D:\00000\cellcount_ultis\atest\YOLODataset\labels"         # 裁剪出来的小图保存的根目录

img_total = []
for file in os.listdir(path2img):
    if file.endswith(".png" or ".jpg"):
        img_total.append(file)

def change_first_number_label(txt_file_path,line_number,new_number):
    # 打开txt文件并读取内容
    with open(txt_file_path, 'r') as file:
        lines = file.readlines()

    # 在指定的行数中找到第一个数字并替换为新数字
    if line_number < len(lines):
        line_to_modify = lines[line_number].strip()
        numbers = line_to_modify.split()
        if numbers and (numbers[0]!='1' and numbers[0]!='3'):
            numbers[0] = str(new_number)
            lines[line_number] = ' '.join(numbers) + '\n'
        else:
            lines[line_number] = ' '.join(numbers) + '\n'
        # 将修改后的内容写回txt文件
        with open(txt_file_path, 'w') as file:
            file.writelines(lines)
            # print(f"Successfully modified the first number in line {line_number} to {new_number}.")
    else:
        print(f"Error: Line number {line_number} is out of range.")

def count_one_img(img_):
    filename_img = img_  # 图片的后缀名
    path1 = os.path.join(path2img, filename_img)
    img = cv2.imread(path1)
    h, w, channels = img.shape
    # img = cv2.resize(img,(w,h),interpolation = cv2.INTER_CUBIC)        # resize 图像大小，否则roi区域可能会报错
    filename_txt = os.path.splitext(img_)[0] + ".txt"
    txt_path = os.path.join(path2txt, filename_txt)
    # 打开txt文件
    with open(txt_path, "r") as file:
        # 创建一个空列表，用于保存每一行（不包含第一个元素）作为一个整体
        lines_without_first = []
        # 逐行读取文件内容
        for line in file:
            # 将每一行按空格分割成多个单词，并排除第一个单词
            words = line.strip().split()[1:]
            # 将每个单词转换为浮点数并乘以1024，然后添加到列表中
            modified_words = [str(float(word) * h) if t % 2 == 0 else str(float(word) * w) for t, word in
                              enumerate(words)]
            lines_without_first.append(" ".join(modified_words))
    # 将列表中的每个元素按照每两个元素合成一个子列表
    for i in range(len(lines_without_first)):
        line_values = lines_without_first[i].split()
        combined_values = []
        for j in range(0, len(line_values), 2):
            combined_values.append([float(line_values[j]), float(line_values[j + 1])])
        lines_without_first[i] = combined_values
    return lines_without_first


thshold = 0.30

# img_ = img_total[29]
# img_ ="871a0819313c4c5ddcb5a9a1ea75ed58.png"
for img_ in img_total:
    red_all = []
    lines_without_first = count_one_img(img_)
    # 加载原始图像
    original_image = cv2.imread(os.path.join(path2img, img_))
    # 创建保存 ROI 区域的文件夹
    output_folder = 'roi_images0'
    os.makedirs(output_folder, exist_ok=True)
    # 遍历每个轮廓
    for i, contour in enumerate(lines_without_first):
        contour_array = np.array(contour, dtype=np.int32)
        mask = np.zeros((original_image.shape[0], original_image.shape[1], 3), dtype=np.uint8)
        cv2.fillPoly(mask, [contour_array], color=(255, 255, 255))
        roi = cv2.bitwise_and(original_image, mask)
        # 提取 ROI 区域的红色通道像素
        red_channel_roi = roi[:, :, 2]  # 红色通道索引为2
        # 计算 ROI 区域红色通道像素的平均值
        red_mean = np.mean(red_channel_roi[red_channel_roi > 0])  # 只计算 ROI 区域中有像素的区域
        red_all.append(red_mean)
        # print(f'ROI {i} : {red_mean}')
        output_path = os.path.join(output_folder, f'roi_{i}.jpg')
        cv2.imwrite(output_path, roi)
        # print(f'ROI {i} saved to: {output_path}')
    print(str(img_),"*"*50 ,len(red_all))
    # 计算红色通道的平均值
    max_value = max(red_all)
    average_value = sum(red_all) / len(red_all)


    roi_images0 = output_folder
    dir_list = os.listdir(roi_images0)
    # result_image = np.zeros((original_image.shape[0], original_image.shape[1], 3), dtype=np.uint8)
    # for i in range(len(dir_list)):
    #     pathimg1 = os.path.join(roi_images0, dir_list[i])
    #     image1 = cv2.imread(pathimg1)
    #     # image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    #     # intensity = cv2.mean(image_gray)[0]
    #     # print("Average intensity:", intensity)
    #     result_image = np.clip(image1.astype(int) + result_image.astype(int), 0, 255).astype(np.uint8)
    # # 输出合成后的图像
    # cv2.imwrite('result_image.jpg', result_image)

    directory_to_delete = roi_images0
    # 使用 shutil.rmtree() 函数删除目录及其所有内容
    shutil.rmtree(directory_to_delete)
    print(f'目录 {directory_to_delete} 已成功删除')

    # 创建文件阈值筛选
    roi_images0 = output_folder
    os.makedirs(output_folder, exist_ok=True)

    #做阈值筛选后的图
    for i, contour in enumerate(lines_without_first):
        contour_array = np.array(contour, dtype=np.int32)
        mask = np.zeros((original_image.shape[0], original_image.shape[1], 3), dtype=np.uint8)
        cv2.fillPoly(mask, [contour_array], color=(255, 255, 255))
        roi = cv2.bitwise_and(original_image, mask)
        # 提取 ROI 区域的红色通道像素
        red_channel_roi = roi[:, :, 2]  # 红色通道索引为2
        # 计算 ROI 区域红色通道像素的平均值
        red_mean = np.mean(red_channel_roi[red_channel_roi > 0])  # 只计算 ROI 区域中有像素的区域
        red_all.append(red_mean)
        # print(f'ROI {i} : {red_mean}')
        output_path = os.path.join(output_folder, f'roi_{i}.jpg')
        if red_mean > (max_value * thshold):
            cv2.imwrite(output_path, roi)
            change_first_number_label(os.path.join(path2txt,os.path.splitext(img_)[0] + ".txt"), i, 0)    #修改txt标签
            # print(f'ROI {i} saved to: {output_path}')
        else:
            change_first_number_label(os.path.join(path2txt,os.path.splitext(img_)[0] + ".txt"), i, 2)
    print('All ROIs saved successfully.')
    print("*"*10 ,len(os.listdir(output_folder)))


    # #合成一张图像
    # dir_list = os.listdir(roi_images0)
    # result_image = np.zeros((original_image.shape[0], original_image.shape[1], 3), dtype=np.uint8)
    # for i in range(len(dir_list)):
    #     pathimg1 = os.path.join(roi_images0, dir_list[i])
    #     image1 = cv2.imread(pathimg1)
    #     # image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    #     # intensity = cv2.mean(image_gray)[0]
    #     # print("Average intensity:", intensity)
    #     result_image = np.clip(image1.astype(int) + result_image.astype(int), 0, 255).astype(np.uint8)
    # # 输出合成后的图像
    # cv2.imwrite('result_image_filt.jpg', result_image)


    # 要删除的目录路径
    directory_to_delete = roi_images0
    # 使用 shutil.rmtree() 函数删除目录及其所有内容
    shutil.rmtree(directory_to_delete)
    print(f'目录 {directory_to_delete} 已成功删除')