import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex
import numpy as np
import pandas as pd
import os
from matplotlib import cm
'''生成图片文件'''
os.mkdir('imgs')


def draw_bar():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False





    # map_vir = cm.get_cmap(name='inferno')

    # fig = plt.figure()  # 调用figure创建一个绘图对象



    sm = cm.ScalarMappable(cmap=plt.cm.Wistia, norm=plt.Normalize(2,10))  # norm设置最大最小值

    plt.colorbar(sm)





plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False# 显示中文
for i in range(2014,2022):
    x=str(i)
    plt.figure(figsize=(16, 8))
    m = Basemap(
        llcrnrlon=77,
        llcrnrlat=14,
        urcrnrlon=140,
        urcrnrlat=51,
        projection='lcc',
        lat_1=33,
        lat_2=45,
        lon_0=100
    )
    m.drawcountries(linewidth=1.5)
    m.drawcoastlines()

    # 设置颜色渐变方案
    cmap=plt.cm.Wistia

    m.readshapefile('gadm36_CHN_1', 'states', drawbounds=True)
    df=pd.read_csv('2014-2021年全国各省份PM2.5指数.csv',encoding='GBK')

    # 画渐变色条
    draw_bar()




    new_index_list = []
    for i in df["地区"]:

        new_index_list.append(i)
    new_index = {"region": new_index_list}
    new_index = pd.DataFrame(new_index)
    df = pd.concat([df,new_index], axis=1)
    df = df.drop(["地区"], axis=1)
    df.set_index("region", inplace=True)
    # print(df)


    # 初始化地区列表
    statements = []
    colors = {}
    vmax = 10
    vmin = 2
    # 获取每个实例,并转换成颜色值

    provinces = m.states_info
    # 转换成 dataframe 去掉 行标0,1,2.。。


    print(df)

    print(x)
    for each_province in provinces:
        province_name = each_province['NL_NAME_1']


        p = province_name.split('|')
        if len(p) > 1:
            s = p[1]
        else:
            s = p[0]

        s = s[:2]
        if s == '黑龍':
            s = '黑龙江'
        if s == '内蒙':
            s = '内蒙古'
        if s=='宁夏回族自治区':
            s='宁夏'
        if s=='内蒙古自治区':
            s='内蒙古'

        statements.append(s)

        if s in df.index:
            pop = df['{}年'.format(x)][s]
            colors[s] = cmap(np.sqrt((pop - vmin) / (vmax - vmin)))[:3]
        else:
            colors[s]=cmap(0,0,0)




    ax = plt.gca()

    for nshape, seg in enumerate(m.states):
        color = rgb2hex(colors[statements[nshape]])
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)
    plt.title(x+'年全国各省份PM2.5综合指数')
    # plt.show()
    plt.savefig('imgs/{}年中国各省份PM2.5综合指数图.jpg'.format(x))


import imageio
def create_gif(img_dir, image_list, gif_name, duration=0.05):
    frames = []
    for image_name in image_list:
        print("image_name={0} img_dir={1}".format(image_name, img_dir))
        frames.append(imageio.imread(img_dir+'/'+image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

# 生成GIF图

img_dir = './imgs'
duration = 1.5 # 1.5秒一张
image_list = os.listdir(img_dir + '/')
gif_name = '2014-2021年我国各省份PM2.5综合指数图'+'.gif'
create_gif(img_dir, image_list, gif_name, duration)
