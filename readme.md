爬取网站：美团美食类的火锅

url解析：http://bj.meituan.com/meishi/c17/pn32/，bj是地点，meishi是大的类别，c17代表火锅，pn{}表示第{}页

问题：在爬取的过程中，有些个别商店的格式和其他的商店是不一致的，解决方式将其过滤掉；遇到了unicodeEncodeerror问题，解释说是gbk在编码unicode码时有些码不能正常转换，网上搜了一些内容，可能自己没找对方式，没能很好解决，自己的解决方式，用空格将不能编码的字符替换掉

spider_meituan.py是简单的爬取程序，将爬取内容存放在csv文件中，用于后续的数据分析

多进程的处理：Pool,Process

Pool:

from multiprocessing import Pool,Process
#实例化进程池，并确定进程池的个数
pool=Pool(4)#最好是跟自己的cpu的数目相匹配
常用的进程池的函数pool.apply_async(func,args=(,)),apply_async(func[, args[, kwds[, callback]]])
   与apply用法一致，但它是非阻塞的且支持结果返回后进行回调。
 实例：
 
from multiprocessing import Pool
from time import sleep 
def f(x):
    for i in range(10):
        print '%s --- %s ' % (i, x)
        sleep(1) 
def main():
    pool = Pool(processes=3)    # set the processes max number 3
    for i in range(11,20):
        result = pool.apply_async(f, (i,))#将所有的运行程序都放到进程池中
    pool.close()#关闭进程池，不允许向进程池中添加函数
    pool.join()#阻塞等待
    if result.successful():
        print 'successful' 
if __name__ == "__main__":
    main()


