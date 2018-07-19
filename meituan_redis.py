import requests
import re
import redis
from config import *
from multiprocessing import Process
num=4


def get_info():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'}
    #r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=password)
    url=r.spop('page_url')
    list=[]
    response=requests.get(url,headers=headers).text
    content_list=re.search('<script>(.*?),"poiInfos":(.*?),"comHeader":(.*?)</script>',response).group(2).rstrip('}}')
    for content in content_list.lstrip('[').rstrip(']').split('},'):
        #print(content)
        dict={}
        content=content+'}'
        if content.endswith('}}'):
            content=content.replace('}}','}')#stype:str
        try:
            dict['title']=eval(content)['title']#eval:str->dict
            dict['avgScore']=eval(content)['avgScore']
            dict['avgPrice']=eval(content)['avgPrice']
            dict['address']=eval(content)['address']
        except:
            pass
        list.append(dict)
    for ele in list:
        with open('/root/wcl2/spider_meituan/meituaninfo.csv','a')as fp:
            try:
                fp.write(str(ele['title']).replace('\u2022','')+'\t')
                fp.write(str(ele['avgScore']) + '\t')
                fp.write(str(ele['avgPrice']) + '\t')
                fp.write(str(ele['address']) + '\n')
            except:
                pass
if __name__=='__main__':
    start_url='http://bj.meituan.com/meishi/c17/pn{}/'#c17 stand for hotpot
    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=password)
    for page in range(1,10):
        url=start_url.format(page)
        r.sadd('page_url',url)
    processes=[]
    for i in range(0,num):
        p=Process(target=get_info,args=())
        p.start()
        processes.append(p)
    for p in processes:
        p.join()




