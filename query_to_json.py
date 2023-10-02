# -*- coding: utf-8 -*-
# Splitting the text using the specified delimiter
import queue

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import pandas as pd
import os
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
#AIzaSyABEdo1vb3VQJfwMU6NmqV239-H4vsfC-c
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import urllib.request
import json,re,string

import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# 启动Chrome浏览器
# driver = webdriver.Chrome(executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")  # 修改为你的chromedriver的实际路径
desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出

"""
cd C:\Program Files\Google\Chrome\Application
chrome.exe --remote-debugging-port=9222 --disable-web-security --user-data-dir=remote-profile   

set kinds of info quelle
https://programmablesearchengine.google.com/controlpanel/overview?cx=e1a862c0bafc544f5&hl=zh-cn
"""
import time

import requests
import json

url_processed_list = []
from selenium_basic_func import *
def url_web(query_input,url_num=100):

    query_variable = query_input.replace(' ',"+")

    # 定义原始 URL
    url = "https://www.google.com/search?q=Technical+map-making+errors+site%3A*.apnews.com+OR+site%3Awww.reuters.com+OR+site%3Awww.theguardian.com+OR+site%3Awww.bbc.com%2Fnews+OR+site%3Awww.cnn.com+OR+site%3A*.techcrunch.com"

    new_url = url.replace("Technical+map-making+errors", query_variable)

    driver.get(new_url)
    # 输出所有的链接
    # for element in elements:
        # print(element.get_attribute('href'))
    allowed_domains = [
        "apnews.com",
        "reuters.com",
        "theguardian.com",
        "bbc.com",
        "cnn.com",
        "techcrunch.com"
    ]
    url_list_web=[]
    # 输出所有的允许的链接
    length_url_list=0

    while True:
        length_url_list=len(url_list_web)
        elements = driver.find_elements_by_xpath('//*[@href]')

        for element in elements:
            href = element.get_attribute('href')
            domain = urlparse(href).netloc

            # 检查链接的域名是否在允许的域名列表中
            if any(allowed_domain in domain for allowed_domain in allowed_domains):
                if href not in url_list_web:
                    url_list_web.append(href)
        print(len(url_list_web))

        if len(url_list_web)==length_url_list:
            print(len(url_list_web), "break2")
            break
        elif len(url_list_web)>=100:
            print(len(url_list_web),"break1")
            break
        scroll_to_end()
        time.sleep(2)
        xpath = '//*[@id="botstuff"]/div/div[3]/div[4]/a[1]/h3/div'
        click_script = '''
        var xpath = arguments[0];
        var element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (element) {
            element.click();
        }
        '''
        driver.execute_script(click_script, xpath)

    return url_list_web

def url_check():
    global url_processed_list
    folder_path = r"C:\Users\Morning\Desktop\hiwi\case_spider\case"  # 请替换为实际的文件夹路径

    # 初始化空列表，用于存储'url'键的值

    # folder_path = './'  # 修改为你的文件夹路径
    for filename in os.listdir(folder_path):
        # 检查文件名是否符合条件
        if filename.startswith('content_') and filename.endswith('.jsonl'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                for line in file:
                    data = json.loads(line)
                    if 'Url' in data:
                        url_processed_list.append(data['Url'])
    return url_processed_list
url_check()
def case_search(search_term):

    def google_search(search_term, api_key, cse_id, start=1, num=10, **kwargs):
        search_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'q': search_term,
            'key': api_key,
            'cx': cse_id,
            'start': start,
            'num': num
        }
        params.update(kwargs)
        response = requests.get(search_url, params=params)
        return response.json()

    # 您的API密钥和自定义搜索引擎ID
    api_key = "AIzaSyABEdo1vb3VQJfwMU6NmqV239-H4vsfC-c"
    cse_id = "e1a862c0bafc544f5"

    # 搜索词
    # search_term = "Navigation Privacy Leak"

    # 执行搜索
    # results = google_search(search_term, api_key, cse_id)

    total_pages =10  # 总共获取3页的结果
    num_results_per_page = 10
    i=0
    # 循环执行搜索以获取多页结果
    for page in range(1, total_pages + 1):
        start_result = (page - 1) * num_results_per_page + 1
        print(f"Fetching page {page} starting at result {start_result}...")

        results = google_search(search_term, api_key, cse_id, start=start_result, num=num_results_per_page)

        # 输出本页的搜索结果
        for result in results.get('items', []):
            i+=1
            print(f"Title: {result.get('title')}")
            print(f"Snippet: {result.get('snippet')}")
            print(f"Link: {result.get('link')}")
            print("---")
            with open('%s.txt'%search_term.replace(" ","_"), 'a', encoding='utf-8') as fileread:
                fileread.write(f"Title: {result.get('title')}\n")
                fileread.write(f"Snippet: {result.get('snippet')}\n")
                fileread.write(f"Link: {result.get('link')}\n")
                fileread.write("---\n")
        time.sleep(2)  # 避免过于频繁的API调用

    print(i,"____________")



