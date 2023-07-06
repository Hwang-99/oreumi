from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num + 1
    else:
        return num + 9 * (num - 1)

def makeUrl(search, start_pg, end_pg):
    urls = []
    if start_pg == end_pg:
        start_page = makePgNum(start_pg)
        url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" +  str(start_page)
        urls.append(url)
        print("생성url: ", urls)
        return urls
    else:
        for i in range(start_pg, end_pg + 1):
            page = makePgNum(i)
            url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" +  str(page)



if __name__ == "__main__":


    #사용자 입력
    search = input("검색할 단어?\n")

    page_start = int(input("시작페이지?"))
    print(f"시작할 페이지: {page_start}")

    page_end = int(input("종료페이지?"))
    print(f"종료할 페이지: {page_end}")

    # 네이버 url 생성
    search_urls = makeUrl(search, page_start, page_end)

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)

    naver_urls = []

    for i in search_urls:
        driver.get(i)
        time.sleep(1)

        a = driver.find_elements(By.CSS_SELECTOR, 'a.info')
    
        for i in a:
            i.click()

            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)

            url = driver.current_url
            print(url)

            if "news.naver.com" in url:
                naver_urls.append(url)
                
            driver.close()

            driver.switch_to.window(driver.window_handles[0])

print(naver_urls)