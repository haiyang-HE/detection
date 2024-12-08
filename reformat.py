import json

# 读取JSON文件
with open(r'D:\00000\C-seg\cells-count\mmdetection\data\coco\annotations\instances_val2017.json', 'r') as file:
    data = json.load(file)

# 修改每个序号下的'file_name'值
for item in data['images']:
    if 'file_name' in item:
        print(item['file_name'])
        item['file_name'] = item['file_name'].split('\\')[-1]
        print(item['file_name'])

# 将修改后的内容写回JSON文件
with open(r'D:\00000\C-seg\cells-count\mmdetection\data\coco\annotations\changed\instances_val2017.json', 'w') as file:
    json.dump(data, file, indent=4)