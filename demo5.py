# coding = utf-8
# @Time: 2020/11/24 20:18
import urllib.request
#urllib.request----请求
#urllib.request.urlopen----响应
response=urllib.request.urlopen("https://www.luogu.com.cn/problem/list?page=1&_contentOnly=1")
data=str(response.read().decode('unicode_escape'))
print(data)

