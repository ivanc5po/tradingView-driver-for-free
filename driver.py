
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
#chrome_options.add_argument('--headless')  ## headless 
chrome_options.add_argument('--disable-gpu')
wd = webdriver.Chrome(options=chrome_options)
wd.get('https://tw.tradingview.com/chart/bLOm64iW/')

is_buy_sell = "None"

time.sleep(5)
wd.find_element(by=By.XPATH, value='//*[@id="footer-chart-panel"]/div[1]/div[1]/div[2]/div').click()
time.sleep(1)
wd.find_element(by=By.XPATH, value='//*[@id="bottom-area"]/div[4]/div/div[1]/div[3]/div/div/div/div/div/button[3]').click()

while True:
  try:
    if is_buy_sell == "buy" and wd.find_element(by=By.XPATH, value='//*[@id="bottom-area"]/div[4]/div/div[2]/div/div/div/div/table/tbody[1]/tr[2]/td[2]').text == "StochSE": # StochSE要改成你策略設定的文字
        ### 賣出
        print("sell")
        is_buy_sell = "sell"
    elif is_buy_sell == "sell" and wd.find_element(by=By.XPATH, value='//*[@id="bottom-area"]/div[4]/div/div[2]/div/div/div/div/table/tbody[1]/tr[2]/td[2]').text == "StochLE":  # StochLE要改成你策略設定的文字
        ### 買入
        print("buy")
        is_buy_sell = "buy"
    elif is_buy_sell == "None":
        is_buy_sell = wd.find_element(by=By.XPATH, value='//*[@id="bottom-area"]/div[4]/div/div[2]/div/div/div/div/table/tbody[1]/tr[2]/td[2]').text
        print("start sell or buy : ", is_buy_sell)

  except:
    pass

  time.sleep(0.5)
