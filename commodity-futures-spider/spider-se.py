import requests
# import unittest
import selenium
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys


url_content = 'http://www.dce.com.cn/publicweb/quotesdata/dayQuotesCh.html'
url_xhr = 'http://www.dce.com.cn/dcestatistic/statisticAjax'
user_Agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'

headers_content = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cache-Control': 'max-age=0',
    'Content-Length': '69',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.dce.com.cn',
    'Referer': 'http://www.dce.com.cn/publicweb/quotesdata/dayQuotesCh.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
}

headers_xhr = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'WMONID=zhlVCQrEQiy',
    'Host': 'www.dce.com.cn',
    'Referer': 'http://www.dce.com.cn/publicweb/quotesdata/dayQuotesCh.html',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'X-Requested-With': 'XMLHttpRequest',
}

json_content = {
    'day': '06',
    'dayQuotes.trade_type': '0',
    'dayQuotes.variety': 'jd',
    'month': '4',
    'year': '2018',
}

json_xhr = {
    'pageId': 'rhqch',
    'requestUrl': 'aHR0cDovL3d3dy5kY2UuY29tLmNuL3B1YmxpY3dlYi9xdW90ZXNkYXRhL2RheVF1b3Rlc0NoLmh0bWw',
    'siteId': '459264',
    'type': 'publicweb',
}


fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

browser = webdriver.Firefox(firefox_profile=fp)
browser.get(url_content)

def get_elements(browser):
    months_elements = browser.find_elements_by_xpath('//*[@id="control"]/select[2]/option')
    years_elements = browser.find_elements_by_xpath('//*[@id="control"]/select[1]/option')
    days_elements = browser.find_elements_by_xpath('//*[@id="calender"]/table/tbody/tr[@class="week"]/td')
    return years_elements, months_elements, days_elements

# element = browser.find_element_by_xpath('//*[@id="dayQuotesForm"]/div/div[2]/ul[1]/li[2]/a')
# element.click()

# years_elements = browser.find_element_by_xpath('//*[@id="control"]/select[1]')
years_elements = browser.find_elements_by_xpath('//*[@id="control"]/select[1]/option')
for i in range(13, years_elements.__len__()):
    y_element = years_elements[i]
    print(y_element.text)
    y_element.click()
    months_elements = browser.find_elements_by_xpath('//*[@id="control"]/select[2]/option')
    for j in range(0, months_elements.__len__()):
        m_element = months_elements[j]
        print(m_element.text)
        m_element.click()
        days_elements = browser.find_elements_by_xpath('//*[@id="calender"]/table/tbody/tr[@class="week"]/td')
        for k in range(0, days_elements.__len__()):
            d_element = days_elements[k]
            if(d_element.text == ''):
                continue
            else:
                print(d_element.text)
                d_element.click()
                # browser.refresh()
                time.sleep(0.3)
                # try:
                #     download_button = browser.find_element_by_xpath('//*[@id="dayQuotesForm"]/div/div[2]/ul[1]/li[2]/a')
                #     download_button.click()
                # finally:
                #     pass
                js = "exportData('excel')"
                browser.execute_script(js)
                time.sleep(2)
                years_elements, months_elements, days_elements = get_elements(browser)


                # state = browser.find_element_by_xpath('//*[@id="dayQuotesForm"]/div/div[2]/p[2]/span')
                # if(state.text[-4] != '暂无数据'):
                #     js = "exportData('excel')"
                #     browser.execute_script(js)
            # print(d_element.text)
            # d_element.click()
            # browser.refresh()
            # js = "exportData('excel')"
            # browser.execute_script(js)


# js = "exportData('excel')"
# browser.execute_script(js)
browser.close()