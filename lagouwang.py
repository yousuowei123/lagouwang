# auth: c_tob

import requests, json, csv


def get_content(page):
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    # params = {
    #     'city': '深圳',
    #     'needAddtionalResult': 'false',
    #     'isSchoolJob': 0
    # }
    data = {
        'first': 'true',
        'pn': page,
        'kd': 'python'
    }
    r = requests.post(url,data=data)
    print(r.status_code)
    return r.text


if __name__ == "__main__":
    html = get_content(1)
    print(html)
