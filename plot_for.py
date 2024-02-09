import matplotlib.pyplot as plt

# 数据：线程数量和每个数据集的平均时间
threads = [1, 2, 4, 8, 16, 32]
times_small = [28.8, 20.8, 24.0, 22.4, 25.6, 24.0]
times_medium = [19.2, 20.8, 19.2, 17.6, 16.0, 19.2]
times_large = [28.8, 24.0, 19.2, 19.2, 25.6, 16.0]

times_small_for = [1643076.8, 947499.2, 738796.8, 461996.8, 368835.2, 2929798.4]
times_medium_for = [3037753.6, 1455328.0, 1133937.6, 634121.6, 391401.6, 9803081.6]
times_large_for = [4711024.0, 2787667.2, 1668092.8, 1077361.6, 732950.4, 3959947.2]


# 绘制图表
plt.figure(figsize=(10, 6))

# 绘制每个数据集的曲线
plt.plot(threads, times_small, marker='o', label='Small Dataset')
plt.plot(threads, times_medium, marker='o', label='Medium Dataset')
plt.plot(threads, times_large, marker='o', label='Large Dataset')

# 绘制每个数据集的曲线
plt.plot(threads, times_small_for, marker='o', label='For Small Dataset')
plt.plot(threads, times_medium_for, marker='o', label='For Medium Dataset')
plt.plot(threads, times_large_for, marker='o', label='For Large Dataset')

# 添加标题和轴标签
plt.title('Average Triangle Count Time vs. Number of Threads')
plt.xlabel('Number of Threads')
plt.ylabel('Average Time (cycles)')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图表
plt.show()
