import json
import os

json_file = r'D:\data\data_guo\new-mydata\HH_CPP_1dpi_2487_Upk3a+Krt20_20x2_c1-3.json'
def neg_to_red(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    # 修改每个序号下的'file_name'值
    for item in data['shapes']:
        # if item["label"] == "Neg-EPcell":
        #     item["label"] = "R-EPcell"
        if item["label"] == "R-EPcell":
            item["label"] = "Neg-EPcell"
    # 将修改后的内容写回JSON文件
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

neg_to_red(json_file)



# data_dir = r'outtest'
# for root, dirs, files in os.walk(data_dir):
#     for file in files:
#         if file.endswith('.json'):
#             json_file = os.path.join(root, file)
#             neg_to_red(json_file)