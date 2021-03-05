import csv
import time
import datetime

import pandas
import requests
import json

from docutils.parsers import null


def getJson(url):
    Json = requests.get(url)
    data = json.loads(Json.text)
    return data

#按日期给数据进行排序
def classifyByTime(file,day,countryData):
    #分别是日期、中文国名，国家缩写，英文国名，地区，确诊人数，新增确诊，死亡人数，新增死亡
    Day_list = []
    chineseCountry_list = []
    country_list = []
    countryName_list = []
    region_list = []
    cases_list = []
    new_cases_list = []
    deaths_list = []
    new_deaths_list = []

    #读取运行代码时的时间，并保留年月日，时间变成8：00：00，然后扩大1000倍，因为json文件里的时间戳到毫秒，并变成字符串格式
    now_time = datetime.datetime.now()
    timeStr = datetime.datetime.strftime(now_time,'%Y-%m-%d 08:00:00')
    timeStamp = int(time.mktime(time.strptime(timeStr,'%Y-%m-%d %H:%M:%S'))*1000)
    #定一个字典，为了之后输出文件用
    JF = {"dimensions": [
         {"name": "TimeStamp", "type": "STRING"},
         {"name": "Chinese Name", "type": "STRING"},
         {"name": "English Name", "type": "STRING"},
         {"name": "State Abbreviations", "type": "STRING"},
         {"name": "Region", "type": "STRING"}],
         "metrics": [
         {"name": "New Deaths", "type": "NUMBER"},
         {"name": "Cumulative Deaths", "type": "NUMBER"},
         {"name": "New Confirmed", "type": "NUMBER"},
         {"name": "Cumulative Confirmed", "type": "NUMBER"}]}
    #创建一个时间戳日期，值为初始日期
    StampDay = day
    #判断日期是否小于今天的8：00：00，如果大于就不继续循环了
    TotalList = []
    while StampDay <= timeStamp:
        print(StampDay)
        #定义一个二维列表TotalList，以及子列表List，子列表存储每个国家的信息，二维列表存储所有子列表
        for i in range(len(file)):
            List = []
            if StampDay == file[i][0]:#时间戳是不是一样
                cN, eN = countryName(file[i][1],countryData)
                #存储csv格式
                Day_list.append(transform_time(file[i][0]))#把时间戳格式变成年月日格式
                chineseCountry_list.append(cN)#国家中文名
                countryName_list.append(eN)#国家英文名
                #1-6分别是：国家简称、地区、死亡、累计死亡、确诊、累计确诊
                country_list.append(file[i][1])
                region_list.append(file[i][2])
                new_deaths_list.append(file[i][3])
                deaths_list.append(file[i][4])
                new_cases_list.append(file[i][5])
                cases_list.append(file[i][6])
                #以字典方式，为了存json
                List.append(file[i][0])
                List.append(cN)
                List.append(eN)
                for x in range(1,7):
                    List.append(file[i][x])
                TotalList.append(List)
        StampDay = StampDay + 86400000
    JF['rows'] = TotalList  # 添加疫情数据到字典中
    #csv文件
    CF = pandas.DataFrame({'Day': Day_list,
                           'Chinese Name': chineseCountry_list,
                           'English Name': country_list,
                           'State Abbreviations': countryName_list,
                           'Region': region_list,
                           'new deaths': new_deaths_list,
                           'Cumula deaths': deaths_list,
                           'confirmed new cases': new_cases_list,
                           'Cumula confirmed cases': cases_list
                           })
    return CF,JF
#转换时间戳为年月日格式
def transform_time(timeStamp):
    timeArray = time.localtime(timeStamp / 1000)
    date = time.strftime("%Y--%m--%d", timeArray)
    return date

#匹配国家缩写，获取国家中英文名字
def countryName(name,countryData):
    ChineseName = ''
    EnglishName = ''
    for line in countryData:
        if name in line[2]:
            ChineseName = line[0]
            EnglishName = line[1].rstrip()
            print(ChineseName, EnglishName,name,line[2])
            break
    return ChineseName,EnglishName

