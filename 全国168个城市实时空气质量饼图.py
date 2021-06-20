import akshare as ak
air_quality_rank_df = ak.air_quality_rank(date="实时")
# 具体某一天 改成date='2021-4-5'这样就行
print(air_quality_rank_df)
import matplotlib.pyplot as plt
s1=0
s2=0
s3=0
for x in air_quality_rank_df['空气质量']:
    print(x)
    if x=='轻度污染':
        s1+=1
    if x=='良':
        s2+=1
    if x=='优':
        s3+=1

labels=['轻度污染','良','优']
values=[s1,s2,s3]
colors=['yellow','lightgreen','green']
plt.pie(values,labels=labels,colors=colors,startangle=60,shadow=True,autopct='%1.1f%%')

plt.title('全国实时空气质量状况饼图')


plt.savefig('全国实时空气质量状况饼图.jpg')
plt.show()

