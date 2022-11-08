# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:33:57 2022

@author: MYCOM
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path = "chipotle.tsv"
chipo = pd.read_csv(file_path, sep = "\t")

print(chipo.shape)
print("=" * 30)
print(chipo.info())

chipo.head(10)
print("=" * 30)

chipo.tail(10)
print("=" * 30)

print(chipo.columns)
print("=" * 30)

print(chipo.index)
print("=" * 30)

# order_id는 숫자의 의미를 가지지 않기 때문에 str로 변환
chipo["order_id"] = chipo["order_id"].astype(str)
print(chipo.describe())

# 가장 많이 주문한 아이템 TOP 10을 출력
item_count = chipo['item_name'].value_counts()[:10]
#print(item_count)
for idx, (val,cnt) in enumerate(item_count.iteritems(),1):
    print("Top", idx, ":", val, cnt)

# 아이템별 주문 횟수를 출력
order_count = chipo.groupby('item_name')['order_id'].count()
order_count = order_count[:10]
print(order_count)

# 아이템별 주문 총량을 계산
item_quantity = chipo.groupby('item_name')['quantity'].sum()
item_quantity = item_quantity[:10]
print(item_quantity)

item_name_list = item_quantity.index.tolist()
#x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()
plt.figure(figsize=(30,10))
#plt.bar(x_pos, order_cnt, align="center")
plt.bar(item_name_list, order_cnt, align="center")
plt.ylabel('orderd_item_count')
plt.title("Distribution of all orderd item")
plt.show()

print(chipo.info())
print("-" * 30)
print(chipo['item_price'].head())

def to_float(n) :
    n = n.replace("$", "")
    n = float(n)
    return n

chipo["item_price"] = chipo["item_price"].apply(to_float)
print(chipo["item_price"].head())
print("-" * 30)
print(chipo.info())
print("-" * 30)

# 주문당 합계 계산금액을 출력합니다.
print(chipo.groupby("order_id")["item_price"].sum())

# 주문당 평균 계산금액을 출력합니다.
print(chipo.groupby("order_id")["item_price"].mean())

# 주문당 평균 계산금액을 출력합니다.
print(chipo.groupby("order_id")["item_price"].sum().mean())

# 한 주문에 10달러 이상 지불한 주문번호(id)를 출력합니다.
chipo_orderid_group = chipo.groupby('order_id').sum()
results = chipo_orderid_group[chipo_orderid_group.item_price >= 10]
print(results)

# 각 아이템의 가격을 계산합니다.
one_item = chipo[chipo.quantity == 1]
print(one_item.head(10))
print("-" * 30)

per_item = one_item.groupby("item_name").min()
print(per_item.head(10))
print("-" * 30)

per_item = per_item.sort_values(by = "item_price", ascending = False)
print(per_item.head())
print("-" * 30)

item_name_list = per_item.index.tolist()
#x_pos = np.arange(len(item_name_list))
item_price = per_item["item_price"].values.tolist()
plt.figure(figsize=(30,10))
plt.xticks(rotation = 90)
#plt.bar(x_pos, order_cnt, align="center")
plt.bar(item_name_list, item_price, align="center")
plt.ylabel('item_price ($)')
plt.title("Distribution of all orderd item")
plt.show()

# temp = chip.groupby('order_id').sum().sort_values(by = "item_price", ascending= False)[:5] 
temp = chipo.groupby('order_id').sum()
print(temp)
print("-" * 30)
temp = temp.sort_values(by = "item_price", ascending= False)
print(temp)
print("-" * 30)
tmep = temp[:5]
print(temp)
print("-" * 30)

item_list = chipo[chipo["item_name"] == "chicken Bowl"]
print(item_list)












