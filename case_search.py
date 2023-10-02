import time

import requests
import json

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
search_term = "Navigation Privacy Leak"

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
