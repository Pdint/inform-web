import pandas as pd
"""
from crawling_test import crawling

a = crawling()
print(a)
"""
import json

data = pd.read_csv("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv",encoding='utf-8')
df = pd.DataFrame(data)

    # 데이터프레임을 HTML로 변환
html_output = df.to_html(classes='table table-bordered table-striped', index=False)
print(html_output)
    #context = {'html_output': html_output}
    #context_json = json.dumps(context)
    #data = json.dumps(html_output)
"""json_data = df.to_json(orient='records')
with open("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.json", 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

with open("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.json", 'w', encoding='utf-8') as new_json_file:
    json.dump(json_data, new_json_file, ensure_ascii=False, indent=4)
"""





"""
csv_file = pd.read_csv("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv",encoding='utf-8')
# print(csv_file.head(10))
df = pd.DataFrame(csv_file)
html_output = df.to_html(classes='table table-bordered table-striped', index=False)
data = json.dumps(html_output)
print(data)
#html = csv_file.to_html(index=False, justify='center')

#df = pd.DataFrame(csv_file)

#html_output = df.to_html(classes='table table-bordered table-striped', index=False)
#context = {'html_output': html_output, 'django_variable': 'Hello from Django!'}
#print(html_output)
"""




"""
data = pd.read_csv("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv",encoding='utf-8')
data = data.loc[::-1].reset_index(drop=True)
df = pd.DataFrame(data[['summary']])
print(df)
"""



"""
import pandas as pd
import pymysql

# DB 정보
host = "localhost"
user = "root"
password = "yuyuno1234!@"
database = "test"

# 엑셀 파일 불러오기
df = pd.read_csv("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv",encoding='utf-8')
df = df.where((pd.notnull(df)), None)
print(df)

# DB 연결
conn = pymysql.connect(host=host, user=user, password=password, db=database)
curs = conn.cursor(pymysql.cursors.DictCursor)

# DB insert
sql = 'INSERT INTO topic (title, news, summary) VALUES(%s, %s, %s)'

for idx in range(len(df)):
	curs.execute(sql, tuple(df.values[idx]))

conn.commit()

#종료
curs.close()
conn.close()
"""