import requests
import sqlite3
import yaml


#url = "https://m.store.naver.com/sogum/api/businesses?filterId=r09&menu=2&query=%EC%84%9C%EC%9A%B8%20%EC%B9%B4%ED%8E%98&searchQuery=%EC%84%9C%EC%9A%B8%20%EC%B9%B4%ED%8E%98&display=1&deviceType=mobile"
url = 'https://m.store.naver.com/sogum/api/businesses?disaplay=1&filterId=r09215107&menu=1&query=%ED%99%94%EC%96%91%EB%8F%99%20%EC%B9%B4%ED%8E%98%20%EB%A7%9B%EC%A7%91&searchQuery=%ED%99%94%EC%96%91%EB%8F%99%20%EC%B9%B4%ED%8E%98%20%EB%A7%9B%EC%A7%91&x=126.9783880&y=37.5666100&start=1&display=1&deviceType=mobile'

check =0
query = '&start='
count=1

conn=sqlite3.connect ("./db.sqlite3")
conn2=sqlite3.connect('./db.sqlite3')


cur=conn.cursor()
cur2=conn2.cursor()
for i in range(1,5000000):

	attackquery=url+query+str(i)
	print attackquery

	res=requests.get(attackquery)


	infotext= res.text
	info_cafe=yaml.load(infotext)

	try :
		roadAddr= ((info_cafe['items'][0])['roadAddr']).replace("'","\'")
		phone= ((info_cafe['items'][0])['phone']).replace("'","\'")
		x= ((info_cafe['items'][0])['x']).replace("'","\'")
		y= ((info_cafe['items'][0])['y']).replace("'","\'")
		name= ((info_cafe['items'][0])['name']).replace("'","\'")
		sql_select='select * from cafe_cafeinfo where phone ="'+phone+'" and x="'+x+'";'

		print sql_select

		cur.execute(sql_select)
		
		for row in cur:
			if(row[1]==phone and row[2]==x):
				check=1

	except:
		roadAddr= ''
                phone= ''
                x= (info_cafe['items'][0])['x']
                y= (info_cafe['items'][0])['y']
                name= (info_cafe['items'][0])['name']
	
	if(check ==1):
		check=0
		print '!!!!!!!!!!!!!already!!!!!!!!!!!!!\n'
		continue
	
	sql="insert into cafe_cafeinfo(cafename,phone,x,y,roadAddr) values (?,?,?,?,?)"

	cur2.execute(sql,(name,phone,x,y,roadAddr))
	conn.commit()
	conn2.commit()
	if((infotext).find('"total":0')>1):
                break
                print i


conn.close()




