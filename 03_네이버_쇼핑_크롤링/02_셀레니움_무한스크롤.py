from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

 
# 브라우저 생성
browser = webdriver.Chrome('C:/chromedriver.exe')
# mac 의 경우 /User/startcoding/Documents/chromedriver

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다림

# 쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(1) # 로딩이 끝날 때까지 1초까지는 기다림

# 검색창 클릭
search = browser.find_element_by_css_selector('input._searchInput_search_input_QXUFf')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script('return window.scrollY') # execute_script : 자바스크립트의 명령어를 실행할 수 있다.

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END) # 키보드의 END키

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(0.5)

    # 스크롤 후 높이
    after_h = browser.execute_script('return window.scrollY')

    if after_h == before_h:
        break
    before_h = after_h

items = browser.find_elements_by_css_selector('.basicList_info_area__17Xyo')

for item in items:
    name = item.find_element_by_css_selector('.basicList_title__3P9Q7').text
    try:
        price = item.find_element_by_css_selector('.basicList_price_area__1UXXR').text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector('.basicList_title__3P9Q7 > a').get_attribute('href')
    print(name,price,link)