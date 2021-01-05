# coding=utf-8
import os
import requests

url = 'https://www.pgyer.com/apiv2/appGroup/listAll'
api_key = 'xxx'


def upload_apk(url, file_path, api_key):
    # postdata = {
    #     'file': file_path,
    #     '_apk_key': apk_key,
    #     'buildUpdateDescription': get_gitlog()
    # }

    postdata = {
        '_api_key': api_key
    }
    rep = requests.post(url, postdata)
    print(rep.content)


def get_gitlog():
    command = 'git log --pretty="%h %cd %s " -n5 --no-merges | cat'
    return os.system(command)


def run(workspace, url=None, api_key=None, file_path=None):
    os.chdir(workspace)
    get_gitlog()
    print(api_key)
    upload_apk(url=url, api_key=api_key, file_path=file_path)


if __name__ == '__main__':
    run(workspace='/Users/mark', url=url, api_key=api_key, file_path='')
