import re
import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="Example script to get input arguments")
# 添加你需要的参数
parser.add_argument('--logFile', type=str, help='The log file name')
# 解析命令行参数
args = parser.parse_args()

file_path = args.logFile

# 正则表达式匹配 Time 开头的行并提取 Time 值和 Tx 数
pattern = re.compile(r'^Time\s+([\d.]+)s\s+Block\s+\d+\s+Tx\s+(\d+)')

total_tx = 0
last_time = None

with open(file_path, "r") as file:
    for line in file:
        match = pattern.match(line)
        if match:
            last_time = match.group(1)  # 获取 Time 值
            total_tx += int(match.group(2))  # 累加交易数量

if last_time:
    # tx: 40000, duration: 10.040100996s, tps: 3984.023668
    print(f"tx: {total_tx}, duration: {last_time}s, tps: {total_tx / float(last_time):.0f}")
else:
    print("No matching lines found.")
    assert False
