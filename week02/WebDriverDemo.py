from selenium import webdriver
import time

#使用绝对路径也可以，但从项目开发角度来说这个方式不好，还是放到虚拟环境当中合适
#browser = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver')
browser = webdriver.Chrome()

# 登录
def weibo_login(username, password):
    # 打开登录页
    browser.get('https://shimo.im/login?from=home')
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息：用户名、密码
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(username)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(password)
    time.sleep(1)
    # 点击登录
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    time.sleep(1)

# 设置用户名、密码
username = 'cl20070706@163.com'
password = "密码"
weibo_login(username, password)
