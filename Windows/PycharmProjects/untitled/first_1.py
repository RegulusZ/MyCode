import pandas as pd
from random import uniform
import numpy as np

# 读入数据表
CSV_FILE_PATH1 = "C:\\math\\data\\data1.csv"
CSV_FILE_PATH2 = "C:\\math\\data\\data2.csv"
CSV_FILE_PATH4 = "C:\\math\\data\\data4.csv"

df1 = pd.read_csv(CSV_FILE_PATH1)
df2 = pd.read_csv(CSV_FILE_PATH2)
df4 = pd.read_csv(CSV_FILE_PATH4)

# 合并数据表，120万行
df = df1.append(df2, ignore_index=True)

# 删除is_finished列为0的行，剩110万行,作为清洗后数据
clean_data = df[~df['is_finished'].isin([0])].reset_index(drop=True)

# 商品种类
category = df4

# 成本价为0的商品销售记录
cost_null = clean_data[clean_data['sku_cost_prc'].isin([0])]

# 成本价不为0的商品销售记录
cost_not_null = clean_data[~clean_data['sku_cost_prc'].isin([0])]

# 成本价不为0的商品历史均价
mean_cost_not_null = cost_not_null.groupby('sku_id').mean()

# sku_cost记录成本价
sku_cost = np.zeros(clean_data.shape[0])
for i in clean_data.index:
    temp = clean_data.loc[i]
    if temp[8] == 0.0:
        sku_cost[i] = temp[7]/(1 + uniform(0.2, 0.4))
    else:
        sku_cost[i] = temp[8]

# 导入成本价到数据表中
clean_data.pop('sku_cost_prc')
clean_data.insert(0, 'sku_cost_prc', sku_cost)

# 计算每天每个商品的利润
profit = np.zeros(clean_data.shape[0])
for i in clean_data.index:
    temp = clean_data.loc[i]
    profit[i] = (temp[8] - temp[0]) * temp[6]

# 导入利润到数据表中
clean_data.insert(0, 'profit', profit)

# 对每天的利润求和
result = clean_data.groupby('create_dt').sum()

# 导出到结果表
result.to_csv("C:\\math\\data\\result1.csv", encoding='UTF-8')


