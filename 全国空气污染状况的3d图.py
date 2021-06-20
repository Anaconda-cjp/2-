from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
import pyecharts.charts as pyec
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode
'''浙江排名10 9 8 ，8 8 7，8，6'''
example_data1 = [
    ("北京",[116.4,39.8,780]),
    ("天津", [117.4219, 39.4189, 832]),
    ("河北", [114.4995, 38.1006, 890]),
    ("山西", [112.3352, 37.9413, 544]),
    ("内蒙古", [110.3467, 41.4899, 690]),
    ("吉林", [125.8154, 44.2584, 641]),
    ("辽宁", [123.1238, 42.1216, 588]),
    ("黑龙江", [127.9688, 45.368, 693]),
    ("上海", [121.4648, 31.2891, 519]),
    ("江苏", [118.8062, 31.9208, 622]),
    ("浙江", [119.5313, 29.8773, 523]),
    ("安徽", [117.29, 32.0581, 385]),
    ("福建", [119.4543, 25.9222, 394]),
    ("江西", [116.0046, 28.6633, 553]),
    ("山东", [117.1582, 36.8701, 843]),
    ("河南", [113.4668, 34.6234, 776]),
    ("湖北", [114.3896, 30.6628, 557]),
    ("湖南", [113.0823, 28.2568, 593]),
    ("广东",[114.5,23,465]),
    ("广西", [108.479, 23.1152, 491]),
    ("海南", [110.3893, 19.8516, 260]),
    ("重庆", [108.384366, 30.439702, 578]),
    ("四川", [103.9526, 30.7617, 664]),
    ("贵州", [106.6992, 26.7682, 429]),
    ("云南",[101,23,407]),
    ("西藏", [91.11, 29.97, 345]),
    ("陕西", [109.1162, 34.2004, 687]),
    ("甘肃", [103.5901, 36.3043, 609]),
    ("青海", [101.4038, 36.8207, 598]),
    ("宁夏", [106.3586, 38.1775, 604]),

    ("新疆", [87.9236, 43.5883, 728]),

]



import pandas as pd

df=pd.read_csv('2014-2021年全国各省份PM2.5指数.csv',encoding='GBK',index_col=0)
print(df)



'''实现dataframe的转置！！！！！！！！！'''
# df.values.T为了读取的时候数据格式 先变成转置后的样子  之后再把行标列标转换一下！
df1=pd.DataFrame(df.values.T,index=df.columns,columns=df.index)
print(df1)
# 获取y轴
def get_value(df,k):
    data=df.iloc[k].to_list()
    k=k+1
    return data,k












k = 0
example_data = []
for i2 in range(2014,2022):

    y = get_value(df1 * 100, k)[0]
    k += 1
    print(y)# 获得对应污染值
    i1 = 0
    list1 = []# 储存需要的列表数据
    for i in example_data1:
        list(i)
        i[1][2] = y[i1]# 修改列表的最后一个数据
        i1 += 1
        list1.append(tuple(i))

    example_data=list1

    c = (
        Map3D()
            .add_schema(
            itemstyle_opts=opts.ItemStyleOpts(
                color="rgb(5,101,123)",
                opacity=1,
                border_width=0.8,
                border_color="rgb(62,215,213)",
            ),
            map3d_label=opts.Map3DLabelOpts(
                is_show=False,
                formatter=JsCode("function(data){return data.name + " " + data.value[2];}"),
            ),
            emphasis_label_opts=opts.LabelOpts(
                is_show=False,
                color="#fff",
                font_size=10,
                background_color="rgba(0,23,11,0)",
            ),
            light_opts=opts.Map3DLightOpts(
                main_color="#99ffff",
                main_intensity=1.2,
                main_shadow_quality="high",
                is_main_shadow=False,
                main_beta=10,
                ambient_intensity=0.3,
            ),
        )
            .add(
            series_name="bar3D",

            data_pair=example_data,
            type_=ChartType.BAR3D,
            bar_size=1,
            min_height=2,

            shading="lambert",
            label_opts=opts.LabelOpts(
                is_show=False,
                formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
            ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title=str(i2)+"年全国各省空气污染状况立体图"))
            .render(str(i2)+"年全国各省空气污染状况立体图.html")
    )











