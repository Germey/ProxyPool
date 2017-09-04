import requests
from requests.exceptions import ProxyError,Timeout,ConnectionError,ChunkedEncodingError
import time
from fake_useragent import UserAgent
ua = UserAgent()

def get_proxy():
    r = requests.get('http://localhost:5000/get')
    proxy = r.text
    return proxy

def get_count_proxys():
    r = requests.get('http://localhost:5000/count')
    proxys = r.text
    return proxys

def crawl(url, proxy):
    proxies = {'http': proxy}
    r = requests.get(url, proxies=proxies,headers=headers,timeout=6)
    return r

def main():
    count = 0
    while True:
        # print('第 ',count,' 次测试')
        count = count + 1
        try:
            #请求不同的代理和headers
            global headers,count_proxys
            headers = {'User-Agent': ua.random}
            count_proxys = get_count_proxys()
            print('代理总数： ',count_proxys,'  当前所用的代理：',proxy,'\n',headers)
            start_time = time.clock()
            html = crawl('http://www.baidu.com', proxy)
            end_time = time.clock()
            print('代理连接时间： ',(str(end_time-start_time))[:4],' 秒')
            if html.status_code==200:
                print(html)
                return count
                break
            elif count>=10:
                print('抓取网页失败')
                break

        except (ChunkedEncodingError,ConnectionError,Timeout,UnboundLocalError,UnicodeError,ProxyError):
            global proxy
            proxy = get_proxy()
            print('代理失败,更换代理','\n')
            # print(' ')


proxy = get_proxy()
if __name__ == '__main__':
    count = 1
    while count<=20:
        print(count)
        count = count + 1
        print('\n ','***********************',main(),'***********************','\n ')


