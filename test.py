#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 11:13
import json
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


proxy = requests.get('http://127.0.0.1:5000/get').text
print('Get proxy from API: {}'.format(proxy))
proxies = {'http': 'http://{}'.format(proxy), 'https': 'http://{}'.format(proxy)}
response = requests.get(url='https://httpbin.org/ip', proxies=proxies)
print('Status Code: {}'.format(response.status_code))
print('Response text: {}'.format(response.text))


# 设置 -- 使用代理/不加载图片/不显示界面
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))
chrome_options.set_headless(True)
prefs = {'profile.default_content_setting_values': {'images': 2}}
chrome_options.add_experimental_option('prefs', prefs)
while True:
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(3)
    driver.get('https://httpbin.org/ip')
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'pre'))
        )
        content = driver.find_element_by_css_selector('pre').get_attribute('textContent')
        ip = json.loads(content)['origin']
        break
    except Exception as e:
        print(e)
print('Chrome Response: {}'.format(ip))

