# -*- coding: utf-8 -*-

import os
import pandas as pd

# 获取当前路径
current_path = os.getcwd()

# 获取当前路径下所有CSV文件的文件名
csv_files = [f for f in os.listdir(current_path) if f.endswith('.csv')]

# 指定要提取的列和行范围
# target_column = 'mt'  # 假设提取'mt'列
target_column = 1  # 假设提取'mt'列
start_row = 2  # 假设要提取从第3行开始
end_row = 6  # 假设要提取到第6行结束
sum_data=[]
# 遍历每个CSV文件，提取数据并保存到新的CSV文件中
for csv_file in csv_files:
    df = pd.read_csv(os.path.join(current_path, csv_file),error_bad_lines=False,encoding='utf-8')
    # print(df)
    # quit()
    # 提取指定列、行范围的数据
    # extracted_data = df.loc[start_row:end_row, target_column]
    extracted_data = df.iloc[start_row:end_row, target_column] # 区间是左闭右开
    # 添加数据
    sum_data.append(extracted_data)
df2 = pd.concat(sum_data,axis=1)
# df3 = pd.pivot(df2)
df3 = df2.T
# print(df3)
#     # 保存提取的数据到新的CSV文件中
# quit()
new_csv_file = 'sum.csv'
# new_csv_file = f"extracted_{csv_file}"
df3.to_csv(os.path.join(current_path, new_csv_file), index=True, header = False)