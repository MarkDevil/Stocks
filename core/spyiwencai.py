# coding=utf-8
import requests


class SpyIwenCai:

    def __init__(self, stocktype):
        self.url = 'https://www.iwencai.com'
        self.stocktype = stocktype

    def open_web(self):
        response = requests.get(self.url)
        print(response.content)

    def select_strategy(self, strategy):
        pass


if __name__ == '__main__':
    SpyIwenCai('name').open_web()
