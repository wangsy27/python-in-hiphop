# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import numpy as np
import os
from xpinyin import Pinyin

p = Pinyin()
song = []
words = []
py = {}

cars = {'宝马':0,'奔驰':0,'兰博基尼':0,'法拉利':0,'宾利':0,'凯迪拉克':0,'路虎':0}
drinks = {'香槟':0, '啤酒':0, '红酒':0,'伏特加':0,'威士忌':0}
cloths = {'金链':0, '帽子':0,'裤子':0,'戒指':0,'衣服':0}

RhymeIndex = [('1', ['a', 'ia', 'ua']), ('2', ['ai', 'uai']), ('3', ['an', 'ian', 'uan']),
              ('4', ['ang', 'iang', 'uang']), ('5', ['ao', 'iao']), ('6', ['e', 'o', 'uo']), ('7', ['ei', 'ui']),
              ('8', ['en', 'in', 'un']), ('9', ['eng', 'ing', 'ong', 'iong']), ('10', ['er']), ('11', ['i']),
              ('12', ['ie', 'ye']), ('13', ['ou', 'iu']), ('14', ['u']), ('16', ['ue']), ('15', ['qu', 'xu', 'yu'])]
 
RhymeDct = {'ui': '7', 'uan': '3', 'ian': '3', 'iu': '13', 'en': '8', 'ue': '16', 'ing': '9', 'a': '1', 'ei': '7',
            'eng': '9', 'uo': '6', 'ye': '12', 'in': '8', 'ou': '13', 'ao': '5', 'uang': '4', 'ong': '9', 'ang': '4',
            'ai': '2', 'ua': '1', 'uai': '2', 'an': '3', 'iao': '5', 'ia': '1', 'ie': '12', 'iong': '9', 'i': '11',
            'er': '10', 'e': '6', 'u': '14', 'un': '8', 'iang': '4', 'o': '6', 'qu': '15', 'xu': '15', 'yu': '15'}

def EachFile(filepath):
	pathDir = os.listdir(filepath)   #获取当前路径下的文件名，返回list
	for s in pathDir:
		newDir=os.path.join(filepath,s)   #将文件名写入到当前文件路径后面
		newFile = os.listdir(newDir)
		for f in newFile:
			fileDir = os.path.join(newDir,f)
			if os.path.splitext(fileDir)[1]==".txt":  #判断是否是txt
				readFile(fileDir)
				pass
			else:
				break

def readFile(filepath):            #控制数据存入不同的list
	with open(filepath,'r', encoding ='utf-8') as f:
		lines = f.readline()
		for line in lines:
			song.append(line)
	for line in open(filepath, encoding='utf-8'):
		temp = line.strip()
		tags = jieba.analyse.extract_tags(temp)
		for t in tags:
			words.append(t)
        

# 制作词云
def Make_wordcloud():
	lyrics = " ".join(words)
	temp = " ".join(jieba.cut(lyrics))
	exclude={'我们','你们','他们','它们','因为','因而','所以','如果','那么',\
		'如此','只是','但是','就是','这是','那是','而是','而且','虽然',\
		'这些','那些','有些','然后','已经','于是','一种','一个','一样','时候',\
	'没有','什么','这样','这种','这里','不会','一些','这个','仍然','不是',\
	'自己','到底','可以','看到','那儿','问题','一会儿','一点','现在','两个',\
		'三个','一场','想要 ','不想','为了','怎么','还是','不要','我会','需要'\
		'不用','觉得','知道','需要','真的','能够','像是','变成','but','想要','只有'\
		'开始','一切','所有','一起','不能','就算','最后','感觉','继续','oh','no'\
		'还有','可能','不用','开始','只有','yeah','一定','变得','全部','每天','永远'\
		'like','喜欢','like','一直','每个','永远','还有'
		}
	#mask = imageio.imread('rap.jpg')
	wc = WordCloud(font_path='./simkai.ttf',stopwords = exclude).generate(temp)
	#plt.imshow(wc)
	#plt.show()
	wc.to_file('result_cloud.jpg')

#rapper们最喜欢喝的酒
def drink():
    for word in words:
        for k in drinks:
            if word == k:
                drinks[k] = drinks[k] + 1
    #print(cars)
    
    plt.rcParams['font.sans-serif']=['kaiti']
    plt.rcParams['font.serif'] = ['kaiti']
    plt.rcParams['axes.unicode_minus']=False
    name = []
    count = []
    for k in drinks:
        name.append(k)
        count.append(drinks[k])
    plt.barh(name,count)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=15)
    plt.title('rapper最爱喝的酒',fontsize=30)
    plt.savefig('drinks.jpg')
    plt.show()

