import urllib.request

headers = {'User-Agent':'ChaiknowsTheBot',}
r = urllib.request.get("https://movie.douban.com/top250", hearders = headers)

html =r.txt
print(html)