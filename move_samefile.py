# import os
# import shutil
#
# # 源文件夹和目标文件夹
# source_folder = r'D:\data\data_guo\zdata\savedata617\imgs'
# target_folder = 'D:\data\data_guo\zdata\savedata617\MYCells-data-modfied'
# new_folder = r'D:\data\data_guo\zdata\savedata617\val'
#
# # 用来存储源文件夹中已记录的文件名
# recorded_files = set()
#
# # 遍历源文件夹中的文件，记录文件名
# for root, dirs, files in os.walk(source_folder):
#     for file in files:
#         recorded_files.add(file)
#
# # 在目标文件夹中查找已记录的文件名，并将其剪切到新的文件夹
# for root, dirs, files in os.walk(target_folder):
#     for file in files:
#         if file in recorded_files:
#             source_file = os.path.join(target_folder, file)
#             target_file = os.path.join(new_folder, file)
#
#             # 确保新文件夹存在
#             if not os.path.exists(new_folder):
#                 os.makedirs(new_folder)
#
#             # 剪切文件到新文件夹
#             # shutil.move(source_file, target_file)
#             # 复制文件到新文件夹
#             shutil.copy(source_file, target_file)
#
# # print('已将文件剪切到名为 "val" 的文件夹中！')
# print('已将文件复制到名为 "val" 的文件夹中！')
import os
import shutil

# 文件夹路径
txt_folder = r'F:\红外数据集\红外航拍人车检测数据集\红外航拍数据集\txt'  # TXT 文件夹路径
jpg_folder = r'F:\红外数据集\红外航拍人车检测数据集\红外航拍数据集\images'  # JPG 文件夹路径
new_folder = r'D:\00000\RTDETR-main-ul\hongwai-data\renche\images'  # 新文件夹路径

# 确保新文件夹存在
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# 获取 TXT 文件夹中的所有文件名（不带扩展名）
txt_files = {os.path.splitext(file)[0] for file in os.listdir(txt_folder) if file.endswith('.txt')}

# 遍历 JPG 文件夹中的文件
for file in os.listdir(jpg_folder):
    if file.endswith('.jpg'):
        # 获取文件名（不带扩展名）
        file_name = os.path.splitext(file)[0]
        # 如果文件名在 TXT 文件夹中，则复制该 JPG 文件到新文件夹
        if file_name in txt_files:
            source_file = os.path.join(jpg_folder, file)
            target_file = os.path.join(new_folder, file)
            shutil.copy(source_file, target_file)

print('已将与 TXT 文件同名的 JPG 文件复制到新文件夹中！')