import matplotlib.pyplot as plt

# 数据
labels = ['car', 'truck', 'person', 'bus', 'cyclist', 'bike']
values = [111512, 12694, 57410, 4860, 7529, 5245]

# 设置柱子的宽度
bar_width = 0.5

# 创建柱状图
plt.figure(figsize=(7, 5))
bars = plt.bar(labels, values, color=['blue', 'orange', 'green', 'red', 'purple', 'brown'], width=bar_width)

# 添加标题和标签
plt.title('Vehicle and Person Count')
plt.xlabel('Category')
plt.ylabel('Count')

# 添加图例
plt.legend(bars, labels, loc='upper right')

# 显示图表
plt.show()
