import akshare as ak
import pandas as pd
'''月'''
# air_quality_hist_df = ak.air_quality_hist(city="北京", period="month", start_date="2019-04-25", end_date="2020-04-27")
# print(air_quality_hist_df)

'''具体某年'''
import akshare as ak
years=['2014','2015','2016','2017','2018','2019','2020','2021']
sum=0
for i in years:

    sum=0
    air_quality_rank_df = ak.air_quality_rank(date=i)
    # print(air_quality_rank_df.loc[air_quality_rank_df['省份']=='河北'])
    y=0
    for x in air_quality_rank_df.loc[air_quality_rank_df['省份']=='新疆','综合指数']:
        # print(x)
        sum+=x
        y+=1
    average=sum/y
    print('\n新疆平均值:',average)
    air_quality_rank_df.to_csv('文件名.csv',mode='a',header=True,index=False)

# air_quality_rank_df.to_csv('文件名.csv',mode='w',header=True,index=False)
# x=air_quality_rank_df['省份']
# print(x.drop_duplicates())

# from csv import reader
# opened_file = open('文件名.csv')
# read_file = reader(opened_file)
# test = list(read_file)# 读取csv并转换为列表(方便处理)







