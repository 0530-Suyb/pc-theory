import matplotlib.pyplot as plt          # 导入matplotlib包中的plot()函数
import numpy as np                       # 导入numpy数组包

def drawPCFabricZipfTPS():
    plt.figure(figsize=(8, 6))  # 设置画布大小

    # 每幅子图横坐标
    TPS = ['1000', '1500', '2000', '2500', '3000']
    # 将横坐标先替换为数值
    x = np.arange(len(TPS))
    width = 0.2
    fabric_x = x
    pc_fabric_1pool_x = x + width
    pc_fabric_2pool_x = x + 2 * width

    # 绘图
    plt.title('TPS')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    fabric_1 = [684, 902, 859, 629, 573] # [1022*0.67, 1530*0.59, 1868*0.46, 1793*0.32]
    fabric_2 = [704, 993, 1158, 1096, 750] # [1036*0.68, 1553*0.64, 1998*0.58, 2333*0.47, 2275*0.33]
    pc_fabric_1pool_1 = [726, 985, 1129, 896, 735] # [886*0.82, 1332*0.74, 1661*0.68, 1868*0.48, 1887*0.39]
    pc_fabric_2pool_1 = [679, 984, 1121, 1314, 1047] # [906*0.75, 1368*0.72, 1823*0.67, 2191*0.6, 2381*0.44]
    pc_fabric_1pool_2 = [727, 934, 681, 607, 585] # [887*0.82, 1316*0.71, 1450*0.47, 1481*0.41, 1501*0.39]
    pc_fabric_2pool_2 = [683, 915, 1048, 722, 666] # [911*0.75, 1347*0.68, 1748*0.6, 1805*0.4, 1755*0.38]
    fabric_3 = [(x + y) / 2 for x, y in zip(fabric_1, fabric_2)]
    pc_fabric_1pool_3 = [(x + y) / 2 for x, y in zip(pc_fabric_1pool_1, pc_fabric_1pool_2)]
    pc_fabric_2pool_3 = [(x + y) / 2 for x, y in zip(pc_fabric_2pool_1, pc_fabric_2pool_2)]
    fabric = fabric_3
    pc_fabric_1pool = pc_fabric_1pool_3
    pc_fabric_2pool = pc_fabric_2pool_3
    f1 = plt.bar(fabric_x, fabric, width=width, color='gold', label='Fabric')
    f2 = plt.bar(pc_fabric_1pool_x, pc_fabric_1pool, width=width, color='blue', label='PC-Fabric one pool')
    f3 = plt.bar(pc_fabric_2pool_x, pc_fabric_2pool, width=width, color='red', label='PC-Fabric two pool')
    plt.xticks(x + width, TPS) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 1600, 200))  #设置y轴刻度
    g = [f1, f2, f3]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper left')
    #显示柱状图的高度文本
    for i in range(len(TPS)):
        plt.text(fabric_x[i], fabric[i], fabric[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_1pool_x[i], pc_fabric_1pool[i], pc_fabric_1pool[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_2pool_x[i], pc_fabric_2pool[i], pc_fabric_2pool[i],va="bottom",ha="center",fontsize=8)
    
    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/zipfTesting-tps-3.png")  #保存图像

def drawPCFabricZipfAvgLatency():
    plt.figure(figsize=(8, 6))  # 设置画布大小

    # 每幅子图横坐标
    TPS = ['1000', '1500', '2000', '2500', '3000']
    # 将横坐标先替换为数值
    x = np.arange(len(TPS))
    width = 0.2
    fabric_x = x
    pc_fabric_1pool_x = x + width
    pc_fabric_2pool_x = x + 2 * width

    # 绘图
    plt.title('Latency')
    plt.xlabel('send TPS')
    plt.ylabel('latency(s)')
    fabric_1 = [0.21, 0.63, 1.41, 3.92, 5.55]
    fabric_2 = [0.14, 0.27, 0.55, 1.37, 3.37]
    pc_fabric_1pool_1 = [0.2, 0.29, 0.65, 1.66, 3.76]
    pc_fabric_2pool_1 = [0.22, 0.22, 0.3, 0.68, 1.62]
    pc_fabric_1pool_2 = [0.2, 0.43, 2.21, 4.23, 5.47]
    pc_fabric_2pool_2 = [0.21, 0.38, 0.77, 2.89, 4.04]
    fabric_3 = [(x + y) / 2 for x, y in zip(fabric_1, fabric_2)]
    pc_fabric_1pool_3 = [(x + y) / 2 for x, y in zip(pc_fabric_1pool_1, pc_fabric_1pool_2)]
    pc_fabric_2pool_3 = [(x + y) / 2 for x, y in zip(pc_fabric_2pool_1, pc_fabric_2pool_2)]
    fabric = fabric_3
    pc_fabric_1pool = pc_fabric_1pool_3
    pc_fabric_2pool = pc_fabric_2pool_3
    f1 = plt.bar(fabric_x, fabric, width=width, color='gold', label='Fabric')
    f2 = plt.bar(pc_fabric_1pool_x, pc_fabric_1pool, width=width, color='blue', label='PC-Fabric one pool')
    f3 = plt.bar(pc_fabric_2pool_x, pc_fabric_2pool, width=width, color='red', label='PC-Fabric two pool')
    plt.xticks(x + width, TPS) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 6, 0.5))  #设置y轴刻度
    g = [f1, f2, f3]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper left')
    #显示柱状图的高度文本
    for i in range(len(TPS)):
        plt.text(fabric_x[i], fabric[i], fabric[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_1pool_x[i], pc_fabric_1pool[i], pc_fabric_1pool[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_2pool_x[i], pc_fabric_2pool[i], pc_fabric_2pool[i],va="bottom",ha="center",fontsize=8)
    
    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/zipfTesting-latency-3.png")  #保存图像


if __name__== "__main__" :
    drawPCFabricZipfTPS()
    drawPCFabricZipfAvgLatency()

    