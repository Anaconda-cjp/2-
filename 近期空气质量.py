import akshare as ak
date=['2021-5-23','2021-5-24','2021-5-25','2021-5-26','2021-5-27','2021-5-28','2021-5-29']
import os
os.mkdir('imgs1')
for i in date:
    air_quality_rank_df = ak.air_quality_rank(date=i)
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

    plt.title(i+'全国空气质量状况饼图')


    plt.savefig('imgs1/'+i+'全国实时空气质量状况饼图.jpg')
    plt.show()
import imageio
def create_gif(img_dir, image_list, gif_name, duration=0.05):
    frames = []
    for image_name in image_list:
        print("image_name={0} img_dir={1}".format(image_name, img_dir))
        frames.append(imageio.imread(img_dir+'/'+image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

# 生成GIF图

img_dir = './imgs1'
duration = 1.5 # 1.5秒一张
image_list = os.listdir(img_dir + '/')
gif_name = '近7天全国168个城市空气污染状况饼图'+'.gif'
create_gif(img_dir, image_list, gif_name, duration)


