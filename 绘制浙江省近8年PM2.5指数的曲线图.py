import matplotlib.pyplot as plt
from pandas import Series
pm=[5.237,4.848,4.397,4.33,3.7,3.74,3.32,3.52]
index=['2014','2015','2016','2017','2018','2019','2020','2021']
data=Series(pm,index=index)# 浙江
pm1=[7.8,7.41,6.98,5.97,4.99,4.69,4.09,4.32]
data1=Series(pm1,index=index)# 北京

fig=plt.figure(figsize=(6,6),facecolor='lightcyan')
ax=plt.subplot(111, facecolor='moccasin')

ax.plot(data,color='green',label='浙江',linestyle='--',marker='+',markersize=10)
ax.plot(data1,color='red',label='北京',linestyle='--',marker='+',markersize=10)


plt.legend()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
plt.title('2014-2021年北京和浙江空气质量综合指数比较图')
# plt.show()
plt.savefig('2014-2021年北京和浙江空气质量综合指数比较图.jpg')

