import json
import os
def false_json(jsonfilelist,fause_json_list):
    '''
    筛选因为形状问题无法转化的 json 文件
    '''
    for i in os.listdir(jsonfilelist):
        if i.endswith("json"):
            f=open(os.path.join(jsonfilelist,i),"r")
            jsonfile=json.loads(f.read())
            for j in jsonfile['shapes']:
                point_list=j['points']
                if len(point_list)<3:
                    fause_json_list.append(i)
    return fause_json_list

jsonfilelist = r"D:\data\data_guo\zdata\save-data-4_4\train\imgs"
false_json_list = []

false_json(jsonfilelist,false_json_list)

print(false_json_list)

# for i in false_json_list:
#     os.remove(os.path.join(jsonfilelist,i))
#     os.remove(os.path.join(jsonfilelist, os.path.splitext(i)[0])+'.jpg')