def construct_excel(file_path,url_list=None):
    #url_processed_list are urls have been processed
    global url_processed_list
    print(len(url_processed_list), "processed_url number")
    file_path=file_path.replace(" ","_")+".txt"
    from urllib.parse import urlparse
    import threading

    def each_process(data_queue, lock, num):
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:" + str(num))
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")
        print(num,"work!")
        while True:

                try:
                        url,url_num = data_queue.get(timeout=3)
                except queue.Empty:
                        print(num,"empty===========")
                        break
                if url not in url_processed_list:

                        url_processed_list.append(url)
                        print(url_num, "___________", (url))

                        result_list = text_get(driver, url)

                        # 创建一个 DataFrame
                        each_dict = {
                            'num': url_num,
                            'Time': result_list[0],
                            'Title': result_list[1],
                            'Content': result_list[2],
                            'From': get_domain(url),
                            'Url': url
                        }

                        # 读取现有的 JSON 文件，并将新的数据追加到文件中
                        filename = 'case/%s.jsonl' % ("content_" + file_path.replace(".txt", ""))

                        # 将更新后的数据写回文件
                        with lock:
                            with open(filename, 'a') as file:
                                file.write(json.dumps(each_dict) + "\n")
                else:
                    print(num,url,"processed url")


    def get_domain(url):


        # url = "https://www.xxxasdasd.com/some/path/?some=query"
        parsed_url = urlparse(url)

        # 获取域名
        domain = parsed_url.netloc
        print("Domain:", domain)

        # 如果域名包括 'www.', 可以去除
        if domain.startswith("www."):
            domain = domain[4:]
        return domain

    def timeout_get_text(driver, xpath_list):
        if isinstance(xpath_list,list):
            process_list=xpath_list
        else:
            process_list=[xpath_list]
        for xpath_str in process_list:
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_str))
                )
                if element:
                    return element.text
            except:
                continue
        return None

    def text_get(driver,title):
        driver.get(title)
        if 'bbc.com' in title:
            print('bbc.com')
            element_time = ('//*[@id="main-content"]/article/header/div[1]/ul/div/li/div[2]/span/span/time')
            element_content = ('//*[@id="main-content"]/article')
            element_content_title = ('//*[@id="main-heading"]')
        elif 'cnn.com' in title:
            print('cnn.com')
            element_time = ('/html/body/div[1]/section[2]/div[1]/div[2]/div[1]/div/div[2]')
            element_content = (
                '/html/body/div[1]/section[3]/section[1]/section[1]/article/section/main/div[2]')
            element_content_title = ('//*[@id="maincontent"]')
        elif 'theguardian' in title:
            print('theguardian')
            element_content_title = ['/html/body/main/article/div/div/div[3]/div/div/h1','/html/body/header/div[2]/div/section/div/div/div/h1/span']
            element_time = ['/html/body/main/article/div/div/aside[4]/div/div/div/div[1]/div/div','/html/body/main/article/div/div/aside[4]/div/div/div/div[1]/div/details/summary/span','/html/body/main/article/div/div/aside[2]/div/div/div/div[1]/div/details/summary/span']
            element_content = '//*[@id="maincontent"]/div'
        elif 'apnews' in title:
            print("apnews")
            element_content_title = '/html/body/div[3]/div[1]/div/h1'
            element_time = ['/html/body/div[3]/div[2]/main/div[1]/div[1]/div/div/div/bsp-timestamp/span','/html/body/div[3]/div[2]/main/div[2]/div[1]/div/div/div[2]/bsp-timestamp/span']
            element_content =[ '/html/body/div[3]/div[2]/main/div[1]/div[2]','/html/body/div[3]/div[2]/main/div[2]/div[2]']
        elif 'reuters.com' in title:
                element_content_title = ['//*[@id="main-content"]/article/div[1]/div/header/div/div/h1','//*[@id="__next"]/div/div[3]/div[2]/div/div/h1','/html/body/section/div[1]/div[2]/div/div/h1','//*[@id="USKBN17U2MU"]/div[1]/div[1]/div/div/div[1]/div/h1']
                element_time = ['//*[@id="main-content"]/article/div[1]/div/header/div/div/div/div[1]/time/span[1]','//*[@id="__next"]/div/div[3]/div[2]/div/div/div/div/time[1]','//*[@id="article-tktktktk"]/div[1]/div[3]/div/p[2]/time','//*[@id="USKBN17U2MU"]/div[1]/div[1]/div/div/div[1]/div/div[2]']
                element_content = ['//*[@id="main-content"]/article/div[1]/div/div/div/div[2]','//*[@id="__next"]/div/div[4]/div[1]/article/div[1]', '//*[@id="article-tktktktk"]/div[2]/div/div', '//*[@id="USKBN17U2MU"]/div[2]/div[1]/div/div[1]']

        else:
            print("TECHchurch")
            element_time = (
                '//*[@id="tc-main-content"]/div/div/div/article[1]/div[2]/div[2]/div[1]/header/div[2]/div[1]/span/time')
            element_content = ('//*[@id="tc-main-content"]/div/div/div/article[1]/div[2]/div[2]/div[2]')
            element_content_title = (
                '//*[@id="tc-main-content"]/div/div/div/article[1]/div[2]/div[2]/div[1]/header/div[1]/h1')

        text_time =timeout_get_text(driver,element_time)
        text_content = timeout_get_text(driver,element_content)
        text_title = timeout_get_text(driver,element_content_title)

        print("_______________________")
        print(text_time)
        print("_______________________")
        print(text_title)
        print("_______________________")
        print(text_content)
        print("_______________________")
        # text_content=selenium_spider(text_content)
        return [text_time,text_title,text_content]





    # Regular expression pattern to extract URLs
    url_pattern = re.compile(r'https?://[^\s]+')

    # Lists to store the categorized URLs


    # Extracting and categorizing the URLs
    i=0
    threads = []
    lock = threading.Lock()
    data_queue = queue.Queue()
    data_list=[]
    if not isinstance(url_list,list):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        for line in lines:
            match = url_pattern.search(line)
            if match:



                url = match.group()
                #在queue中去重
                if url not in data_list and "https" in url:
                    i += 1
                    data_list.append(url)
                    data_queue.put((url,i))
    else:
        for url in url_list:
            if url not in data_list and "https" in url:
                i += 1
                data_list.append(url)
                data_queue.put((url,i))
    for i in range(6):
        t = threading.Thread(target=each_process, args=(data_queue, lock, i + 9222))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


    # 保存到 Excel 文件
    # df.to_excel('%s.xlsx'%("content_"+file_path.strip(".txt")), index=True, engine='openpyxl')
