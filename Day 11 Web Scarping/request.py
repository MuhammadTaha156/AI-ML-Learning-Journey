import requests as r
url="https://www.scrapethissite.com/pages/simple/"
res=r.get(url)

if res.status_code==200:
    # print(res.text)
    # print(res.content)
    print(res.headers)