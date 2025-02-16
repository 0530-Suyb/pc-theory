from datetime import datetime
import re
import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="Example script to get input arguments")

# 添加你需要的参数
parser.add_argument('--logFile', type=str, help='The log file name')

# 解析命令行参数
args = parser.parse_args()

log_file = args.logFile
transactions = {}

# 正则匹配txid、事件和时间戳
pattern = re.compile(r'txid (\w+), event (CreateChaincodeProposal|CommitAtPeers: (VALID|MVCC_READ_CONFLICT)) at ([\d\-T:+.]+)')

with open(log_file, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            txid, event, _, timestamp = match.groups()
            
            # 将时间戳纳秒部分裁剪为 6 位微秒
            timestamp = re.sub(r'(\.\d{6})\d+', r'\1', timestamp)
            
            # 解析时间格式
            time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
            timestamp = datetime.strptime(timestamp, time_format)

            # print("txid:", txid, "event:", event, "timestamp:", timestamp)
            if event == "CreateChaincodeProposal":
                transactions[txid] = {"start": timestamp}
            elif event.startswith("CommitAtPeers:") and txid in transactions:
                transactions[txid]["end"] = timestamp

# 计算时间间隔
durations = []
for txid, times in transactions.items():
    if "start" in times and "end" in times:
        diff = (times["end"] - times["start"]).total_seconds()
        durations.append(diff)
        # print(f"Transaction {txid} took {diff:.9f} seconds")

# 计算平均时间
if durations:
    avg_duration = sum(durations) / len(durations)
    # print(f"Average transaction time: {avg_duration:.3f} seconds")
    print(f"{avg_duration:.3f}")
else:
    print("No valid transactions found.")