"""
"Policy issues due to geographical mapping errors",
"Impact of mapping errors on international relations",
"Geographical inaccuracies affecting policy decisions",
"Boundary disputes caused by map inaccuracies",
"Policy implications of incorrect geographical data",
"""

key_word_list=[
# "autonomous driving accidents",
# "self-driving car crashes",
# "autonomous vehicle failures",
# "self-driving technology malfunctions",
# "Tesla Autopilot accidents",
# "driverless car incidents",
# "autonomous driving system errors",
# "Autonomous Vehicle accidents due to technical issues",

# "Navigation system failure",
# "GPS malfunction accidents",
# "Navigation system error incidents",
# "GPS misdirection incidents",
# "Vehicle accidents due to navigation errors",
#
# "GPS privacy breach",
# "Navigation system data leak",
# "Location tracking privacy issues",
# "Unauthorized GPS tracking",
# "Location data exposure"


# "Digital cartography disputes",
"Geospatial mapping controversies",
"Technical map-making errors",
"Geographic Information Systems inaccuracies",
"Border disputes due to digital mapping",
"Misrepresentation in digital maps",
"Geospatial data manipulation issues",
"Digital map bias",
"Mapping software glitches",
"Digital territorial disputes"
]

for num,key_word in enumerate(key_word_list):
    if num >=6:
        print(key_word,"processing",num)
        # case_search(key_word)
        url_list=url_web(key_word)
        if len(url_list)!=0:

            construct_excel(key_word,url_list)