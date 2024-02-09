import matplotlib.pyplot as plt

# 数据：线程数量和每个数据集的平均时间
threads = [1, 2, 4, 8, 16, 32]
times_small = [28.8, 20.8, 24.0, 22.4, 25.6, 24.0]
times_medium = [19.2, 20.8, 19.2, 17.6, 16.0, 19.2]
times_large = [28.8, 24.0, 19.2, 19.2, 25.6, 16.0]

times_small_par_atom = [2354948.8, 8722352.0, 42234976.0, 145378556.8, 77627102.4, 174876217.6]
times_medium_par_atom = [3424286.4, 7198030.4, 38108892.8, 84799208.0, 197110475.2, 263853251.2]
times_large_par_atom = [5253760.0, 13546996.8, 43579708.8, 83691118.4, 259598350.4, 210871308.8]


# 绘制图表
plt.figure(figsize=(10, 6))

# 绘制每个数据集的曲线
plt.plot(threads, times_small, marker='o', label='Small Dataset')
plt.plot(threads, times_medium, marker='o', label='Medium Dataset')
plt.plot(threads, times_large, marker='o', label='Large Dataset')

# 绘制每个数据集的曲线
plt.plot(threads, times_small_par_atom, marker='o', label='Par_atom Small Dataset')
plt.plot(threads, times_medium_par_atom, marker='o', label='Par_atom Medium Dataset')
plt.plot(threads, times_large_par_atom, marker='o', label='Par_atom Large Dataset')

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
