import matplotlib.pyplot as plt

# 数据：线程数量和每个数据集的平均时间
threads = [1, 2, 4, 8, 16, 32]
times_small = [28.8, 20.8, 24.0, 22.4, 25.6, 24.0]
times_medium = [19.2, 20.8, 19.2, 17.6, 16.0, 19.2]
times_large = [28.8, 24.0, 19.2, 19.2, 25.6, 16.0]

times_small_par = [1546137.6, 1617616.0, 1637860.8, 1786432.0, 1953414.4, 20062579.2]
times_medium_par = [2316012.8, 2623240.0, 2679928.0, 3242457.6, 3431934.4, 5655284.8]
times_large_par = [4473329.6, 4632064.0, 5614577.6, 5587844.8, 7349518.4, 11746334.4]



# 绘制图表
plt.figure(figsize=(10, 6))

# 绘制每个数据集的曲线
plt.plot(threads, times_small, marker='o', label='Small Dataset')
plt.plot(threads, times_medium, marker='o', label='Medium Dataset')
plt.plot(threads, times_large, marker='o', label='Large Dataset')

# 绘制每个数据集的曲线
plt.plot(threads, times_small_par, marker='o', label='Par Small Dataset')
plt.plot(threads, times_medium_par, marker='o', label='Par Medium Dataset')
plt.plot(threads, times_large_par, marker='o', label='Par Large Dataset')

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
