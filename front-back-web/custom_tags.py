from requests import get
from json import loads
from django import template

register = template.Library()

@register.simple_tag
def crawling():
    url = "https://forum.nexon.com/api/v1/board/1018/threads?alias=bluearchive&pageNo=1&paginationType=PAGING&pageSize=15&blockSize=5&_=1700919768522"
    r = get(url)

    js = loads(r.text)
    UT_dic = { }
    url_list = [ ]
    title_list = [ ]
    url2 = "https://forum.nexon.com/bluearchive/board_view?board=1018&thread="

    for i in range(1,6):
        url_list.append(url2 + js["threads"][i]["threadId"])
        title_list.append(f'{str(i)}. {js["threads"][i]["title"]}')
        UT_dic[url2 + js["threads"][i]["threadId"]] = [js["threads"][i]["title"]]

    result = []
    for j in range(5):
        result.append({
            'title': title_list[j],
            'url': url_list[j]
        })

    return result