#按国家排序
def classifyByName(file,countryData):
    #分别是日期、中文国名，国家缩写，英文国名，地区，确诊人数，新增确诊，死亡人数，新增死亡
    Day_list = []
    chineseCountry_list = []
    country_list = []
    countryName_list = []
    region_list = []
    cases_list = []
    new_cases_list = []
    deaths_list = []
    new_deaths_list = []

    #读取运行代码时的时间，并保留年月日，时间变成8：00：00，然后扩大1000倍，因为json文件里的时间戳到毫秒，并变成字符串格式
    now_time = datetime.datetime.now()
    timeStr = datetime.datetime.strftime(now_time,'%Y-%m-%d 08:00:00')
    timeStamp = int(time.mktime(time.strptime(timeStr,'%Y-%m-%d %H:%M:%S'))*1000)
    #定义一个字典，为了之后输出文件用
    JF = {"dimensions": [
         {"name": "TimeStamp", "type": "STRING"},
         {"name": "Chinese Name", "type": "STRING"},
         {"name": "English Name", "type": "STRING"},
         {"name": "State Abbreviations", "type": "STRING"},
         {"name": "Region", "type": "STRING"}],
         "metrics": [
         {"name": "New Deaths", "type": "NUMBER"},
         {"name": "Cumulative Deaths", "type": "NUMBER"},
         {"name": "New Confirmed", "type": "NUMBER"},
         {"name": "Cumulative Confirmed", "type": "NUMBER"}]}
    # 定义一个二维列表TotalList，以及子列表List，子列表存储每个国家的信息，二维列表存储所有子列表
    TotalList = []
    atateAbbreviations = ''
    for i in range(len(file)):
        List = []
        if atateAbbreviations != file[i][1]:  # 判断是不是一个国家,如果名字不一样换一个
            atateAbbreviations = file[i][1]
            cN, eN = countryName(file[i][1], countryData)
        # 存储csv格式
        Day_list.append(transform_time(file[i][0]))  # 把时间戳格式变成年月日格式
        chineseCountry_list.append(cN)  # 国家中文名
        countryName_list.append(eN)  # 国家英文名
        # 1-6分别是：国家简称、地区、死亡、累计死亡、确诊、累计确诊
        country_list.append(file[i][1])
        region_list.append(file[i][2])
        new_deaths_list.append(file[i][3])
        deaths_list.append(file[i][4])
        new_cases_list.append(file[i][5])
        cases_list.append(file[i][6])
        # 以字典方式，为了存json
        List.append(file[i][0])
        List.append(cN)
        List.append(eN)
        for x in range(1, 7):
            List.append(file[i][x])
        TotalList.append(List)

    JF['rows'] = TotalList  # 添加疫情数据到字典中
    #csv文件
    CF = pandas.DataFrame({'Day': Day_list,
                           'Chinese Name': chineseCountry_list,
                           'English Name': country_list,
                           'State Abbreviations': countryName_list,
                           'Region': region_list,
                           'new deaths': new_deaths_list,
                           'Cumula deaths': deaths_list,
                           'confirmed new cases': new_cases_list,
                           'Cumula confirmed cases': cases_list
                           })
    return CF,JF

if __name__ == '__main__':
    #打开有国家中文名和国家英文名的csv文件,并生成一个列表，如果直接用读取的csv.reader只能迭代一次
    country = open("country.csv", 'r', encoding="utf-8")
    country_data = csv.reader(country)
    countryList = []
    for line in country_data:
        countryList.append(line)
    # 从url链接里获取json文件，并在rows里获得数据
    starttime = time.time()
    url = 'https://dashboards-dev.sprinklr.com/data/9043/global-covid19-who-gis.json'
    data = getJson(url)
    rows = data['rows']
    print(len(rows))
    #开始用日期整理数据，并加入国家的中英文
    Day = 1578441600000  # 初始日期2020年1月8号
    CF,JF = classifyByName(rows,countryList)#一个csv文件，一个json文件
    CF.to_csv('ByName_COVID-19.csv')
    with open('ByName_COVID-19.json', 'w') as f:
         json.dump(JF, f,ensure_ascii=False)#最后一个参数为了避免乱码

    CF,JF = classifyByTime(rows, Day,countryList)#一个csv文件，一个json文件
    CF.to_csv('ByTime_COVID-19.csv')
    with open('ByTime_COVID-19.json', 'w') as f:
         json.dump(JF, f,ensure_ascii=False)#最后一个参数为了避免乱码






