# calc Tape.log tx valid rate
#import numpy as np

valid = 0
invalid = 0
tot = 0

# read from Tape.log file
file_path = "Tape.log"

# 打开文件并逐行读取内容
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        if "CommitAtPeers: " in line:
            tot += 1
        if "VALID" in line: 
            valid += 1
        elif "MVCC" in line:
            invalid += 1

print("valid: %d/%d %.2f%% invalid: %d/%d %.2f%%" % (valid, tot, valid/tot*100, invalid, tot, invalid/tot*100))

