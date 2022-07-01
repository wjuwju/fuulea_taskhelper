from email import header
import imp
from multiprocessing.spawn import import_main_path
from tkinter import N
from matplotlib.font_manager import json_load
import requests
import re
import json

#user = str(input(''))
#password = str(input(''))

subject_num = input(str('语文7\n数学1\n英语6\n物理3\n地理9\n化学2\n生物5\n历史8\n政治10\n美术63\n'))
url = 'https://api.fuulea.com/v2/auth/student/login/'
headers = {
    'accept': 'application/json, text/plain, */*',
    'app-version': '2.1.3',
    'version': '2.1.3',
    'user-agent': 'saturn/2.0 (Android 11)',
    'serial': 'unknown',
    'content-length': '0',
    'accept-encoding': 'gzip'
}
data = {
    'username':'88426102',
    'password':'88426102lcx'
    }
req  = requests.post(url,headers=headers,json=data)
token = req.text
uesr_cookie = req.cookies
auth = re.findall('"token":"(.*?)",',token)
token_header = {
    'accept': 'application/json, text/plain, */*',
    'app-version': '2.1.3',
    'version': '2.1.3',
    'user-agent': 'saturn/2.0 (Android 11)',
    'serial': 'unknown',
    'authorization':'jwt '+str(auth[0]),
    'content-length': '0',
    'accept-encoding': 'gzip'
}
print(token_header['authorization'])
cookie = requests.utils.dict_from_cookiejar(uesr_cookie)
for page in range(1,10):
    task_url = 'https://api.fuulea.com/v2/tasks/students/?page=1&pageSize=50&subjectId='+subject_num+'&finished=false&title='
    print(task_url)
    task = requests.get(task_url,headers=token_header,cookies=cookie)
    taskrep= task.text
    print(taskrep)
    task_id = re.findall('"taskId":(.*?),',taskrep)
    moudle =re.findall('"taskDetailId":(.*?),',taskrep)
    title = re.findall('"title":"(.*?)",',taskrep)
    len_id = len(task_id)
    for i in range(0,int(len_id)):
        try:
            fin_url ='https://api.fuulea.com/v2/tasks/'+task_id[i]+'/detail/'+moudle[i]+'/mark-finish/'
            print(fin_url)
            t = requests.post(fin_url,headers=token_header,cookies=cookie)
            print(i,task_id[i],title[i],t.text)
        except:
            break
    
