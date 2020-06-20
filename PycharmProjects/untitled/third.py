import pandas as pd
import matplotlib.pyplot as plt


CSV_FILE_PATH1 = "C:\\math\\data\\result1.csv"
CSV_FILE_PATH2 = "C:\\math\\data\\result2.csv"
df1 = pd.read_csv(CSV_FILE_PATH1)
df2 = pd.read_csv(CSV_FILE_PATH2)

df1 = df1.set_index('create_dt')
df2 = df2.set_index('begin_time')

data = pd.concat([df2, df1], axis=1, join='inner')
clear_data = data[['rate', 'sku_sale_prc', 'profit_rate']]

plt.scatter(clear_data['rate'], clear_data['sku_sale_prc'])

plt.scatter(clear_data['rate'], clear_data['profit_rate'])

