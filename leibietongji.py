import os
import xml.etree.ElementTree as ET
from collections import defaultdict

# 定义源文件夹
source_folder = r'C:\Users\Administrator\Desktop\IPVD红外车辆行人检测\dataset\红外航拍人车检测数据集\红外航拍数据集\dataset'

# 初始化类别计数器
label_counts = defaultdict(int)

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.json'):
        xml_path = os.path.join(source_folder, filename)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 检查XML文件中所有的目标标签
        for obj in root.findall('object'):
            name = obj.find('name').text
            label_counts[name] += 1

# 输出统计结果
print("Label counts:")
for label, count in label_counts.items():
    print(f"{label}: {count}")

print("Processing completed.")
