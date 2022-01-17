# 账单 检查 计算
import csv

with open(r"C:\Users\Administrator\Desktop\新建文本文档.csv", "r+", encoding='utf-8') as f:
    datas = f.readlines()
    rows = []
    for i in datas:
        ll = i.split(' ')
        print(ll)
        rows.append(ll)
with open(r"1.csv", "w+", newline='', encoding='utf-8') as f:
    header = ['交易日期', '入帐日期', '交易描述', '交易金额', '交易货币', '入账金额', '入账货币']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
