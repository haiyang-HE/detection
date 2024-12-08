# import os
# import xml.etree.ElementTree as ET
#
# # 定义需要修改的文件夹路径
# folder_path = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels\train_xml'  # 替换为你的文件夹路径
# # 定义要替换的旧类别和新类别
# old_class = 'fishing boat'  # 替换为要修改的类别名
# new_class = 'fishing-boat'  # 替换为你需要的新类别名
#
# # 遍历文件夹中的所有XML文件
# for filename in os.listdir(folder_path):
#     if filename.endswith('.xml'):
#         file_path = os.path.join(folder_path, filename)
#
#         # 解析XML文件
#         tree = ET.parse(file_path)
#         root = tree.getroot()
#
#         # 查找并替换类别
#         for obj in root.findall('object'):
#             name = obj.find('name')
#             if name is not None and name.text == old_class:
#                 name.text = new_class
#                 print(f'Modified {filename}: {old_class} to {new_class}')
#
#                 # 保存更改后的文件
#         tree.write(file_path)
#
# print('所有文件已更新。')

import os
import xml.etree.ElementTree as ET

# 定义需要检查的文件夹路径
folder_path = r'F:\红外数据集\红外海上船舶数据集\红外船舶数据库\dataset\labels\train_xml'  # 替换为你的文件夹路径

# 遍历文件夹中的所有XML文件
for filename in os.listdir(folder_path):
    if filename.endswith('.xml'):
        file_path = os.path.join(folder_path, filename)

        # 解析XML文件
        tree = ET.parse(file_path)
        root = tree.getroot()

        # 查找类别名
        has_none_type = False
        for obj in root.findall('object'):
            name = obj.find('name')
            if name is not None and name.text == 'NoneType':
                has_none_type = True
                break

                # 如果找到了类别为 'NoneType'，则删除该文件
        if has_none_type:
            os.remove(file_path)
            print(f'Deleted: {filename}')

print('处理完成。')