import pandas as pd
import datetime
import numpy as np

# 读取数据
CSV_FILE_PATH3 = "C:\\math\\data\\data3.csv"
df3 = pd.read_csv(CSV_FILE_PATH3)

# 选取状态是5（审核通过）的促销记录
clean_data = df3[df3['state'].isin([5])].reset_index(drop=True)

data = clean_data[['id', 'sku_id', 'total_difference', 'promotion_rate', 'begin_time.1', 'time']]
data.pop('id')
data['begin_time'] = pd.to_datetime(data['begin_time.1'])
data.pop('begin_time.1')
# 设定每天的时间差
delta = datetime.timedelta(days=1)

df_temp = pd.DataFrame(columns=['sku_id', 'total_difference', 'promotion_rate', 'time', 'begin_time'])
for i in data.index:
    temp_row = data.loc[i]
    if temp_row[3] != 0:
        for j in range(temp_row[3]):
            temp_row[4] = temp_row[4] + delta
            df_temp = df_temp.append(temp_row)

data_by_day = data.append(df_temp, ignore_index=True)
result1 = data_by_day.groupby('begin_time').sum()
total_difference_by_day = {i: j for i, j in zip(result1.index, result1['total_difference'])}

weight = np.zeros(data_by_day.shape[0])

for i in data_by_day.index:
    temp = data_by_day.loc[i]
    if total_difference_by_day[temp[4]] == 0.0:
        weight[i] = 0
    else:
        weight[i] = temp[1] / total_difference_by_day[temp[4]]

rate = np.zeros(data_by_day.shape[0])

for i in data_by_day.index:
    temp = data_by_day.loc[i]
    rate[i] = temp[2] * weight[i]

data_by_day.insert(0, 'weight', weight)
data_by_day.insert(0, 'rate', rate)
result2 = data_by_day.groupby('begin_time').sum()

result2.to_csv("C:\\math\\data\\result2.csv", encoding='UTF-8')
# A:0 , B:0~0.25, C:0.25~0.5, D:0.5~0.75, E:0.75~1
static = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
for i in result2['rate']:
    if i == 0.0:
        static['A'] = static['A'] + 1
    elif 0.0 < i < 0.25:
        static['B'] = static['B'] + 1
    elif 0.25 < i < 0.5:
        static['C'] = static['C'] + 1
    elif 0.5 < i < 0.75:
        static['D'] = static['D'] + 1
    elif 0.75 < i <= 1:
        static['E'] = static['E'] + 1