#rapper们最喜欢开的车
def car():
    for word in words:
        for k in cars:
            if word == k:
                cars[k] = cars[k] + 1
    #print(cars)
    plt.rcParams['font.sans-serif']=['kaiti']
    plt.rcParams['font.serif'] = ['kaiti']
    plt.rcParams['axes.unicode_minus']=False
    name = []
    count = []
    for k in cars:
        name.append(k)
        count.append(cars[k])
    plt.barh(name,count)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=10)
    plt.title('rapper最爱开的车',fontsize=30)
    plt.savefig('cars.jpg')
    plt.show()

#rapper最爱穿的东西
def cloth():
    for word in words:
        for k in cloths:
            if word == k:
                cloths[k] = cloths[k] + 1
    #print(cars)
    plt.rcParams['font.sans-serif']=['kaiti']
    plt.rcParams['font.serif'] = ['kaiti']
    plt.rcParams['axes.unicode_minus']=False
    name = []
    count = []
    for k in cloths:
        name.append(k)
        count.append(cloths[k])
    plt.barh(name,count)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.title('rapper最爱穿的东西',fontsize=30)
    plt.savefig('cloths.jpg')
    plt.show()

# 简单的情感分析
def Get_Emotion():
	lyrics = song
	marks_list = []
	for lyric in lyrics:
		lyric = lyric.strip()
		if not lyric:
			continue
		mark = SnowNLP(lyric)
		marks_list.append(mark.sentiments)
	plt.hist(marks_list, bins=np.arange(0, 1, 0.02))
	plt.title('rapper的情感分析',fontsize=30)
	plt.savefig('emotion.jpg')
	plt.show()

#把中文转成拼音保存起来
def Analysis_words(words):
    word_py =p.get_pinyin((u'{}'.format(words)))
    lst_words = word_py.split('-')
    r = []
    #找出和拼音表里的拼音一样的两个字
    for i in lst_words:
        while True:
            if not i:
                break
            token = RhymeDct.get(i, None)#字典返回的数字
            if token:
                r.append(token)
                break
            i = i[1:]
    if len(r) == len(words): #返回标号
        return '-'.join(r)

#找出押韵的单词
def Getkeyword():
    with open('keyword.txt','a') as f:
        f.write("[")
        for word in words:
            if len(word) == 2:
                if Analysis_words(word)!=None:
                    f.write("{'"+Analysis_words(word)+"':'"+word+"'},")
                    if Analysis_words(word) not in py.keys():
                        py[Analysis_words(word)]=1
                    else:
                        py[Analysis_words(word)]=py[Analysis_words(word)]+1
        f.write("]")
        f.close()

def pinyin():
    p = {}
    p = sorted(py.items(), key=lambda x: x[1], reverse=True)
    name = ['i-i','i-an','ng-i','an-i','n-o','o-i','an-an','u-i','ng-ng','an-ng']
    number = []
    for i,(k,v) in enumerate(p):
        if i in range(0,10):
            print((k,v))
            number.append(v)
    plt.barh(name,number)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title('rapper的韵脚分析',fontsize=30)
    plt.savefig('yunjiao.jpg')
    plt.show()
    
#找到次数最多的前20个词用饼状图输出
def Findkey(str):
    result={}
    with open('keyword.txt', 'r') as f:
        # print(f.readlines())
        list=eval(f.readlines()[0])
        for item in list:
            if item.get(str):
                key=item.get(str)
                number=result.get(key)
                #如果一个词出现多次，进行次数累加，用来表示频次
                if number !=None and number>=1:
                    result[key]=number+1
                else:
                    result.update({key:1})
        f.close()
        #按次数从大到小排序
        p = {}
        p = sorted(result.items(), key=lambda x: x[1], reverse=True)
        for i, (k, v) in enumerate(p):
            if i in range(1, 51):
                print(k)
    plt.rcParams['font.sans-serif'] = ['kaiti']
    plt.rcParams['font.serif'] = ['kaiti']
    labels=[]
    sizes=[]
    count = -1
    for k, v in p:
        count = count + 1
        if count == 0:
            continue
        labels.append(k)
        sizes.append(v)
        if count == 10:
            break
    plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
    plt.axis('equal')   # 设置x，y轴刻度一致，保证饼图是圆的
    plt.savefig('result.jpg')
    plt.show()


if __name__ == '__main__':
	# GetWordFrequency()
	# make_wordcloud()
	EachFile('C:/Users/25030/Desktop/python/python大作业/rap歌词')
	#print(words)
	#print(song)
	#cloth()
	#drink()
	#car()
	#Make_wordcloud()
	#Get_Emotion()
	Getkeyword()
	#pinyin()
	key=input("请输入关键词:")
	str = Analysis_words(key)
	print("匹配押韵的词：")
	Findkey(str)
