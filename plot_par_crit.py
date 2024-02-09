import matplotlib.pyplot as plt

# 数据：线程数量和每个数据集的平均时间
threads = [1, 2, 4, 8, 16, 32]
times_small = [28.8, 20.8, 24.0, 22.4, 25.6, 24.0]
times_medium = [19.2, 20.8, 19.2, 17.6, 16.0, 19.2]
times_large = [28.8, 24.0, 19.2, 19.2, 25.6, 16.0]

times_small_par_crit = [3740896.0, 28891801.6, 174069889.6, 499817579.2, 1270852692.8, 4121629440.0]
times_medium_par_crit = [4410409.6, 29434660.8, 145143486.4, 440385060.8, 1336424200.0, 4528430702.4]
times_large_par_crit = [7482480.0, 56955390.4, 248061596.8, 693836369.6, 1926404292.8, 6715121612.8]



# 绘制图表
plt.figure(figsize=(10, 6))

# 绘制每个数据集的曲线
plt.plot(threads, times_small, marker='o', label='Small Dataset')
plt.plot(threads, times_medium, marker='o', label='Medium Dataset')
plt.plot(threads, times_large, marker='o', label='Large Dataset')

# 绘制每个数据集的曲线
plt.plot(threads, times_small_par_crit, marker='o', label='Par_crit Small Dataset')
plt.plot(threads, times_medium_par_crit, marker='o', label='Par_crit Medium Dataset')
plt.plot(threads, times_large_par_crit, marker='o', label='Par_crit Large Dataset')

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
