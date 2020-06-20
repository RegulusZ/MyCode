import pandas as pd
from random import uniform
import numpy as np
import datetime
# 读入数据表
CSV_FILE_PATH1 = "C:\\math\\data\\data1.csv"
CSV_FILE_PATH2 = "C:\\math\\data\\data2.csv"
CSV_FILE_PATH3 = "C:\\math\\data\\data3.csv"
CSV_FILE_PATH4 = "C:\\math\\data\\data4.csv"
df1 = pd.read_csv(CSV_FILE_PATH1)
df2 = pd.read_csv(CSV_FILE_PATH2)
df3 = pd.read_csv(CSV_FILE_PATH3)
df4 = pd.read_csv(CSV_FILE_PATH4)
# 合并数据表，120万行
df = df1.append(df2, ignore_index=True)
# 删除is_finished列为0的行，剩110万行,作为清洗后数据
clean_data = df[~df['is_finished'].isin([0])].reset_index(drop=True)
# 商品种类
category = df4

category_dict = {i: j for i, j in zip(category['sku_id'], category['first_category_id'])}
first_category = np.zeros(clean_data.shape[0])
for i in clean_data.index:
    temp = clean_data.loc[i]
    try:
        first_category[i] = category_dict[temp[2]]
    except:
        pass

# 成本价不为0的商品销售记录
cost_not_null = clean_data[~clean_data['sku_cost_prc'].isin([0])]

# 成本价不为0的商品历史均价
mean_cost_not_null = cost_not_null.groupby('sku_id').mean()

# 建立成本均价字典，方面后续取值
mean_cost_dict = {i: j for i, j in zip(mean_cost_not_null.index, mean_cost_not_null['sku_cost_prc'])}

# sku_cost记录成本价
sku_cost = np.zeros(clean_data.shape[0])
for i in clean_data.index:
    temp = clean_data.loc[i]
    if temp[8] == 0.0:
        try:
            sku_cost[i] = mean_cost_dict[temp[2]]
        except:
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
# 导入大类信息到数据表中
clean_data.insert(0, 'first_category', first_category)

result_by_category = clean_data.groupby(['first_category', 'create_dt']).sum()

# 大类信息集
first_category_set = set(list(clean_data['first_category']))

# 按大类计算折扣力度
clean_data1 = df3[df3['state'].isin([5])].reset_index(drop=True)
clean_data1 = clean_data1[['sku_id', 'total_difference', 'promotion_rate', 'begin_time.1', 'time']]
clean_data1['begin_time'] = pd.to_datetime(clean_data1['begin_time.1'])
clean_data1.pop('begin_time.1')

first_category = np.zeros(clean_data1.shape[0])
for i in clean_data1.index:
    temp = clean_data1.loc[i]
    try:
        first_category[i] = category_dict[temp[0]]
    except:
        pass

clean_data1.insert(0, 'first_category', first_category)

delta = datetime.timedelta(days=1)
df_temp = pd.DataFrame(columns=['first_category', 'sku_id', 'total_difference', 'promotion_rate', 'time', 'begin_time'])
for i in clean_data1.index:
    temp_row = clean_data1.loc[i]
    if temp_row[4] != 0:
        for j in range(temp_row[4]):
            temp_row[5] = temp_row[5] + delta
            df_temp = df_temp.append(temp_row)

