import os
import time

if __name__ == '__main__':
    while True:
        os.system("scrapy crawl smzd")
        # 每２个小时执行一次　６０＊６０＊２
        time.sleep(7200)

