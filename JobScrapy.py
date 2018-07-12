#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/7/12 16:46
# 采集出城市(北京) 职位(python)的要求信息（信息数量不少于300条件）
# 采集出的信息有：a. 薪资b. 公司名称c. 公司地址d. 职位描述
# 把采集到的信息存放到1个txt中，格式不定，但要能够分清楚采集到的不同的职位
# 实现难点：如何自动翻页, 如何加入 职位 关键词搜索; 如何判断 职位 信息 已采集完

import requests
from bs4 import BeautifulSoup as bs
import re
import urllib
import os
import sys
import json

# 城市, 职位, 页码
city = '成都'
kd = '测试工程师'
page = 2


# 第一步：
def jobScrapy(city, kd, page):
    # url = "https://www.lagou.com/jobs/positionAjax.json"
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=' + city + '&needAddtionalResult=false'
    # querystring = {"city":"北京","needAddtionalResult":"false"}
    querystring = {"first": "true", "pn": page, "kd": kd}
    payload = ""
    headers = {
        'origin': "https://www.lagou.com",
        'x-anit-forge-code': "0",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'x-devtools-emulate-network-conditions-client-id': "BC7D1E21EDAE5E8F115549218ACFC10F",
        'x-requested-with': "XMLHttpRequest",
        'x-anit-forge-token': "None",
        'referer': "https://www.lagou.com/jobs/list_python?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "user_trace_token=20180511091318-7d503eb7-54b8-11e8-9487-525400f775ce; LGUID=20180511091318-7d50418f-54b8-11e8-9487-525400f775ce; _ga=GA1.2.285704315.1526001199; LG_LOGIN_USER_ID=1fa8a1cf4ec2cc008e582b4292b1f8bc15ae48ef524e925587557becece6a284; WEBTJ-ID=20180712162556-1648d98c4b4d6-0ed6cfd4a1f2e8-5e442e19-1049088-1648d98c4b81e1; _gid=GA1.2.1305151322.1531383957; JSESSIONID=ABAAABAAADEAAFI085E842619CBF0BC790816136424D89C; LGSID=20180712162543-2b1a8b2c-85ad-11e8-95d7-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531383957,1531383964; X_HTTP_TOKEN=a8e39788d98cbc77478e663754825b2e; SEARCH_ID=4688a5641a5a4f46a997156f7aaf4794; TG-TRACK-CODE=search_code; LGRID=20180712165454-3e94e631-85b1-11e8-95d9-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531385715; index_location_city=%E5%85%A8%E5%9B%BD; isCloseNotice=0",
        'cache-control': "no-cache",
        'postman-token': "9f3b9696-55e1-54b8-ea4a-f4365eff9cea"
    }
    response = requests.request("POST", url, headers=headers, params=querystring)
    print(response.text)
    res = response.text
    return res


# 第二步：采集过程
def jobCollect(positionID):
    url = 'https://www.lagou.com/jobs/'+positionID+'.html'
    response = requests.request(url)
    response.raise_for_status()
    res = response.text


# 第三步：信息整合与输出
def jobOuput():
    print()


if __name__ == '__main__':
    for i in range(1, 30):
        jobScrapy(city, kd, i)

