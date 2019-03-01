# coding=gbk
import requests
import os
url="https://www.nationalgeographic.com/travel/top-10/10-destinations-to-visit-for-african-american-history-and-culture/#/national-museum-of-african-american-history-washington-dc.jpg"
root="D://"
path= root + url.split('/')[-1]
kv = {'user-agent':'Mozilla/5.0'}

if not os.path.exists(root):
	os.mkdir(root)
if not os.path.exists(path):
	r=requests.get(url,timeout=30, headers=kv)
	print(r.status_code)
	with open(path,'wb') as f:
		f.write(r.content)
		f.close()
		print("文件保存成功")
else:
	print("文件已存在")

	
