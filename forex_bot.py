#自動查匯率並發送
inport os
import requests
import pandas as pd
from io import StringIO

headers = {'User-Agent':'Mozilla/5.0 '}
ur1 = "https://rate.bot.com.tw/xrt/flcsv/0/day"
res = requests.get(ur1,headers=headers)
res.encoding = 'utf-8'
csv_data = StringIO(res.text)
df = pd.read_csv(csv_data,index_col=False)
currency = 'USD'
usd_row = df[df['幣別'].str.contains(currency)].iloc[0]

chat_id = os.environ.get('TG_CHAT_ID')
token = os.environ.get('TG_BOT_TOKEN')

text = f"{currency}匯率:\n幣別:{usd_row['幣別']}\n本行買入:{usd_row['現金']}\n本行賣出:{usd_row['現金.1']}"
output_TB = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
requests.get(output_TB)
