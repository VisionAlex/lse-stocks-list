import pandas as pd
from sqlalchemy import create_engine
import pymysql
import requests

user = ""
password = ""
host = ""
db = ""

url ="https://docs.londonstockexchange.com/sites/default/files/reports/Instrument%20list_1.xlsx"
response = requests.get(url)
with open('lse_data.xlsx','wb') as f:
    f.write(response.content)

data = pd.read_excel('lse_data.xlsx', skiprows=[0,1,2,3,4,5,6])


engine =create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')
con = engine.connect()

try:
	data.to_sql(con=con, name='LSE', if_exists="replace")
	print('LSE Table Created Successfully')
except Exception as e:
	print(e)
finally:
	con.close()

engine.dispose()
