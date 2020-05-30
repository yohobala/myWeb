# 打开文件
import json
import os

f = open(os.path.dirname(os.getcwd()) + '/drawContours/contourdata.json', 'r')
# 获得一个字典格式的数据
data = json.load(f)
print(data)