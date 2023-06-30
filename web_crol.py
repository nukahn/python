from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import datetime
 
browser = webdriver.Chrome()
browser.get('https://cafe.naver.com/joonggonara')

time.sleep(3)
last_num = 0
j = 0
while j < 15:
    j += 1

    browser.switch_to.default_content()

    elem = browser.find_element(By.ID, 'topLayerQueryInput')
    elem.send_keys('판매'+ Keys.ENTER)

    iframe = browser.find_element(By.CSS_SELECTOR,"#cafe_main");
    browser.switch_to.frame(iframe)

    src = browser.page_source
    soup = BeautifulSoup(src, 'html.parser')

    #post_list = soup.select("div.article-board.result-board.m-tcol-c >table>tbody>tr")
    posts = soup.select("div.article-board.m-tcol-c > table > tbody > tr")


    #print(len(posts)) #posts 안에는 15개의 글이 있다.

    post_list = []

    for p in posts:
        post_dic= {'pnum':'','ptitle':'','pwriter':''}
        post_dic['pnum'] = p.select('div.inner_number')[0].text
        post_dic['ptitle'] = p.select('a.article')[0].text.strip()
        post_dic['pwriter'] = p.select('a.m-tcol-c')[0].text

        post_list.append(post_dic)


    if last_num == 0:
        last_num = post_list[0]['pnum']
        now = datetime.datetime.now()
        print("모니터링을 시작합니다.")
        print (str(now) + ": "+str(j)+"번째 시도. 최신 글번호는"+str(last_num)+"입니다.")
    else:
        for i in range(0, len(post_list)):
            if(post_list[i]['pnum'] <= last_num):
                del post_list[i:]
                break

        if(len(post_list) != 0):
            last_num = post_list[0]['pnum']

        
        print (str(now) + ": "+str(j)+"번째 시도. 새로운 글이 "+ str(len(post_list))+ "개 등록되었습니다. 최신 글번호는"+str(last_num)+"입니다.")
    
    time.sleep(360)

print(i)

#time.sleep(1)

