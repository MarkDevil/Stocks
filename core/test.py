# coding=utf-8
import requests
import re


def crawlkuaidaili():

    print('start crawl {}'.format('.....'))
    for page in range(1, 4):
        # start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
        start_url = 'https://www.kuaidaili.com/free/inha/1/'
        html = requests.get(start_url)
        ip_adress = re.compile(
            '<td resource-title="IP">(.*)</td>\s*<td resource-title="PORT">(\w+)</td>'
        )
        re_ip_adress = ip_adress.findall(html)
        for adress, port in re_ip_adress:
            result = adress + ':' + port

            yield result.replace(' ', '')

crawlkuaidaili()