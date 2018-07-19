import requests
import re
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
def get_info(url,headers):
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
    return list
def saveinfo(list):
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
    for page in range(1,100):
        url=start_url.format(page)
        info=get_info(url,headers)
        saveinfo(info)
