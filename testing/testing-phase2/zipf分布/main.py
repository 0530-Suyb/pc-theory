import numpy as np
import matplotlib.pyplot as plt

# 设置参数
N = 10000  # 总项数
s = 0.01    # Zipf参数

# 计算归一化常数 C
C = sum(1 / (r ** s) for r in range(1, N + 1))

# 计算每个排名的频率
frequencies = [1 / (r ** s) / C for r in range(1, N + 1)]

# 绘制分布图
plt.figure(figsize=(10, 6))
# plt.plot(range(1, 100+1), frequencies[:100], label=f'Zipf Distribution (s={s})')
plt.plot(range(1, N+1), frequencies, label=f'Zipf Distribution (s={s})')
# plt.yscale('log')  # 使用对数坐标
# plt.xscale('log')  # 使用对数坐标
plt.title('Zipf Distribution')
plt.xlabel('Rank (r)')
plt.ylabel('Frequency (f(r))')
plt.grid(True)
plt.legend()
plt.show()