import re

# 获取学费当中的最大值
def getTuition_fee(str):
    allfee = re.findall(r'\d+,\d+', str)
    # print(allfee)
    for index in range(len(allfee)):
        fee = allfee[index].split(",")
        allfee[index] = ''.join(fee)
        # print(allfee[index])
    # print(allfee)
    maxfee = 0
    for fee in allfee:
        if int(fee) >= maxfee:
            maxfee = int(fee)
    return maxfee

def getT_fee(str):
    allfee = re.findall(r'\d{5}', str)
    maxfee = 0
    for fee in allfee:
        if int(fee) >= maxfee:
            maxfee = int(fee)
    return maxfee