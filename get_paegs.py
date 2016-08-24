# libraryのimport
import sys
from selenium import webdriver
import time
import os.path
import uuid

def get_pages_from_google(query):
    # 来訪すべきURLのリスト取得
    GOOGLE_URL = 'http://www.google.com'
    query_list = query.split()
    url_links = []
    browser = webdriver.Firefox()
    browser.get(GOOGLE_URL)
    search_input = browser.find_element_by_name('q') #inputフォームを見つける
    search_input.send_keys(query) # そのフォームにqueryメッセージをぶち込む
    search_input.submit() # そのqueryを送る
    time.sleep(1) # 1秒待つ (待たないと, 結果が全部表示される前に次のページに移るため. )
    titles = browser.find_elements_by_css_selector('h3.r') # 検索結果のタイトルを取得する. (webelementのリストで帰ってくる. )
    # 来訪すべきURLのリストを一つ一つ訪れる
    for i in titles:
        i = i.find_elements_by_css_selector('a') #webelementからアンカータグのwebelementを取り出す. (リスト形式で返ってくる)
        url_link = i[0].get_attribute('href') # アンカータグのwebelementに含まれているhrefのリンク先を取得
        url_links.append(url_link) # url_linksにurl_linkを追加していく
    for i in url_links:
        browser.get(i)
        file_name = os.path.join(os.path.dirname(os.path.abspath("__file__")), 'saved_images', str(uuid.uuid4())+'page.png')
        browser.save_screenshot(file_name)
        time.sleep(1)
