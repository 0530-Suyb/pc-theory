import matplotlib.pyplot as plt          # 导入matplotlib包中的plot()函数
import numpy as np                       # 导入numpy数组包


fabric_dependentTxs_TPS500_MaxK100_FailedRate = [0.1, 0.2, 0.3, 0.4, 0.5]

def drawPCFabricBasicTPSvsLatencyFig():
    # 创建 x 轴数据 to 3000
    x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600,
         1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700]

    # 创建 y 轴数据
    fabric = [0.57, 0.35, 0.27, 0.24, 0.2, 0.18, 0.17, 0.16, 0.15, 0.14, 0.14, 0.14, 0.13, 0.13, 0.13, 0.14, 
              0.14, 0.14, 0.14, 0.14, 0.14, 0.15, 0.17, 0.17, 0.33, 0.51, 0.83]
    pc_fabric_one_pool = [0.56, 0.4, 0.3, 0.25, 0.21, 0.19, 0.17, 0.16, 0.14, 0.14, 0.13, 0.13, 0.13, 0.13, 0.12, 0.12, 
                          0.13, 0.13, 0.14, 0.14, 0.14, 0.15, 0.16, 0.16, 0.34, 0.67]
    pc_fabric_three_pool = [0.75, 0.57, 0.54, 0.51, 0.49, 0.43, 0.38, 0.36, 0.32, 0.32, 0.29, 0.29, 0.26, 0.27, 0.24, 0.27, 
                            0.23, 0.25, 0.23, 0.25, 0.25, 0.27, 0.27, 0.32, 0.89]
    
    # 创建图表和子图对象
    fig, ax = plt.subplots()

    # 绘制折线图
    ax.plot(x, fabric, label='Fabric')
    ax.plot(x[:len(pc_fabric_one_pool)], pc_fabric_one_pool, label='PC-Fabric One Pool')
    ax.plot(x[:len(pc_fabric_three_pool)], pc_fabric_three_pool, label='PC-Fabric Three Pool')

    # 添加图例
    ax.legend(loc='upper right')

    # 添加标题和标签
    ax.set_title('TPS vs Latency')
    ax.set_xlabel('TPS')
    ax.set_ylabel('Latency (s)')

    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/basicTPSvsLatency.png")  #保存图像

def drawPCFabricConflictTxsFig():
    print("drawFig")
    
    plt.figure(figsize=(12, 9))  # 设置画布大小

    
    # 每幅子图横坐标
    MaxK = ['100', '1000', '5000']
    # 将横坐标先替换为数值
    x = np.arange(len(MaxK))
    width = 0.2
    fabric_GETvsSET_3vs1_x = x
    fabric_GETvsSET_9vs1_x = x + width
    pc_fabric_GETvsSET_3vs1_x = x + 2 * width
    pc_fabric_GETvsSET_9vs1_x = x + 3 * width



    # 绘图
    plt.subplot(2,2,1)
    plt.title('TPS = 500')
    plt.xlabel('Max of K')
    plt.ylabel('Failed Rate (%)')
    fabric_GETvsSET_3vs1 = [28, 43, 36]
    fabric_GETvsSET_9vs1 = [34, 74, 73]
    pc_fabric_GETvsSET_3vs1 = [3, 3, 3]
    pc_fabric_GETvsSET_9vs1 = [3, 8, 3]
    f1 = plt.bar(fabric_GETvsSET_3vs1_x, fabric_GETvsSET_3vs1, width=width, color='gold', label='Fabric Get:Set=3:1')
    f2 = plt.bar(fabric_GETvsSET_9vs1_x, fabric_GETvsSET_9vs1, width=width, color='blue', label='Fabric Get:Set=9:1')
    f3 = plt.bar(pc_fabric_GETvsSET_3vs1_x, pc_fabric_GETvsSET_3vs1, width=width, color='silver', label='PC-Fabric Get:Set=3:1')
    f4 = plt.bar(pc_fabric_GETvsSET_9vs1_x, pc_fabric_GETvsSET_9vs1, width=width, color='orange', label='PC-Fabric Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 101, 10))  #设置y轴刻度
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(fabric_GETvsSET_3vs1_x[i],fabric_GETvsSET_3vs1[i], fabric_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(fabric_GETvsSET_9vs1_x[i],fabric_GETvsSET_9vs1[i], fabric_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_GETvsSET_3vs1_x[i],pc_fabric_GETvsSET_3vs1[i], pc_fabric_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_GETvsSET_9vs1_x[i],pc_fabric_GETvsSET_9vs1[i], pc_fabric_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,2)
    plt.title('TPS = 1000')
    plt.xlabel('Max of K')
    plt.ylabel('Failed Rate (%)')
    fabric_GETvsSET_3vs1 = [45, 40, 49]
    fabric_GETvsSET_9vs1 = [50, 41, 62]
    pc_fabric_GETvsSET_3vs1 = [5, 6, 4]
    pc_fabric_GETvsSET_9vs1 = [3, 2, 8]
    f1 = plt.bar(fabric_GETvsSET_3vs1_x, fabric_GETvsSET_3vs1, width=width, color='gold', label='Fabric Get:Set=3:1')
    f2 = plt.bar(fabric_GETvsSET_9vs1_x, fabric_GETvsSET_9vs1, width=width, color='blue', label='Fabric Get:Set=9:1')
    f3 = plt.bar(pc_fabric_GETvsSET_3vs1_x, pc_fabric_GETvsSET_3vs1, width=width, color='silver', label='PC-Fabric Get:Set=3:1')
    f4 = plt.bar(pc_fabric_GETvsSET_9vs1_x, pc_fabric_GETvsSET_9vs1, width=width, color='orange', label='PC-Fabric Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 101, 10))  #设置y轴刻度
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(fabric_GETvsSET_3vs1_x[i],fabric_GETvsSET_3vs1[i], fabric_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(fabric_GETvsSET_9vs1_x[i],fabric_GETvsSET_9vs1[i], fabric_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_GETvsSET_3vs1_x[i],pc_fabric_GETvsSET_3vs1[i], pc_fabric_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_GETvsSET_9vs1_x[i],pc_fabric_GETvsSET_9vs1[i], pc_fabric_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,3)
    plt.title('TPS = 1500')
    plt.xlabel('Max of K')
    plt.ylabel('Failed Rate (%)')
    fabric_GETvsSET_3vs1 = [18, 41, 29]
    fabric_GETvsSET_9vs1 = [43, 71, 64]
    pc_fabric_GETvsSET_3vs1 = [6, 8, 10]
    pc_fabric_GETvsSET_9vs1 = [7, 11, 5]
    f1 = plt.bar(fabric_GETvsSET_3vs1_x, fabric_GETvsSET_3vs1, width=width, color='gold', label='Fabric Get:Set=3:1')
    f2 = plt.bar(fabric_GETvsSET_9vs1_x, fabric_GETvsSET_9vs1, width=width, color='blue', label='Fabric Get:Set=9:1')
    f3 = plt.bar(pc_fabric_GETvsSET_3vs1_x, pc_fabric_GETvsSET_3vs1, width=width, color='silver', label='PC-Fabric Get:Set=3:1')
    f4 = plt.bar(pc_fabric_GETvsSET_9vs1_x, pc_fabric_GETvsSET_9vs1, width=width, color='orange', label='PC-Fabric Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 101, 10))  #设置y轴刻度
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(fabric_GETvsSET_3vs1_x[i],fabric_GETvsSET_3vs1[i], fabric_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(fabric_GETvsSET_9vs1_x[i],fabric_GETvsSET_9vs1[i], fabric_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_GETvsSET_3vs1_x[i],pc_fabric_GETvsSET_3vs1[i], pc_fabric_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_GETvsSET_9vs1_x[i],pc_fabric_GETvsSET_9vs1[i], pc_fabric_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,4)
    plt.title('TPS = 2000')
    plt.xlabel('Max of K')
    plt.ylabel('Failed Rate (%)')
    fabric_GETvsSET_3vs1 = [34, 42, 26]
    fabric_GETvsSET_9vs1 = [41, 54, 49]
    pc_fabric_GETvsSET_3vs1 = [11, 8, 14]
    pc_fabric_GETvsSET_9vs1 = [19, 8, 20]
    f1 = plt.bar(fabric_GETvsSET_3vs1_x, fabric_GETvsSET_3vs1, width=width, color='gold', label='Fabric Get:Set=3:1')
    f2 = plt.bar(fabric_GETvsSET_9vs1_x, fabric_GETvsSET_9vs1, width=width, color='blue', label='Fabric Get:Set=9:1')
    f3 = plt.bar(pc_fabric_GETvsSET_3vs1_x, pc_fabric_GETvsSET_3vs1, width=width, color='silver', label='PC-Fabric Get:Set=3:1')
    f4 = plt.bar(pc_fabric_GETvsSET_9vs1_x, pc_fabric_GETvsSET_9vs1, width=width, color='orange', label='PC-Fabric Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 101, 10))  #设置y轴刻度
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(fabric_GETvsSET_3vs1_x[i],fabric_GETvsSET_3vs1[i], fabric_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(fabric_GETvsSET_9vs1_x[i],fabric_GETvsSET_9vs1[i], fabric_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_GETvsSET_3vs1_x[i],pc_fabric_GETvsSET_3vs1[i], pc_fabric_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_GETvsSET_9vs1_x[i],pc_fabric_GETvsSET_9vs1[i], pc_fabric_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)

    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/conflictTxs.png")  #保存图像

def drawPCFabricConflictTxsValidTPSFig():
    plt.figure(figsize=(12, 9))  # 设置画布大小
    
    # 每幅子图横坐标
    sendTPS = ['500', '1000', '1500', '2000']

    # 绘图1
    plt.subplot(2,3,1)
    y1 = [360, 550, 1230, 1320]
    y2 = [485, 950, 1410, 1780]
    
    plt.plot(sendTPS, y1, label='Fabric')
    plt.plot(sendTPS, y2, label='PC-Fabric')
    plt.legend(loc='upper left')
    plt.title('Get:Set=3:1, Max of K = 100')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图2
    plt.subplot(2,3,2)
    y1 = [285, 600, 885, 1160]
    y2 = [485, 940, 1380, 1840]
    
    plt.plot(sendTPS, y1, label='Fabric')
    plt.plot(sendTPS, y2, label='PC-Fabric')
    plt.legend(loc='upper left')
    plt.title('Get:Set=3:1, Max of K = 1000')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图3
    plt.subplot(2,3,3)
    y1 = [320, 510, 1065, 1480]
    y2 = [485, 960, 1350, 1720]
    
    plt.plot(sendTPS, y1, label='Fabric')
    plt.plot(sendTPS, y2, label='PC-Fabric')
    plt.legend(loc='upper left')
    plt.title('Get:Set=3:1, Max of K = 5000')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图4
    plt.subplot(2,3,4)
    y1 = [330, 500, 855, 1180]
    y2 = [485, 970, 1395, 1620]
    
    plt.plot(sendTPS, y1, label='Fabric')
    plt.plot(sendTPS, y2, label='PC-Fabric')
    plt.legend(loc='upper left')
    plt.title('Get:Set=9:1, Max of K = 100')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图5
    plt.subplot(2,3,5)
    y1 = [130, 590, 435, 920]
    y2 = [460, 980, 1335, 1840]
    
    plt.plot(sendTPS, y1, label='Fabric')
    plt.plot(sendTPS, y2, label='PC-Fabric')
    plt.legend(loc='upper left')
    plt.title('Get:Set=9:1, Max of K = 1000')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图6
    plt.subplot(2,3,6)
    y1 = [135, 380, 540, 1020]
    y2 = [485, 920, 1425, 1600]
    
    plt.plot(sendTPS, y1, label='Fabric')
    plt.plot(sendTPS, y2, label='PC-Fabric')
    plt.legend(loc='upper left')
    plt.title('Get:Set=9:1, Max of K = 5000')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度

    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/conflictTxsValidTPS.png")  #保存图像

def drawPCFabricDependentTxsFig():
    print("drawFig")
    
    plt.figure(figsize=(8, 6))  # 设置画布大小

    
    # 每幅子图横坐标
    TPS = ['500', '1000', '1500', '2000']
    # 将横坐标先替换为数值
    x = np.arange(len(TPS))
    width = 0.2
    fabric_x = x
    pc_fabric_x = x + width

    # 绘图
    plt.title('TPS vs Latency')
    plt.xlabel('TPS')
    plt.ylabel('Latency (ms)')
    fabric = [363, 244, 307, 612]
    pc_fabric = [196, 133, 125, 144]
    f1 = plt.bar(fabric_x, fabric, width=width, color='gold', label='Fabric')
    f2 = plt.bar(pc_fabric_x, pc_fabric, width=width, color='blue', label='PC-Fabric')
    plt.xticks(x + width, labels=TPS) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 701, 100))  #设置y轴刻度
    g = [f1, f2]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper left')
    #显示柱状图的高度文本
    for i in range(len(TPS)):
        plt.text(fabric_x[i], fabric[i], fabric[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_fabric_x[i], pc_fabric[i], pc_fabric[i],va="bottom",ha="center",fontsize=8)
    
    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/dependentTxs.png")  #保存图像


def drawPCP3ChainBasicTPSvsLatencyFig():
    # 创建 x 轴数据 to 3000
    x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 
         1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 
         3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000]

    # 创建 y 轴数据
    pc_p3chain_one_pool = [1.075, 1.122, 1.131, 1.17, 1.185, 1.22, 1.196, 1.216, 1.211, 1.226, 1.142, 1.214, 1.208, 1.18, 1.235, 
                          1.231, 1.241, 1.217, 1.24, 1.245, 1.333, 1.298, 1.267, 1.324, 1.274, 1.3, 1.345, 1.398, 1.524, 1.334, 
                          1.309, 1.435, 1.571, 1.675, 1.79, 1.813, 1.811, 1.762, 1.659, 1.632]
    pc_p3chain_three_pool = [1.334, 1.328, 1.375, 1.424, 1.398, 1.415, 1.395, 1.383, 1.389, 1.399, 1.383, 1.407, 1.456, 1.513, 1.436, 
                            1.501, 1.447, 1.44, 1.449, 1.483, 1.522, 1.551, 1.608, 1.571, 1.666, 1.713, 1.586, 1.582, 1.709, 1.994, 
                            1.955, 1.835, 2.125, 2.11, 1.952, 2.177, 2.193, 2.287, 2.216, 2.215]
    pc_p3chain_midProc_one_pool_200ms = [1.262, 1.31, 1.288, 1.319, 1.332, 1.328, 1.319, 1.326, 1.318, 1.324, 1.321, 1.343, 1.351, 1.381, 1.34, 1.406, 1.409, 1.444, 1.469, 1.444, 1.369, 1.577, 1.507, 1.638, 1.447, 1.654, 1.791, 1.685, 1.562, 2.336, 1.865, 1.876, 2.002, 2.682, 2.353, 1.942, 2.703, 2.635, 2.604, 2.179]
    pc_p3chain_midProc_one_pool_800ms = [1.286, 1.296, 1.298, 1.294, 1.285, 1.286, 1.309, 1.259, 1.282, 1.286, 1.306, 1.34, 1.337, 1.3, 1.348, 1.333, 1.338, 1.395, 1.484, 1.412, 1.7, 1.617, 1.609, 1.622, 2.028, 1.83, 1.84, 1.683, 2.245, 1.957, 2.226, 2.032, 2.283, 2.481, 2.469, 2.399, 2.427, 2.882, 3.028, 2.491]
    pc_p3chain_midProc_three_pool = [1.327, 1.318, 1.33, 1.379, 1.378, 1.316, 1.317, 1.343, 1.398, 1.347, 1.345, 1.391, 1.406, 1.363, 1.413, 1.378, 1.396, 1.53, 1.436, 1.455, 1.708, 1.699, 1.911, 1.861, 1.962, 1.979, 2.102, 2.032, 2.155, 2.241, 2.295, 2.2, 2.113, 2.619, 2.519, 2.219, 2.719, 2.379, 2.61, 2.422]

    # 创建图表和子图对象
    fig, ax = plt.subplots()

    # 绘制折线图
    ax.plot(x[:len(pc_p3chain_one_pool)], pc_p3chain_one_pool, label='PC-P3Chain One Pool 200ms')
    ax.plot(x[:len(pc_p3chain_three_pool)], pc_p3chain_three_pool, label='PC-P3Chain Three Pool 500ms')
    ax.plot(x[:len(pc_p3chain_one_pool)], pc_p3chain_midProc_one_pool_200ms, label='PC-P3Chain One Pool midProc 200ms')
    ax.plot(x[:len(pc_p3chain_one_pool)], pc_p3chain_midProc_one_pool_800ms, label='PC-P3Chain One Pool midProc 800ms')
    ax.plot(x[:len(pc_p3chain_three_pool)], pc_p3chain_midProc_three_pool, label='PC-P3Chain Three Pool midProc 800ms')

    # 添加图例
    ax.legend(loc='upper left')

    # 添加标题和标签
    ax.set_title('TPS vs Latency')
    ax.set_xlabel('TPS')
    ax.set_ylabel('Latency (s)')

    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/PC-P3Chain_BasicTPSvsLatency.png")  #保存图像

def drawPCP3ChainConflictTxsFig():
    plt.figure(figsize=(12, 9))  # 设置画布大小

    # 每幅子图横坐标
    MaxK = ['100', '1000', '5000']
    # 将横坐标先替换为数值
    x = np.arange(len(MaxK))
    width = 0.2
    pc_p3chain_BLOCK_GETvsSET_3vs1_x = x
    pc_p3chain_BLOCK_GETvsSET_9vs1_x = x + width
    pc_p3chain_POOL_GETvsSET_3vs1_x = x + 2 * width
    pc_p3chain_POOL_GETvsSET_9vs1_x = x + 3 * width



    # 绘图
    plt.subplot(2,2,1)
    plt.title('TPS = 500')
    plt.xlabel('Max of K')
    # plt.ylabel('Valid Rate (%)')
    # pc_p3chain_BLOCK_GETvsSET_3vs1 = [85.3, 98.2, 98.9]
    # pc_p3chain_BLOCK_GETvsSET_9vs1 = [84.9, 99.9, 100]
    # pc_p3chain_POOL_GETvsSET_3vs1 = [100, 99.6, 100]
    # pc_p3chain_POOL_GETvsSET_9vs1 = [100, 100, 100]
    plt.ylabel('Failed Rate (%)')
    pc_p3chain_BLOCK_GETvsSET_3vs1 = [14.7, 1.8, 1.1]
    pc_p3chain_BLOCK_GETvsSET_9vs1 = [15.1, 0.1, 0]
    pc_p3chain_POOL_GETvsSET_3vs1 = [0, 0.4, 0]
    pc_p3chain_POOL_GETvsSET_9vs1 = [0, 0, 0]
    f1 = plt.bar(pc_p3chain_BLOCK_GETvsSET_3vs1_x, pc_p3chain_BLOCK_GETvsSET_3vs1, width=width, color='gold', label='BLOCK Get:Set=3:1')
    f2 = plt.bar(pc_p3chain_BLOCK_GETvsSET_9vs1_x, pc_p3chain_BLOCK_GETvsSET_9vs1, width=width, color='blue', label='BLOCK Get:Set=9:1')
    f3 = plt.bar(pc_p3chain_POOL_GETvsSET_3vs1_x, pc_p3chain_POOL_GETvsSET_3vs1, width=width, color='silver', label='POOL Get:Set=3:1')
    f4 = plt.bar(pc_p3chain_POOL_GETvsSET_9vs1_x, pc_p3chain_POOL_GETvsSET_9vs1, width=width, color='orange', label='POOL Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 26, 5))  #设置y轴刻度
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(pc_p3chain_BLOCK_GETvsSET_3vs1_x[i],pc_p3chain_BLOCK_GETvsSET_3vs1[i], pc_p3chain_BLOCK_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_BLOCK_GETvsSET_9vs1_x[i],pc_p3chain_BLOCK_GETvsSET_9vs1[i], pc_p3chain_BLOCK_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_3vs1_x[i],pc_p3chain_POOL_GETvsSET_3vs1[i], pc_p3chain_POOL_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_9vs1_x[i],pc_p3chain_POOL_GETvsSET_9vs1[i], pc_p3chain_POOL_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,2)
    plt.title('TPS = 1000')
    plt.xlabel('Max of K')
    # plt.ylabel('Valid Rate (%)')
    # pc_p3chain_BLOCK_GETvsSET_3vs1 = [81.5, 92.4, 99.1]
    # pc_p3chain_BLOCK_GETvsSET_9vs1 = [83.6, 99.6, 100]
    # pc_p3chain_POOL_GETvsSET_3vs1 = [99.6, 97.1, 99.9]
    # pc_p3chain_POOL_GETvsSET_9vs1 = [98.2, 100, 100]
    plt.ylabel('Failed Rate (%)')
    pc_p3chain_BLOCK_GETvsSET_3vs1 = [18.5, 7.6, 0.9]
    pc_p3chain_BLOCK_GETvsSET_9vs1 = [16.4, 0.4, 0]
    pc_p3chain_POOL_GETvsSET_3vs1 = [0.4, 2.9, 0.1]
    pc_p3chain_POOL_GETvsSET_9vs1 = [1.8, 0, 0]
    f1 = plt.bar(pc_p3chain_BLOCK_GETvsSET_3vs1_x, pc_p3chain_BLOCK_GETvsSET_3vs1, width=width, color='gold', label='BLOCK Get:Set=3:1')
    f2 = plt.bar(pc_p3chain_BLOCK_GETvsSET_9vs1_x, pc_p3chain_BLOCK_GETvsSET_9vs1, width=width, color='blue', label='BLOCK Get:Set=9:1')
    f3 = plt.bar(pc_p3chain_POOL_GETvsSET_3vs1_x, pc_p3chain_POOL_GETvsSET_3vs1, width=width, color='silver', label='POOL Get:Set=3:1')
    f4 = plt.bar(pc_p3chain_POOL_GETvsSET_9vs1_x, pc_p3chain_POOL_GETvsSET_9vs1, width=width, color='orange', label='POOL Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 26, 5))  #设置y轴刻度
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(pc_p3chain_BLOCK_GETvsSET_3vs1_x[i],pc_p3chain_BLOCK_GETvsSET_3vs1[i], pc_p3chain_BLOCK_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_BLOCK_GETvsSET_9vs1_x[i],pc_p3chain_BLOCK_GETvsSET_9vs1[i], pc_p3chain_BLOCK_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_3vs1_x[i],pc_p3chain_POOL_GETvsSET_3vs1[i], pc_p3chain_POOL_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_9vs1_x[i],pc_p3chain_POOL_GETvsSET_9vs1[i], pc_p3chain_POOL_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,3)
    plt.title('TPS = 1500')
    plt.xlabel('Max of K')
    # plt.ylabel('Valid Rate (%)')
    # pc_p3chain_BLOCK_GETvsSET_3vs1 = [82.8, 86.7, 99.4]
    # pc_p3chain_BLOCK_GETvsSET_9vs1 = [82, 95.5, 98.5]
    # pc_p3chain_POOL_GETvsSET_3vs1 = [99.8, 99.9, 100]
    # pc_p3chain_POOL_GETvsSET_9vs1 = [99.4, 100, 100]
    plt.ylabel('Failed Rate (%)')
    pc_p3chain_BLOCK_GETvsSET_3vs1 = [17.2, 13.3, 0.6]
    pc_p3chain_BLOCK_GETvsSET_9vs1 = [18, 4.5, 1.5]
    pc_p3chain_POOL_GETvsSET_3vs1 = [0.2, 0.1, 0]
    pc_p3chain_POOL_GETvsSET_9vs1 = [0.6, 0, 0]
    f1 = plt.bar(pc_p3chain_BLOCK_GETvsSET_3vs1_x, pc_p3chain_BLOCK_GETvsSET_3vs1, width=width, color='gold', label='BLOCK Get:Set=3:1')
    f2 = plt.bar(pc_p3chain_BLOCK_GETvsSET_9vs1_x, pc_p3chain_BLOCK_GETvsSET_9vs1, width=width, color='blue', label='BLOCK Get:Set=9:1')
    f3 = plt.bar(pc_p3chain_POOL_GETvsSET_3vs1_x, pc_p3chain_POOL_GETvsSET_3vs1, width=width, color='silver', label='POOL Get:Set=3:1')
    f4 = plt.bar(pc_p3chain_POOL_GETvsSET_9vs1_x, pc_p3chain_POOL_GETvsSET_9vs1, width=width, color='orange', label='POOL Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 26, 5))  #设置y轴刻度
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(pc_p3chain_BLOCK_GETvsSET_3vs1_x[i],pc_p3chain_BLOCK_GETvsSET_3vs1[i], pc_p3chain_BLOCK_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_BLOCK_GETvsSET_9vs1_x[i],pc_p3chain_BLOCK_GETvsSET_9vs1[i], pc_p3chain_BLOCK_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_3vs1_x[i],pc_p3chain_POOL_GETvsSET_3vs1[i], pc_p3chain_POOL_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_9vs1_x[i],pc_p3chain_POOL_GETvsSET_9vs1[i], pc_p3chain_POOL_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,4)
    plt.title('TPS = 2000')
    plt.xlabel('Max of K')
    # plt.ylabel('Valid Rate (%)')
    # pc_p3chain_BLOCK_GETvsSET_3vs1 = [84.8, 86.9, 99.9]
    # pc_p3chain_BLOCK_GETvsSET_9vs1 = [79.5, 92.8, 97.8]
    # pc_p3chain_POOL_GETvsSET_3vs1 = [99.5, 97.8, 100]
    # pc_p3chain_POOL_GETvsSET_9vs1 = [98.9, 99.9, 100]
    plt.ylabel('Failed Rate (%)')
    pc_p3chain_BLOCK_GETvsSET_3vs1 = [15.2, 13.1, 0.1]
    pc_p3chain_BLOCK_GETvsSET_9vs1 = [20.5, 7.2, 2.2]
    pc_p3chain_POOL_GETvsSET_3vs1 = [0.5, 2.2, 0]
    pc_p3chain_POOL_GETvsSET_9vs1 = [1.1, 0.1, 0]
    f1 = plt.bar(pc_p3chain_BLOCK_GETvsSET_3vs1_x, pc_p3chain_BLOCK_GETvsSET_3vs1, width=width, color='gold', label='BLOCK Get:Set=3:1')
    f2 = plt.bar(pc_p3chain_BLOCK_GETvsSET_9vs1_x, pc_p3chain_BLOCK_GETvsSET_9vs1, width=width, color='blue', label='BLOCK Get:Set=9:1')
    f3 = plt.bar(pc_p3chain_POOL_GETvsSET_3vs1_x, pc_p3chain_POOL_GETvsSET_3vs1, width=width, color='silver', label='POOL Get:Set=3:1')
    f4 = plt.bar(pc_p3chain_POOL_GETvsSET_9vs1_x, pc_p3chain_POOL_GETvsSET_9vs1, width=width, color='orange', label='POOL Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 26, 5))  #设置y轴刻度
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(pc_p3chain_BLOCK_GETvsSET_3vs1_x[i],pc_p3chain_BLOCK_GETvsSET_3vs1[i], pc_p3chain_BLOCK_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_BLOCK_GETvsSET_9vs1_x[i],pc_p3chain_BLOCK_GETvsSET_9vs1[i], pc_p3chain_BLOCK_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_3vs1_x[i],pc_p3chain_POOL_GETvsSET_3vs1[i], pc_p3chain_POOL_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_9vs1_x[i],pc_p3chain_POOL_GETvsSET_9vs1[i], pc_p3chain_POOL_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)

    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/PC-P3Chain_ConflictTxs.png")  #保存图像

def drawPCP3ChainDependentTxsFig():
    plt.figure(figsize=(8, 6))  # 设置画布大小

    # 每幅子图横坐标
    TPS = ['500', '1000', '1500', '2000']
    # 将横坐标先替换为数值
    x = np.arange(len(TPS))
    width = 0.2
    commonSelector_x = x
    depSelector_x = x + width

    # 绘图
    plt.title('TPS vs Latency')
    plt.xlabel('TPS')
    plt.ylabel('Latency (ms)')
    commonSelector = [2732, 2832, 2901, 3381]
    depSelector = [1404, 1413, 1435, 1443]
    f1 = plt.bar(commonSelector_x, commonSelector, width=width, color='gold', label='PC-P3Chain commonSelector')
    f2 = plt.bar(depSelector_x, depSelector, width=width, color='blue', label='PC-P3Chain depSelector')
    plt.xticks(x + width, labels=TPS) #将横坐标数值转换为MaxK
    plt.yticks(np.arange(0, 4000, 400))  #设置y轴刻度
    g = [f1, f2]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='upper left')
    #显示柱状图的高度文本
    for i in range(len(TPS)):
        plt.text(commonSelector_x[i], commonSelector[i], commonSelector[i],va="bottom",ha="center",fontsize=8)
        plt.text(depSelector_x[i], depSelector[i], depSelector[i],va="bottom",ha="center",fontsize=8)
    
    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/PC-P3Chain_DependentTxs.png")  #保存图像

def drawPCP3ChainConflictTxsValidTPSFig():
    plt.figure(figsize=(12, 9))  # 设置画布大小
    
    # 每幅子图横坐标
    sendTPS = ['500', '1000', '1500', '2000']

    # 绘图1
    plt.subplot(2,3,1)
    y1 = [427, 815, 1242, 1696]
    y2 = [500, 996, 1497, 1990]
    
    plt.plot(sendTPS, y1, label='BLOCK')
    plt.plot(sendTPS, y2, label='POOL')
    plt.legend(loc='upper left')
    plt.title('Get:Set=3:1, Max of K = 100')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图2
    plt.subplot(2,3,2)
    y1 = [491, 924, 1300, 1738]
    y2 = [498, 971, 1499, 1956]
    
    plt.plot(sendTPS, y1, label='BLOCK')
    plt.plot(sendTPS, y2, label='POOL')
    plt.legend(loc='upper left')
    plt.title('Get:Set=3:1, Max of K = 1000')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图3
    plt.subplot(2,3,3)
    y1 = [495, 991, 1491, 1998]
    y2 = [500, 999, 1500, 2000]
    
    plt.plot(sendTPS, y1, label='BLOCK')
    plt.plot(sendTPS, y2, label='POOL')
    plt.legend(loc='upper left')
    plt.title('Get:Set=3:1, Max of K = 5000')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图4
    plt.subplot(2,3,4)
    y1 = [425, 836, 1230, 1590]
    y2 = [500, 982, 1491, 1978]
    
    plt.plot(sendTPS, y1, label='BLOCK')
    plt.plot(sendTPS, y2, label='POOL')
    plt.legend(loc='upper left')
    plt.title('Get:Set=9:1, Max of K = 100')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图5
    plt.subplot(2,3,5)
    y1 = [499, 996, 1433, 1856]
    y2 = [500, 1000, 1500, 1998]
    
    plt.plot(sendTPS, y1, label='BLOCK')
    plt.plot(sendTPS, y2, label='POOL')
    plt.legend(loc='upper left')
    plt.title('Get:Set=9:1, Max of K = 1000')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度
    
    # 绘图6
    plt.subplot(2,3,6)
    y1 = [500, 1000, 1478, 1956]
    y2 = [500, 1000, 1500, 2000]
    
    plt.plot(sendTPS, y1, label='BLOCK')
    plt.plot(sendTPS, y2, label='POOL')
    plt.legend(loc='upper left')
    plt.title('Get:Set=9:1, Max of K = 5000')
    plt.xlabel('send TPS')
    plt.ylabel('real TPS')
    plt.yticks(np.arange(0, 2001, 200))  #设置y轴刻度

    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/PC-P3Chain_ConflictTxsValidTPS.png")  #保存图像


def drawPCP3ChainConflictTxsTPSValueFig():
    plt.figure(figsize=(12, 9))  # 设置画布大小

    # 每幅子图横坐标
    MaxK = ['100', '1000', '5000']
    # 将横坐标先替换为数值
    x = np.arange(len(MaxK))
    width = 0.2
    pc_p3chain_BLOCK_GETvsSET_3vs1_x = x
    pc_p3chain_BLOCK_GETvsSET_9vs1_x = x + width
    pc_p3chain_POOL_GETvsSET_3vs1_x = x + 2 * width
    pc_p3chain_POOL_GETvsSET_9vs1_x = x + 3 * width



    # 绘图
    plt.subplot(2,2,1)
    plt.title('TPS = 500')
    plt.xlabel('Max of K')
    # plt.ylabel('Valid Rate (%)')
    # pc_p3chain_BLOCK_GETvsSET_3vs1 = [85.3, 98.2, 98.9]
    # pc_p3chain_BLOCK_GETvsSET_9vs1 = [84.9, 99.9, 100]
    # pc_p3chain_POOL_GETvsSET_3vs1 = [100, 99.6, 100]
    # pc_p3chain_POOL_GETvsSET_9vs1 = [100, 100, 100]
    plt.ylabel('Failed Rate (%)')
    pc_p3chain_BLOCK_GETvsSET_3vs1 = [ 5 * (100 - item) for item in [14.7, 1.8, 1.1]]
    pc_p3chain_BLOCK_GETvsSET_9vs1 = [ 5 * (100 - item) for item in [15.1, 0.1, 0]]
    pc_p3chain_POOL_GETvsSET_3vs1 = [ 5 * (100 - item) for item in [0, 0.4, 0]]
    pc_p3chain_POOL_GETvsSET_9vs1 = [ 5 * (100 - item) for item in [0, 0, 0]]
    f1 = plt.bar(pc_p3chain_BLOCK_GETvsSET_3vs1_x, pc_p3chain_BLOCK_GETvsSET_3vs1, width=width, color='gold', label='BLOCK Get:Set=3:1')
    f2 = plt.bar(pc_p3chain_BLOCK_GETvsSET_9vs1_x, pc_p3chain_BLOCK_GETvsSET_9vs1, width=width, color='blue', label='BLOCK Get:Set=9:1')
    f3 = plt.bar(pc_p3chain_POOL_GETvsSET_3vs1_x, pc_p3chain_POOL_GETvsSET_3vs1, width=width, color='silver', label='POOL Get:Set=3:1')
    f4 = plt.bar(pc_p3chain_POOL_GETvsSET_9vs1_x, pc_p3chain_POOL_GETvsSET_9vs1, width=width, color='orange', label='POOL Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='lower right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(pc_p3chain_BLOCK_GETvsSET_3vs1_x[i],pc_p3chain_BLOCK_GETvsSET_3vs1[i], pc_p3chain_BLOCK_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_BLOCK_GETvsSET_9vs1_x[i],pc_p3chain_BLOCK_GETvsSET_9vs1[i], pc_p3chain_BLOCK_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_3vs1_x[i],pc_p3chain_POOL_GETvsSET_3vs1[i], pc_p3chain_POOL_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_9vs1_x[i],pc_p3chain_POOL_GETvsSET_9vs1[i], pc_p3chain_POOL_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,2)
    plt.title('TPS = 1000')
    plt.xlabel('Max of K')
    # plt.ylabel('Valid Rate (%)')
    # pc_p3chain_BLOCK_GETvsSET_3vs1 = [81.5, 92.4, 99.1]
    # pc_p3chain_BLOCK_GETvsSET_9vs1 = [83.6, 99.6, 100]
    # pc_p3chain_POOL_GETvsSET_3vs1 = [99.6, 97.1, 99.9]
    # pc_p3chain_POOL_GETvsSET_9vs1 = [98.2, 100, 100]
    plt.ylabel('Failed Rate (%)')
    pc_p3chain_BLOCK_GETvsSET_3vs1 = [ 10 * (100 - item) for item in [18.5, 7.6, 0.9]]
    pc_p3chain_BLOCK_GETvsSET_9vs1 = [ 10 * (100 - item) for item in [16.4, 0.4, 0]]
    pc_p3chain_POOL_GETvsSET_3vs1 = [ 10 * (100 - item) for item in [0.4, 2.9, 0.1]]
    pc_p3chain_POOL_GETvsSET_9vs1 = [ 10 * (100 - item) for item in [1.8, 0, 0]]
    f1 = plt.bar(pc_p3chain_BLOCK_GETvsSET_3vs1_x, pc_p3chain_BLOCK_GETvsSET_3vs1, width=width, color='gold', label='BLOCK Get:Set=3:1')
    f2 = plt.bar(pc_p3chain_BLOCK_GETvsSET_9vs1_x, pc_p3chain_BLOCK_GETvsSET_9vs1, width=width, color='blue', label='BLOCK Get:Set=9:1')
    f3 = plt.bar(pc_p3chain_POOL_GETvsSET_3vs1_x, pc_p3chain_POOL_GETvsSET_3vs1, width=width, color='silver', label='POOL Get:Set=3:1')
    f4 = plt.bar(pc_p3chain_POOL_GETvsSET_9vs1_x, pc_p3chain_POOL_GETvsSET_9vs1, width=width, color='orange', label='POOL Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='lower right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(pc_p3chain_BLOCK_GETvsSET_3vs1_x[i],pc_p3chain_BLOCK_GETvsSET_3vs1[i], pc_p3chain_BLOCK_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_BLOCK_GETvsSET_9vs1_x[i],pc_p3chain_BLOCK_GETvsSET_9vs1[i], pc_p3chain_BLOCK_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_3vs1_x[i],pc_p3chain_POOL_GETvsSET_3vs1[i], pc_p3chain_POOL_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_9vs1_x[i],pc_p3chain_POOL_GETvsSET_9vs1[i], pc_p3chain_POOL_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,3)
    plt.title('TPS = 1500')
    plt.xlabel('Max of K')
    # plt.ylabel('Valid Rate (%)')
    # pc_p3chain_BLOCK_GETvsSET_3vs1 = [82.8, 86.7, 99.4]
    # pc_p3chain_BLOCK_GETvsSET_9vs1 = [82, 95.5, 98.5]
    # pc_p3chain_POOL_GETvsSET_3vs1 = [99.8, 99.9, 100]
    # pc_p3chain_POOL_GETvsSET_9vs1 = [99.4, 100, 100]
    plt.ylabel('Failed Rate (%)')
    pc_p3chain_BLOCK_GETvsSET_3vs1 = [ 15 * (100 - item) for item in [17.2, 13.3, 0.6]]
    pc_p3chain_BLOCK_GETvsSET_9vs1 = [ 15 * (100 - item) for item in [18, 4.5, 1.5]]
    pc_p3chain_POOL_GETvsSET_3vs1 = [ 15 * (100 - item) for item in [0.2, 0.1, 0]]
    pc_p3chain_POOL_GETvsSET_9vs1 = [ 15 * (100 - item) for item in [0.6, 0, 0]]
    f1 = plt.bar(pc_p3chain_BLOCK_GETvsSET_3vs1_x, pc_p3chain_BLOCK_GETvsSET_3vs1, width=width, color='gold', label='BLOCK Get:Set=3:1')
    f2 = plt.bar(pc_p3chain_BLOCK_GETvsSET_9vs1_x, pc_p3chain_BLOCK_GETvsSET_9vs1, width=width, color='blue', label='BLOCK Get:Set=9:1')
    f3 = plt.bar(pc_p3chain_POOL_GETvsSET_3vs1_x, pc_p3chain_POOL_GETvsSET_3vs1, width=width, color='silver', label='POOL Get:Set=3:1')
    f4 = plt.bar(pc_p3chain_POOL_GETvsSET_9vs1_x, pc_p3chain_POOL_GETvsSET_9vs1, width=width, color='orange', label='POOL Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='lower right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(pc_p3chain_BLOCK_GETvsSET_3vs1_x[i],pc_p3chain_BLOCK_GETvsSET_3vs1[i], pc_p3chain_BLOCK_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_BLOCK_GETvsSET_9vs1_x[i],pc_p3chain_BLOCK_GETvsSET_9vs1[i], pc_p3chain_BLOCK_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_3vs1_x[i],pc_p3chain_POOL_GETvsSET_3vs1[i], pc_p3chain_POOL_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_9vs1_x[i],pc_p3chain_POOL_GETvsSET_9vs1[i], pc_p3chain_POOL_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
    

    # 绘图
    plt.subplot(2,2,4)
    plt.title('TPS = 2000')
    plt.xlabel('Max of K')
    # plt.ylabel('Valid Rate (%)')
    # pc_p3chain_BLOCK_GETvsSET_3vs1 = [84.8, 86.9, 99.9]
    # pc_p3chain_BLOCK_GETvsSET_9vs1 = [79.5, 92.8, 97.8]
    # pc_p3chain_POOL_GETvsSET_3vs1 = [99.5, 97.8, 100]
    # pc_p3chain_POOL_GETvsSET_9vs1 = [98.9, 99.9, 100]
    plt.ylabel('Failed Rate (%)')
    pc_p3chain_BLOCK_GETvsSET_3vs1 = [ 20 * (100 - item) for item in [15.2, 13.1, 0.1]]
    pc_p3chain_BLOCK_GETvsSET_9vs1 = [ 20 * (100 - item) for item in [20.5, 7.2, 2.2]]
    pc_p3chain_POOL_GETvsSET_3vs1 = [ 20 * (100 - item) for item in [0.5, 2.2, 0]]
    pc_p3chain_POOL_GETvsSET_9vs1 = [ 20 * (100 - item) for item in [1.1, 0.1, 0]]
    f1 = plt.bar(pc_p3chain_BLOCK_GETvsSET_3vs1_x, pc_p3chain_BLOCK_GETvsSET_3vs1, width=width, color='gold', label='BLOCK Get:Set=3:1')
    f2 = plt.bar(pc_p3chain_BLOCK_GETvsSET_9vs1_x, pc_p3chain_BLOCK_GETvsSET_9vs1, width=width, color='blue', label='BLOCK Get:Set=9:1')
    f3 = plt.bar(pc_p3chain_POOL_GETvsSET_3vs1_x, pc_p3chain_POOL_GETvsSET_3vs1, width=width, color='silver', label='POOL Get:Set=3:1')
    f4 = plt.bar(pc_p3chain_POOL_GETvsSET_9vs1_x, pc_p3chain_POOL_GETvsSET_9vs1, width=width, color='orange', label='POOL Get:Set=9:1')
    plt.xticks(x + width, labels=MaxK) #将横坐标数值转换为MaxK
    g = [f1, f2, f3, f4]
    f = [l.get_label() for l in g]
    plt.legend(g, f, fontsize=7, loc='lower right')
    #显示柱状图的高度文本
    for i in range(len(MaxK)):
        plt.text(pc_p3chain_BLOCK_GETvsSET_3vs1_x[i],pc_p3chain_BLOCK_GETvsSET_3vs1[i], pc_p3chain_BLOCK_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_BLOCK_GETvsSET_9vs1_x[i],pc_p3chain_BLOCK_GETvsSET_9vs1[i], pc_p3chain_BLOCK_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_3vs1_x[i],pc_p3chain_POOL_GETvsSET_3vs1[i], pc_p3chain_POOL_GETvsSET_3vs1[i],va="bottom",ha="center",fontsize=8)
        plt.text(pc_p3chain_POOL_GETvsSET_9vs1_x[i],pc_p3chain_POOL_GETvsSET_9vs1[i], pc_p3chain_POOL_GETvsSET_9vs1[i],va="bottom",ha="center",fontsize=8)

    plt.tight_layout()  #tight_layout() 函数来自动调整子图间距,从而避免部分内容（标题等）被遮住
    # plt.show()          #展示图像
    plt.savefig("img/PC-P3Chain_ConflictTxsTPSValue.png")  #保存图像


if __name__== "__main__" :
    drawPCP3ChainConflictTxsValidTPSFig()

    