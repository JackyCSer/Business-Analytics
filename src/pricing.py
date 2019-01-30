import pandas as pd
path = "/Users/Jacky/Downloads/再弹-在库车辆金融方案-数据快照-2019-01-21.xlsx"
path2 = "/Users/Jacky/Downloads/集采新车-不可退-2019-01-21.xlsx"

used = pd.read_excel(path);
new = pd.read_excel(path2);


# print(data.head(1000))
# for index, row in used.iterrows():
#     for index2, row2 in new.iterrows():
#         if row['x.model_name'] == row2['车型']:
#          # 相同车型比较
#
#
# # print(data.types);