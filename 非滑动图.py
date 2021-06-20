from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
import pyecharts.charts as pyec
from pyecharts.globals import ThemeType
'''浙江排名10 9 8 ，8 8 7，8，6'''


colors=['rgb(0,200,0)','rgb(0,200,0)','rgb(0,0,255)','rgb(0,0,0)','rgb(0,255,255)',
        'rgb(255,255,0)','rgb(255,0,255)','rgb(120,120,0)'
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

x = df1.columns.to_list()

colorList = [
'rgb(128, 128, 128)','rgb(100,0,100)'
]# 定义储存颜色的数组
tl = Timeline()
tl.add_schema(is_auto_play=False,play_interval=500,is_loop_play=False)
k=0
x=df1.columns.to_list()
print(x)
for i in range(2014,2022):
    x=df1.columns.to_list()# 获得列名
    y=get_value(df1,k)[0]
    s={'地区':x,
       'pm2.5综合指数':y}
    tem=pd.DataFrame(s)
    tem=tem.sort_values(by='pm2.5综合指数',ascending=True)

    x=tem['地区'].to_list()
    print(x)
    y=tem['pm2.5综合指数'].to_list()
    print(y)
    k=get_value(df1,k)[1]


    bar = (
        Bar(init_opts=opts.InitOpts(width='900px',height='600px',theme='dark'))
        .add_xaxis(x)

        .add_yaxis('',y,itemstyle_opts=opts.ItemStyleOpts(color='rgb(255,0,100)'),is_show_background=True,background_style='dark')


        .set_series_opts(label_opts=opts.LabelOpts(margin=0,font_size=10),
                         itemstyle_opts=opts.ItemStyleOpts(color='rgb(244,164,95)'))

        .set_global_opts(



            yaxis_opts=opts.AxisOpts(name='空气质量综合指数'),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(
                color='black',
                font_size=15,margin=0,rotate=-90,font_style='border')),


            title_opts=opts.TitleOpts("".format(i)),
            graphic_opts=[

                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=150,
                        bottom=150,
                        z=100,
                    ),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(
                                left="center", top='center', z=100
                            ),
                            graphic_shape_opts=opts.GraphicShapeOpts(
                                width=600, height=50
                            ),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="rgba(0,0,0,0.3)"
                            ),
                        ),

                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text="各省{}年空气质量综合指数".format(i),
                                font="bold 26px Microsoft YaHei",

                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="#fff"
                                ),
                            ),
                        ),
                    ],
                )
            ],
        )
    )


    tl.add(bar, "{}年".format(i))

tl.render("非滑动图最终版.html")



