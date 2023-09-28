# 네이버 블로그 자동 글발행
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
import urllib.request

# selenium이 업데이트 되어서 이제 크롬 드라이버를 다운받지 않아도된다.
options = webdriver.ChromeOptions()
# 평소에 크롬브라우저로 쓰던 계정정보를 여기에 복붙하자.
# chrome://version/ => 프로필 경로
#=================================================================================================
# 네이버 로그인 캡쳐 우회방법
# 1. 그냥 아이디 입력이 아니라 ctrl+v로 아이디 입력
# 2. 실제 브라우저처럼 꾸미기
# 브라우저로 웹사이트를 접속할때 모든 걸 다 파악할 수 있다.
# 이 사람의 OS, 무슨 브라우저, 언제 접속, 어디서 접속, 프로필, 계정 등등
chrome_options = Options()
options.add_argument(r'user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data\Default')
options.add_experimental_option('excludeSwitches',['enable-logging'])
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=chrome_options)

# driver.get('https://m.naver.com/')
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/')
time.sleep(2)

pyperclip.copy('아이디') # ctrl+c가 된 상태
# driver.find_element(By.NAME, 'id').click()
e = driver.find_element(By.NAME, 'id')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v
time.sleep(2)

pyperclip.copy('비밀번호') # ctrl+c
e = driver.find_element(By.NAME, 'pw')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v
time.sleep(2)

e = driver.find_element(By.CLASS_NAME, 'btn_check').click()
#time.sleep(2)
#e.send_keys(Keys.ENTER)
time.sleep(10)

# 어떤 페이지를 거쳐왔는지 추적이 가능하다.
# 인간처럼 페이지 이동을 해야한다.
driver.get('https://m.blog.naver.com/FeedList.naver')
time.sleep(2)
driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FGoWriteForm.naver')
time.sleep(2)

# 셀레니움으로 내용 입력하고
# 클릭하고 싶은거 클릭, 발행
pyperclip.copy('제목') # ctrl+c
e = driver.find_element(By.CLASS_NAME, 'se_textarea')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v
time.sleep(2)

pyperclip.copy('내용') # ctrl+c
# <input>에다가 send_keys(파일경로) 이러면 파일업로드 됩니다.
e = driver.find_element(By.CLASS_NAME, 'se_editable.is-empty')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v
time.sleep(2)

e = driver.find_element(By.CLASS_NAME, 'btn_applyPost').click()
time.sleep(10)

# pip install pyperclip

driver.close()