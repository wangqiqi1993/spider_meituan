爬取网站：美团美食类的火锅

url解析：http://bj.meituan.com/meishi/c17/pn32/，bj是地点，meishi是大的类别，c17代表火锅，pn{}表示第{}页

问题：在爬取的过程中，有些个别商店的格式和其他的商店是不一致的，解决方式将其过滤掉；遇到了unicodeEncodeerror问题，解释说是gbk在编码unicode码时有些码不能正常转换，网上搜了一些内容，可能自己没找对方式，没能很好解决，自己的解决方式，用空格将不能编码的字符替换掉

spider_meituan.py是简单的爬取程序，将爬取内容存放在csv文件中，用于后续的数据分析

多进程的处理：Pool,multiprocessing

Pool:




