from bitkub import Bitkub
from IPython.display import clear_output
import time
import requests
import json
from datetime import datetime


# SETTING
coin = "KUB"
USD_THB_RATE = 33

def getbitkrub(coin):
  bitkub = Bitkub()
  bitkub_coin = 'THB_'+ coin  
  result = bitkub.ticker(sym=bitkub_coin)
  bitkub_price = result[bitkub_coin]['last']
  return bitkub_price
  
from songline import Sendline
from datetime import datetime
from pytz import timezone
fmt = "%Y-%m-%d %H:%M:%S"
token = 'Put Your Line Chat Bot Token Here'
m = Sendline(token)
coin = "KUB"

while(True):
  bitkub_price = getbitkrub(coin)
  now_time = datetime.now(timezone('Asia/Bangkok')).strftime(fmt)
  message = [now_time,coin,bitkub_price]
  m.sendtext(message)
  time.sleep(60)
