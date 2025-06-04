#自動查匯率並發送
import requests
import pandas as pd
from io import StringIO

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
ur1 = "https://rate.bot.com.tw/xrt/flcsv/0/day"
res = requests.get(ur1,headers=headers)
res.encoding = 'utf-8'
csv_data = StringIO(res.text)
df = pd.read_csv(csv_data,index_col=False)
currency = 'USD'
usd_row = df[df['幣別'].str.contains(currency)].iloc[0]

chat_id = 7700693983
text = f"{currency}匯率:\n幣別:{usd_row['幣別']}\n本行買入:{usd_row['現金']}\n本行賣出:{usd_row['現金.1']}"
output_TB = f"https://api.telegram.org/bot8168282078:AAHxAb8g-l_uRHhbeemMyDw2nc2fBWJSnC4/sendMessage?chat_id={chat_id}&text={text}"
requests.get(output_TB)
