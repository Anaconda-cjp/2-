import matplotlib.pyplot as plt
from matplotlib import cm


def draw_bar():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False



    # 归一化

    map_vir = cm.get_cmap(name='inferno')

    fig = plt.figure()  # 调用figure创建一个绘图对象
    plt.subplot(111)


    sm = cm.ScalarMappable(cmap=plt.cm.Wistia, norm=plt.Normalize(2,10))  # norm设置最大最小值
    sm.set_array([])
    plt.colorbar(sm)


    plt.show()

draw_bar()

