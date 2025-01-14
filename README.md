+ spider.py用来爬取网页html信息并且写入相应的文件暂存

+ html_trans.py用来把前面所有的html文件转化为json文件并暂存

+ json_trans.py用来把前面所有的json文件一起写入xlsx文件

+ find.py和get.py是尝试阶段写的脚本，可以忽略

+ Seedrs_FirmList.xlsx是你发给我的源数据表

+ website.csv是提取出来的所有网站的网址

+ data.xlsx是经过上面json_trans.py文件转化后的数据表

+ data_copy.xlsx是在上面data基础上，做了一点修改，然后发给你的最后的版本

+ note.md是写项目的时候随手写的一点备忘

+ json_file文件夹用来存放所有json文件

+ raw_html文件夹用来存放所有的html文件

+ final_spider.py是尝试爬取单个公司全部信息的python脚本

+ get_all.py是用来爬取所有公司全部信息的脚本

+ get_name.py是用来给data添加公司名字的脚本

+ add_to_data是用来将前面爬取的html解析并且将最后一列补充进去的脚本

+ final_html文件夹是用来存储最终版html的目录