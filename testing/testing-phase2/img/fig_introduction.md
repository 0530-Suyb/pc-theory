[toc]

## 基础性能测试

### 实验环境

云服务器SA4.16XLARGE256

| 硬件 | 性能                           |
| ---- | ------------------------------ |
| CPU  | AMD EPYC Genoa(-/3.7GHz)，64核 |
| 内存 | 256GB                          |
| 硬盘 | 128GB                          |

| 软件           | 版本    |
| -------------- | ------- |
| ubuntu         | 20.04   |
| tape           |         |
| docker         |         |
| docker-compose |         |
| Fabric         | v2.2.14 |
| PC-Fabric      |         |
| PC-P3Chain     |         |



### 实验设置

对照组设置：**Fabric** vs **PC-Fabric one pool** vs **PC-Fabric two pools**

- Fabric
- PC-Fabric one pool：smallbank不管hotkey还是coldkey都往一个池，因此sort模块只用把smallbank合约的交易往某个池送，select模块中实现重排序。
- PC-Fabric two pool：hotkey和coldkey从100划分，sort模块首先确定是smallbank合约，再看涉及的账号是0-99还是100-9999，以此来分入不同池，处理hotkey的池使用重排序，coldkey就正常打包。

| 自变量          | 参数                                                         |
| --------------- | ------------------------------------------------------------ |
| 网络拓扑        | 2 peer（不同组织）、3 orderer（raft）                        |
| 交易类型        | zipf分布的smallbank交易，偏移s=1，写率w=0.5，总账号量10000   |
| 发送TPS         | 1000 - 3000 （500递增，各次TPS测试时长20s）                  |
| orderer共识配置 | 交易最多等待时间1s、单笔交易最大大小99MB、单个区块最多交易数300、单个区块所有交易最大总大小512KB（双节点背书）（实际上起作用为512KB，约140笔交易，经过测试当前配置相对较好） |



### 实验结果

![zipfTesting-tps](.\zipfTesting-tps.png)![zipfTesting-latency](.\zipfTesting-latency.png)
