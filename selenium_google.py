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
    while len(url_list_web)<url_num:
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
            break
        scroll_to_end()

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